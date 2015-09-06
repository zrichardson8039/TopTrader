from rest_framework import serializers
from apps.contests.models import Record, Game, Transaction


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
