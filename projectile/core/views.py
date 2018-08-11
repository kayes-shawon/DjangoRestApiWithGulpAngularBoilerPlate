# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.models import 
from .enums import PersonGroupType
from django.db import models

# Create your views here.
class Person(AbstractBaseUser, PermissionsMixin, CreatedAtUpdatedAtBaseModel, UserThumbFieldMixin):

    """
    A custom User model

    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.

    A more descriptive tutorial can be found here
    http://www.caktusgroup.com/blog/2013/08/07/migrating-custom-user-model-django/
    """
    # Django's default fields
    email = models.EmailField(
        db_index=True,
        unique=False,
        null=True,
        default=None
    )
    phone = models.CharField(
        db_index=True,
        max_length=24,
        unique=False,
        null=True,
        default=None
    )
    first_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('''Whether this user should be treated as active. Unselect this instead of
         deleting accounts.''')
    )
    # Extended fields
    is_head_of_family = models.BooleanField(
        _('head of family'),
        default=False,
        help_text=_('''Whether this user should be treated as head of his family''')
    )
    country = models.CharField(
        max_length=2,
        choices=COUNTRIES,
        default='bd',
        db_index=True
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default='en'
    )
    economic_status = fields.SelectIntegerField(
        blueprint=EconomicGroup,
        default=EconomicGroup.POOR
    )
    nid = models.CharField(
        max_length=32,
        default=None,
        blank=True,
        null=True,
        verbose_name=_('NID No.'),
        help_text=_('National ID No. Example: YYYYXXXXXXXXXXXXX')
    )
    profile_image = TimestampImageField(
        upload_to='profiles/pic',
        blank=True,
        null=True
    )
    hero_image = TimestampImageField(
        upload_to='profiles/hero',
        blank=True,
        null=True
    )
    birth_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text=_('Birth ID No. Example: YYYYXXXXXXXXXXXXX')
    )
    permanent_address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    present_address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    dob = models.DateField(
        blank=True,
        null=True
    )
    person_group = fields.SelectIntegerField(
        blueprint=PersonGroupType,
        default=PersonGroupType.GUEST,
        db_index=True
    )
    balance = models.FloatField(
        default=0
    )
    opening_balance = models.FloatField(
        default=0
    )
    code = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    family_id = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    gender = fields.SelectIntegerField(
        blueprint=PersonGender,
        default=PersonGender.MALE
    )
    mothers_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    fathers_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    husbands_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    relatives_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    relatives_address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    relatives_contact_number = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    relatives_relation = fields.SelectIntegerField(
        blueprint=Relationship
    )
    family_relation = fields.SelectIntegerField(
        blueprint=FamilyRelationship,
        default=FamilyRelationship.OTHER,
        blank=True,
        null=True
    )
    patient_refered_by = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    designation = models.ForeignKey(
        EmployeeDesignation,
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_index=True
    )
    joining_date = models.DateField(
        blank=True,
        null=True
    )
    registration_number = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    degree = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )
    remarks = models.TextField(
        blank=True,
        null=True
    )
    medical_remarks = models.TextField(
        blank=True,
        null=True
    )
    theme = fields.SelectIntegerField(
        blueprint=Themes,
        default=Themes.LIGHT
    )

    # fields for supplier account
    company_name = models.CharField(
        max_length=100,
        blank=True
    )
    contact_person = models.CharField(
        max_length=100,
        blank=True
    )
    contact_person_number = models.CharField(
        max_length=100,
        blank=True
    )
    contact_person_address = models.CharField(
        max_length=100,
        blank=True
    )

    fingerprint_1 = models.TextField(blank=True, null=True)
    fingerprint_2 = models.TextField(blank=True, null=True)
    fingerprint_3 = models.TextField(blank=True, null=True)

    objects = PersonManager()
    organization = models.ForeignKey(
        Organization,
        models.DO_NOTHING,
        blank=True,
        null=True,
        default=None
    )
    is_positive = models.BooleanField(
        default=False
    )
    pagination_type = fields.SelectIntegerField(
        blueprint=PaginationType,
        default=PaginationType.DEFAULT
    )
    USERNAME_FIELD = 'id'
    date_picker = fields.SelectIntegerField(
        blueprint=DatePickerType,
        default=DatePickerType.DEFAULTDATEPICKER)

    # REQUIRED_FIELDS = (,)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __unicode__(self):
        name = u"{} {} - {}".format(
            self.first_name,
            self.last_name,
            self.phone
        )
        return name.strip()
