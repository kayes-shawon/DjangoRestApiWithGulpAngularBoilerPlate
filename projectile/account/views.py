# -*- coding: utf-8 -*-
from rest_framework import generics
from .models import Account 
from .serializers import AccountSerializer

from django.shortcuts import render

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
