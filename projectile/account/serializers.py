from rest_framework import serializers
from .models import Transaction 
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id',
            'date',
            'head',
            'amount',
            'method',
        )
        read_only_fields = (
            'id',
        )