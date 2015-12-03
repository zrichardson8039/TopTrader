from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['trader']

    def clean_cash(self):
        cash = self.cleaned_data.get('cash')
        return cash

    def clean_margin(self):
        margin = self.cleaned_data.get('margin')
        return margin

    def clean_shares(self):
        shares = self.cleaned_data.get('shares')
        return shares

    def clean_stock_value(self):
        stock_value = self.cleaned_data.get('stock_value')
        return stock_value

    def clean_net_income(self):
        net_income = self.cleaned_data.get('net_income')
        return net_income


