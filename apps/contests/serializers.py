from rest_framework import serializers
from apps.contests.models import Game, Transaction


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
