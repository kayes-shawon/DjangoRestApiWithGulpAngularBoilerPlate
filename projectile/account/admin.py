# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from reversion.admin import VersionAdmin
from .models import (
    Account
)
# Register your models here.
class AccountAdmin(VersionAdmin):
    list_display = ('name', 'id', 'organization', 'alias', 'status')
    list_filter = ('organization', 'status')
    search_fields = ('name', 'organization__name', 'alias')

admin.site.register(Account, AccountAdmin)