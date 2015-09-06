from rest_framework import serializers
from apps.stockmarket.models import Stock, Price


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
