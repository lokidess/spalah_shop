from django.contrib import admin
from core.models import TradeMark, Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'get_total')
    search_fields = ('name', 'trade_mark__name')

    def get_total(self, obj):
        return obj.price * obj.count
    get_total.short_description = 'Total'


admin.site.register(TradeMark)
admin.site.register(Products, ProductAdmin)
