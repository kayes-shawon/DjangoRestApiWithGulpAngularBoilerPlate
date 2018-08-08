# -*- coding: utf-8 -*-
from rest_framework import generics
from .models import Transaction 
from .serializers import TransactionSerializer

from django.shortcuts import render

# Create your views here.
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
