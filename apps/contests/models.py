from django.db import models
from apps.common.models import EditMixin
from apps.stockmarket.models import Price
from django.contrib.auth.models import User


DEFAULT_USER = 1
DEFAULT_RECORD = 1
DEFAULT_NET_INCOME = 0
DEFAULT_PRICE = 0


class Record(models.Model):
    trader = models.ForeignKey(User, null=False, default=DEFAULT_USER)
    wins = models.IntegerField(null=True, default=0)
    losses = models.IntegerField(null=True, default=0)
    net_income = models.DecimalField(max_digits=12, decimal_places=2, default=DEFAULT_NET_INCOME)
    def __str__(self):
        return "{} ({}-{})".format(self.trader, str(self.wins), str(self.losses))


class Game(models.Model):
    contestant = models.ForeignKey("Record", related_name='contestant')
    opponent = models.ForeignKey("Record", related_name='opponent')
    winner = models.ForeignKey("Record", related_name='winner')
    def __str__(self):
        return "{} vs {}".format(self.contestant, self.opponent)


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('BO', "BUY-TO-OPEN"),
        ('BC', "BUY-TO-CLOSE"),
        ('SO', "SELL-TO-OPEN"),
        ('SC', "SELL-TO-CLOSE"),
    )
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPES, default="H")
    shares = models.IntegerField(null=False, default=0)
    quote = models.ForeignKey(Price, null=False, default=DEFAULT_PRICE)
    contest = models.ForeignKey(Game)
    def __str__(self):
        return "{} {} shares of {} at {}".format(self.transaction_type, self.shares, self.quote.ticker, self.quote)