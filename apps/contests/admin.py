from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('trader', 'cash', 'margin', 'shares', 'stock_value', 'net_income')
    search_fields = ['trader']


admin.site.register(Portfolio, PortfolioAdmin)


