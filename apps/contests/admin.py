from django.contrib import admin
from .models import Game, Transaction


class GameAdmin(admin.ModelAdmin):
    list_display = ('trader', 'won', 'net_income')
    search_fields = ['trader', 'won']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'shares', 'price', 'game')
    list_filter = ['transaction_type']


admin.site.register(Game, GameAdmin)
admin.site.register(Transaction, TransactionAdmin)


