# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-19 10:55
from __future__ import unicode_literals

import common.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumerify.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'Active'), (2, b'Inactive'), (3, b'Draft')], db_index=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(db_index=True, default=None, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(db_index=True, default=None, max_length=24, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this user should be treated as active. Unselect this instead of\n         deleting accounts.', verbose_name='active')),
                ('nid', models.CharField(blank=True, default=None, help_text='National ID No. Example: YYYYXXXXXXXXXXXXX', max_length=32, null=True, verbose_name='NID No.')),
                ('profile_image', common.fields.TimestampImageField(blank=True, null=True, upload_to='profiles/pic')),
                ('hero_image', common.fields.TimestampImageField(blank=True, null=True, upload_to='profiles/hero')),
                ('birth_id', models.CharField(blank=True, help_text='Birth ID No. Example: YYYYXXXXXXXXXXXXX', max_length=32, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=255, null=True)),
                ('present_address', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('person_group', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'Guest'), (2, b'Manager'), (3, b'Stack Holder'), (4, b'Housekeeping'), (5, b'Board of Director'), (6, b'System Admin'), (7, b'Other')], db_index=True, default=1)),
                ('balance', models.FloatField(default=0)),
                ('opening_balance', models.FloatField(default=0)),
                ('code', models.CharField(blank=True, max_length=16, null=True)),
                ('family_id', models.CharField(blank=True, max_length=16, null=True)),
                ('gender', enumerify.fields.SelectIntegerField(choices=[(0, b'Male'), (1, b'Female'), (2, b'Transsexual'), (3, b'Any')], db_index=True, default=0)),
                ('mothers_name', models.CharField(blank=True, max_length=64, null=True)),
                ('fathers_name', models.CharField(blank=True, max_length=64, null=True)),
                ('husbands_name', models.CharField(blank=True, max_length=64, null=True)),
                ('relatives_name', models.CharField(blank=True, max_length=64, null=True)),
                ('relatives_address', models.CharField(blank=True, max_length=255, null=True)),
                ('relatives_contact_number', models.CharField(blank=True, max_length=16, null=True)),
                ('patient_refered_by', models.CharField(blank=True, max_length=255, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=64, null=True)),
                ('degree', models.CharField(blank=True, max_length=256, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('medical_remarks', models.TextField(blank=True, null=True)),
                ('theme', enumerify.fields.SelectIntegerField(choices=[(0, b'Light'), (1, b'Dark')], db_index=True, default=0)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('contact_person', models.CharField(blank=True, max_length=100)),
                ('contact_person_number', models.CharField(blank=True, max_length=100)),
                ('contact_person_address', models.CharField(blank=True, max_length=100)),
                ('is_positive', models.BooleanField(default=False)),
                ('pagination_type', enumerify.fields.SelectIntegerField(choices=[(1, b'Default'), (2, b'Scroll')], db_index=True, default=1)),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_person_created_by', to=settings.AUTH_USER_MODEL, verbose_name=b'created by')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'Active'), (2, b'Inactive'), (3, b'Draft')], db_index=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_department_created_by', to=settings.AUTH_USER_MODEL, verbose_name=b'created by')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EmployeeDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'Active'), (2, b'Inactive'), (3, b'Draft')], db_index=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_employeedesignation_created_by', to=settings.AUTH_USER_MODEL, verbose_name=b'created by')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Department')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'Active'), (2, b'Inactive'), (3, b'Draft')], db_index=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('slogan', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=255)),
                ('logo', common.fields.TimestampImageField(blank=True, null=True, upload_to='organization/logo')),
                ('primary_mobile', models.CharField(max_length=20)),
                ('other_contact', models.CharField(blank=True, max_length=64, null=True)),
                ('contact_person', models.CharField(max_length=64)),
                ('contact_person_designation', models.CharField(max_length=64)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('website', models.CharField(blank=True, max_length=64, null=True)),
                ('domain', models.CharField(blank=True, max_length=128, null=True)),
                ('name_font_size', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'h1'), (2, b'h2'), (3, b'h3'), (4, b'h4')], db_index=True, default=2)),
                ('slogan_font_size', enumerify.fields.SelectIntegerField(choices=[(0, b'-'), (1, b'h1'), (2, b'h2'), (3, b'h3'), (4, b'h4')], db_index=True, default=3)),
                ('print_slogan', models.BooleanField(default=False)),
                ('print_address', models.BooleanField(default=True)),
                ('print_logo', models.BooleanField(default=True)),
                ('print_header', models.BooleanField(default=True)),
                ('print_patient_code', models.BooleanField(default=True)),
                ('print_patient_group', models.BooleanField(default=True)),
                ('type', enumerify.fields.SelectIntegerField(choices=[(0, b'Mother'), (1, b'Branch'), (2, b'Unite'), (3, b'Private Practitioners'), (4, b'Pharmacy')], db_index=True, default=0)),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_organization_created_by', to=settings.AUTH_USER_MODEL, verbose_name=b'created by')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_organization_updated_by', to=settings.AUTH_USER_MODEL, verbose_name=b'last updated by')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='employeedesignation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Organization', verbose_name=b'organization name'),
        ),
        migrations.AddField(
            model_name='employeedesignation',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_employeedesignation_updated_by', to=settings.AUTH_USER_MODEL, verbose_name=b'last updated by'),
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Organization', verbose_name=b'organization name'),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_department_updated_by', to=settings.AUTH_USER_MODEL, verbose_name=b'last updated by'),
        ),
        migrations.AddField(
            model_name='person',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.EmployeeDesignation'),
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Organization'),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_person_updated_by', to=settings.AUTH_USER_MODEL, verbose_name=b'last updated by'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]