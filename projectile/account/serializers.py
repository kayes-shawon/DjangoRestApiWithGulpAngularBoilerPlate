from rest_framework import serializers
from .models import TransactionHead 
class TransactionHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHead
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )