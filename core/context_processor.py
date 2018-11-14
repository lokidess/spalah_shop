from core.models import TradeMark


def trade_marks(request):
    return {'trade_marks': TradeMark.objects.all()}
