# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TransactionHead(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)