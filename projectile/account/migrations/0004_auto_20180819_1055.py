# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-19 10:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180819_1055'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_account_created_by', to=settings.AUTH_USER_MODEL, verbose_name=b'created by'),
        ),
        migrations.AddField(
            model_name='account',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Organization', verbose_name=b'organization name'),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_account_updated_by', to=settings.AUTH_USER_MODEL, verbose_name=b'last updated by'),
        ),
    ]
