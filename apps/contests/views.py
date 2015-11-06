from django.contrib import auth
from django.shortcuts import render
from rest_framework import viewsets
from apps.contests.serializers import GameSerializer, TransactionSerializer
from apps.common.permissions import ReadOnly
from .models import Game, Transaction
from .forms import EndGameForm, TransactionForm


def NewGame(request):
    game = Game.objects.create(trader=auth.get_user(request))
    form1 = EndGameForm(request.POST or None)
    if form1.is_valid():
        net_income = form1.cleaned_data['net_income']
        won = False
        if net_income > 0:
            won = True
        game.net_income = net_income
        game.won = won
        game.save()

    form2 = TransactionForm(request.POST or None)
    if form2.is_valid():
        shares = form2.cleaned_data['shares']
        price = form2.cleaned_data['price']
        transaction_type = form2.cleaned_data['transaction_type']
        transaction = Transaction.objects.create(game=game, shares=shares, price=price, transaction_type=transaction_type)
        transaction.save()
    context = {
        "game_form": form1,
        "transaction_form": form2
    }
    return render(request, "play.html", context)


def profile(request):
    games = Game.objects.filter(trader=auth.get_user(request))
    all_games = []
    for g in games:
        buy_to_open = Transaction.objects.filter(game=g, transaction_type='BO').count()
        buy_to_close = Transaction.objects.filter(game=g, transaction_type='BC').count()
        sell_to_open = Transaction.objects.filter(game=g, transaction_type='SO').count()
        sell_to_close = Transaction.objects.filter(game=g, transaction_type='SC').count()
        game_details = {
            "game_id": g.id,
            "net_income": g.net_income,
            "buy_to_open": buy_to_open,
            "buy_to_close": buy_to_close,
            "sell_to_open": sell_to_open,
            "sell_to_close": sell_to_close
        }
        all_games.append(game_details)
    context = {
        "all_games": all_games
    }

    return render(request, "profile.html", context)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [ReadOnly, ]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ReadOnly, ]