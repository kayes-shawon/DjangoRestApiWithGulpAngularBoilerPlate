# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.models import (
    EntityBaseModel,
    NameDescriptionBaseModel,
    NameDescriptionWithOrganizationBaseModel,
)
from common.fields import TimestampImageField
from common.enums import Status
from core.enums import (
    PersonGroupType,
    PersonGender,
    Themes,
    TextSize,
    OrganizationType,
    PaginationType
)
from enumerify import fields
from django.utils.translation import ugettext_lazy as _
from .managers import PersonManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class Organization(NameDescriptionBaseModel):
    slogan = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    logo = TimestampImageField(
        upload_to='organization/logo', blank=True, null=True)
    primary_mobile = models.CharField(max_length=20)
    other_contact = models.CharField(max_length=64, blank=True, null=True)
    contact_person = models.CharField(max_length=64)
    contact_person_designation = models.CharField(max_length=64)
    email = models.CharField(max_length=64, blank=True, null=True)
    website = models.CharField(max_length=64, blank=True, null=True)
    domain = models.CharField(max_length=128, blank=True, null=True)
    mother = models.ForeignKey('self', blank=True, null=True)
    name_font_size = fields.SelectIntegerField(
        blueprint=TextSize, default=TextSize.H2)
    slogan_font_size = fields.SelectIntegerField(
        blueprint=TextSize, default=TextSize.H3)
    print_slogan = models.BooleanField(default=False)
    print_address = models.BooleanField(default=True)
    print_logo = models.BooleanField(default=True)
    print_header = models.BooleanField(default=True)
    print_patient_code = models.BooleanField(default=True)
    print_patient_group = models.BooleanField(default=True)

    type = fields.SelectIntegerField(
        blueprint=OrganizationType, default=OrganizationType.MOTHER)

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.id, self.name)

    def get_organization_by_name(self, organization_name):
        try:
            return Organization.objects.get(
                name=organization_name,
                status=Status.ACTIVE
            )
        except Organization.DoesNotExist:
            return None

    class Meta:
        ordering = ('name',)

    def get_all_organizations(self):
        return Organization.objects.all()

    def get_active_organizations(self):
        return Organization.objects.filter(status=Status.ACTIVE)

    def get_filtered_organizations(self, filter):
        return Organization.objects.filter(**filter)


class Person(AbstractBaseUser, PermissionsMixin, EntityBaseModel):

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
        unique=True,
        null=True,
        default=None
    )
    phone = models.CharField(
        db_index=True,
        max_length=24,
        unique=True,
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
    patient_refered_by = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    designation = models.ForeignKey(
        'EmployeeDesignation',
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

    def get_full_name(self):
        """ Returns the full name """
        name = u"{} {} - {}".format(self.first_name,
                                    self.last_name, self.phone)
        return name.strip()

    def get_short_name(self):
        return u"{}".format(self.phone)


class Department(NameDescriptionWithOrganizationBaseModel):

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.get_name()


class EmployeeDesignation(NameDescriptionWithOrganizationBaseModel):
    department = models.ForeignKey(
        Department, models.DO_NOTHING,
        db_index=True
    )

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {} - {}".format(self.id, self.department, self.name)
