from django.contrib import auth
from django.shortcuts import render
from rest_framework import viewsets
from apps.contests.serializers import GameSerializer, TransactionSerializer
from apps.common.permissions import ReadOnly
from .models import Game, Transaction
from .forms import GameForm, TransactionForm


def new_game(request):
    game = Game.objects.create(trader=auth.get_user(request))
    game.save()

    context = {
        "game_id": game.id
    }
    return render(request, "play.html", context)


def submit_game(request):
    game = Game.objects.filter(trader=auth.get_user(request)).reverse()[0]
    context = {
        'net_income': game.net_income,
        'cash': game.cash,
        'margin': game.margin,
        'stock': game.stock,
        'total_value': game.total_value,
    }
    return render(request, "submitgame.html", context)


def profile(request):
    games = Game.objects.filter(trader=auth.get_user(request))
    all_games = []
    for g in games:
        buys = Transaction.objects.filter(game=g, transaction_type='B')
        sells = Transaction.objects.filter(game=g, transaction_type='S')
        buys_count = buys.count()
        sells_count = sells.count()

        sells_proceeds = 0
        for s in sells:
            sells_proceeds = sells_proceeds + (s.price * s.shares)

        buys_proceeds = 0
        for b in buys:
            buys_proceeds = buys_proceeds + (b.price * b.shares)

        commissions = (buys_count + sells_count) * 15

        game_details = {
            "cash": g.cash,
            "margin": g.margin,
            "stock": g.stock,
            "total_value": g.total_value,
            "net_income": g.net_income,
            "buys": buys_count,
            "buys_proceeds": buys_proceeds,
            "sells": sells_count,
            "sells_proceeds": sells_proceeds,
            "commissions": commissions
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