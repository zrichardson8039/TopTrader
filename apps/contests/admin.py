from django.contrib import admin
from .models import Record, Game, Transaction


class RecordAdmin(admin.ModelAdmin):
    list_display = ('trader', 'wins', 'losses', 'net_income')
    search_fields = ['trader']


class GameAdmin(admin.ModelAdmin):
    list_display = ('contestant', 'opponent', 'winner')
    search_fields = ['contestant', 'opponent']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'shares', 'quote', 'contest')
    list_filter = ['transaction_type']


admin.site.register(Record, RecordAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Transaction, TransactionAdmin)


