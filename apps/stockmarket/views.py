from rest_framework import viewsets
from apps.stockmarket.models import Stock, Price
from apps.stockmarket.serializers import StockSerializer, PriceSerializer
from apps.common.permissions import ReadOnly
from django.shortcuts import render_to_response
from django.template import RequestContext


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [ReadOnly, ]

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [ReadOnly, ]