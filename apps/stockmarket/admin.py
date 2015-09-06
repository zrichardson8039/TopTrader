from django.contrib import admin
from .models import Stock, Price


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker')
    search_fields = ['name', 'ticker']


class PriceAdmin(admin.ModelAdmin):
    list_display = ('date', 'stock', 'price')
    search_fields = ['stock']


admin.site.register(Stock, StockAdmin)
admin.site.register(Price, PriceAdmin)


