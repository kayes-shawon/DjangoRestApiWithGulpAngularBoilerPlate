from rest_framework import serializers
from .models import Account 
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'date',
            'head',
            'amount',
            'method',
        )
        read_only_fields = (
            'id',
        )