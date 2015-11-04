from django.db import models
from apps.stockmarket.models import Price
from django.contrib.auth.models import User


DEFAULT_USER = 1
DEFAULT_RECORD = 1
DEFAULT_NET_INCOME = 0
DEFAULT_PRICE = 0


class Game(models.Model):
    trader = models.ForeignKey(User, null=False, default=DEFAULT_USER)
    won = models.BooleanField(null=False, default=False)
    net_income = models.DecimalField(max_digits=12, decimal_places=2, default=DEFAULT_NET_INCOME)
    def __str__(self):
        if self.won:
            return "WON"
        return "LOST"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('BO', "BUY-TO-OPEN"),
        ('BC', "BUY-TO-CLOSE"),
        ('SO', "SELL-TO-OPEN"),
        ('SC', "SELL-TO-CLOSE"),
    )
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPES, default="H")
    shares = models.IntegerField(null=False, default=0)
    price = models.ForeignKey(Price, null=False, default=DEFAULT_PRICE)
    game = models.ForeignKey(Game)
    def __str__(self):
        return "{} {} shares at {}".format(self.transaction_type, self.shares, self.quote)