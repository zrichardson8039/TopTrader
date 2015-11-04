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
    title = "Profile"
    context = {
        'title': title
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