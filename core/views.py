from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

from core.models import Products, TradeMark


class Home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        products = Products.objects.all().select_related().order_by('price')[:2]  # JOIN for ForeignKey
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

