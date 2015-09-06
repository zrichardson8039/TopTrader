from rest_framework import viewsets
from apps.contests.models import Record, Game, Transaction
from apps.contests.serializers import RecordSerializer, GameSerializer, TransactionSerializer
from apps.common.permissions import ReadOnly


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [ReadOnly, ]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [ReadOnly, ]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ReadOnly, ]