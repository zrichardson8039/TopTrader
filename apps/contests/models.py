from django.db import models
from apps.stockmarket.models import Price
from django.contrib.auth.models import User


DEFAULT_USER = 1
DEFAULT_RECORD = 1
DEFAULT_NET_INCOME = 0
DEFAULT_PRICE = 0


class Game(models.Model):
    trader = models.ForeignKey(User, null=False, default=DEFAULT_USER)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=100000)
    margin = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return ("{} - {}".format(self.trader, self.net_income))


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('B', "BUY"),
        ('S', "SELL"),
    )
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES)
    shares = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=DEFAULT_PRICE)
    commission = models.IntegerField(null=False, default=15)
    game = models.ForeignKey(Game)
    def __str__(self):
        return "{} {} shares at {}".format(self.transaction_type, self.shares, self.price)