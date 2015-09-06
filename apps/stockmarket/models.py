from django.db import models
from apps.common.models import EditMixin


DEFAULT_STOCK_ID = 1
DEFAULT_PRICE = 0
DEFAULT_TICKER = 'NONE'
DEFAULT_URL = ''

class Stock(EditMixin):
    name = models.CharField(max_length=128, unique=True, blank=False, default=DEFAULT_TICKER)
    ticker = models.CharField(max_length=6, unique=True, blank=False, default=DEFAULT_TICKER)
    has_prices = models.BooleanField(default=False)
    prices_url = models.CharField(max_length=256, blank=True, default=DEFAULT_URL)
    def __str__(self):
        return self.name

class Price(EditMixin):
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=DEFAULT_PRICE)
    stock = models.ForeignKey('Stock', null=False, default=DEFAULT_STOCK_ID)
    def __str__(self):
        return str(self.price)
