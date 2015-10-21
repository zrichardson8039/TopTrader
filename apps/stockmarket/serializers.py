from rest_framework import serializers
from apps.stockmarket.models import Stock, Price


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        field = ("id", "name")

class PriceSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = Price
        field = ("id", "stock", "date")
