# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import (
    Organization,
    Person,
    Department,
    EmployeeDesignation,
)
# Register your models here.


class OrganizationAdmin(VersionAdmin):
    list_display = (
        'name', 'type', 'slogan', 'address', 'primary_mobile',
        'other_contact', 'contact_person', 'contact_person_designation',
        'email', 'website', 'domain', 'status',
    )

    list_filter = ('type', 'status',)
    search_fields = ('name', 'slogan', 'primary_mobile', 'contact_person',
                     'email', 'website', 'domain',)


admin.site.register(Organization, OrganizationAdmin)


class PersonAdmin(VersionAdmin):
    list_display = (
        'phone', 'email', 'first_name', 'last_name',  'nid',
        '_person', 'dob', 'code', 'status', 'organization'
    )

    def _person(self, obj):
        if obj.company_name:
            return u'{} -{}'.format(obj.company_name, obj.contact_person_number)
        return obj.get_full_name()

    list_filter = ('status', 'organization', 'gender')
    search_fields = ('first_name', 'last_name', 'alias', 'id', 'phone')


admin.site.register(Person, PersonAdmin)
