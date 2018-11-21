from django.conf import settings

from core.models import TradeMark


def trade_marks(request):
    return {'trade_marks': TradeMark.objects.all()}


def stripe_pk_key(request):
    return {'stripe_pk_key': settings.STRIPE_PUBLIC_KEY}