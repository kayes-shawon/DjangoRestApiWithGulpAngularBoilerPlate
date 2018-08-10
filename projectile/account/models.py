# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.models import NameDescriptionWithOrganizationBaseModel
# Create your models here.

class Account(NameDescriptionWithOrganizationBaseModel):
    date = models.DateTimeField()
    head = models.CharField(max_length=255, blank=False, unique=True)
    amount = models.FloatField()
    method = models.CharField(max_length=255, blank= True)
    

    
    
    