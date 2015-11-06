from django import forms
from .models import Game, Transaction

class EndGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['net_income']

    def clean_net_income(self):
        net_income = self.cleaned_data.get('net_income')
        return net_income


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


