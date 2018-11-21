from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from core.forms import RegisterForm
from core.models import Products, TradeMark


class Home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        products = Products.objects.filter(
            status=Products.STATUS_IN_STOCK
        ).select_related().order_by('price')[:12]  # JOIN for ForeignKey
        context['products'] = products
        return context


class TradeMarkView(ListView):
    template_name = 'trade_mark.html'
    model = Products

    def get_queryset(self):
        # trade_mark = TradeMark.objects.get(id=self.kwargs['trade_mark_id'])
        trade_mark = get_object_or_404(TradeMark, id=self.kwargs['trade_mark_id'])
        queryset = self.model.objects.filter(trade_mark=trade_mark)
        # queryset = self.model.objects.filter(
        #     trade_mark__id=self.kwargs['trade_mark_id'],
        #     count__gt=0
        # )
        return queryset


class Register(FormView):
    template_name = 'auth/registration.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class CheckoutView(View):

    def post(self, request, *args, **kwargs):
        import stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product = Products.objects.get(id=kwargs['product_id'])
        stripe.Charge.create(
            amount=int(product.price_for_stripe),
            currency="usd",
            source=request.POST['stripeToken'],  # obtained with Stripe.js
            description=""
        )
        product.count -= 1
        product.save()
        return redirect(reverse('thank_you'))


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'
