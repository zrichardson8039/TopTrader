from django.shortcuts import render
from rest_framework import viewsets
from apps.contests.models import Game, Transaction
from apps.contests.serializers import GameSerializer, TransactionSerializer
from apps.common.permissions import ReadOnly


def play(request):
    title = "Play"
    context = {
        'title': title
    }

    return render(request, "play.html", context)


def profile(request):
    games = Game.objects.filter(trader=request.user)
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