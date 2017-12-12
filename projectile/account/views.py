# -*- coding: utf-8 -*-
from rest_framework import generics
from .models import TransactionHead 
from .serializers import TransactionHeadSerializer

from django.shortcuts import render

# Create your views here.
class TransactionHeadList(generics.ListCreateAPIView):
    queryset = TransactionHead.objects.all()
    serializer_class = TransactionHeadSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

