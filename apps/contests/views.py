from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render
from rest_framework import viewsets
from apps.contests.serializers import PortfolioSerializer
from apps.common.permissions import ReadOnly
from .models import Portfolio
from .forms import PortfolioForm


def play(request):
    portfolio = Portfolio.objects.get(trader=auth.get_user(request))

    form = PortfolioForm(request.POST or None)
    if form.is_valid():
        portfolio.cash = form.cleaned_data['cash']
        portfolio.margin = form.cleaned_data['margin']
        portfolio.shares = form.cleaned_data['shares']
        portfolio.stock_value = form.cleaned_data['stock_value']
        portfolio.net_income = form.cleaned_data['net_income']
        portfolio.save()
        return HttpResponseRedirect('/profile/')
    else:
        form.fields['cash'].initial = portfolio.cash
        form.fields['margin'].initial = portfolio.margin
        form.fields['shares'].initial = portfolio.shares
        form.fields['stock_value'].initial = portfolio.stock_value
        form.fields['net_income'].initial = portfolio.net_income

        context = {"form": form }
        return render(request, "play.html", context)


def profile(request):
    portfolio = Portfolio.objects.get_or_create(trader=auth.get_user(request))
    portfolio = portfolio[0]
    context = {
        "portfolio": portfolio,
        "net_income": portfolio.net_income,
        "cash": portfolio.cash,
        "margin": portfolio.margin,
        "shares": portfolio.shares,
        "stock_value": portfolio.stock_value
    }

    return render(request, "profile.html", context)


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [ReadOnly, ]