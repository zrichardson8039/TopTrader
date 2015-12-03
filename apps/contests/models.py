from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    trader = models.ForeignKey(User, null=False, default=1)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=100000)
    margin = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    shares = models.IntegerField(default=0)
    stock_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return ("{} - {}".format(self.trader, self.net_income))