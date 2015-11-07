from django import forms
from .models import Game, Transaction

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['trader']

    def clean_net_income(self):
        net_income = self.cleaned_data.get('net_income')
        return net_income

    def clean_buys(self):
        buys = self.cleaned_data.get('buys')
        return buys

    def clean_sells(self):
        sells = self.cleaned_data.get('sells')
        return sells

    def clean_buys_proceeds(self):
        buys_proceeds = self.cleaned_data.get('buys_proceeds')
        return buys_proceeds

    def clean_sells_proceeds(self):
        sells_proceeds = self.cleaned_data.get('sells_proceeds')
        return sells_proceeds

    def clean_commissions(self):
        commissions = self.cleaned_data.get('commissions')
        return commissions


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['game', 'transaction_type']

    def clean_shares(self):
        shares = self.cleaned_data.get('shares')
        return shares

    def clean_price(self):
        price = self.cleaned_data.get('price')
        return price

    def clean_transaction_type(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        return transaction_type


