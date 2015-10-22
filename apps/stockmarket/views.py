from rest_framework import viewsets
from apps.stockmarket.models import Stock, Price
from apps.stockmarket.serializers import StockSerializer, PriceSerializer
from apps.common.permissions import ReadOnly
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request):
    title = "Welcome | TopTrader"
    context {
        'title': title,
    }

    return render(request, "index.html", {})



class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [ReadOnly, ]

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [ReadOnly, ]