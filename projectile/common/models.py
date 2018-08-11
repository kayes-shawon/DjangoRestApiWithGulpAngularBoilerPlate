import uuid
from django.db import models
from enumerify import fields
from model_utils import Choices
from django.utils.translation import gettext as _
from .enums import Status
class EntityBaseModel(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    status = fields.SelectIntegerField(blueprint=Status, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        'core.Person',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('created by'),
        related_name="%(app_label)s_%(class)s_created_by"
    )

    updated_by = models.ForeignKey(
        'core.Person',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('last updated by'),
        related_name="%(app_label)s_%(class)s_updated_by"
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class EntityBaseWithOrganizationModel(models.Model):
    organization = models.ForeignKey(
            'core.Organization',
            models.DO_NOTHING,
            blank=False,
            null=False,
            db_index=True,
            verbose_name=('organization name')
        )

    class Meta:
        abstract = True,
        index_together = ["organization", "status"],
        ordering = ('-created_at',)


class NameDescriptionBaseModel(EntityBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return self.get_name()


class NameDescriptionWithOrganizationBaseModel(NameDescriptionBaseModel):
    organization = models.ForeignKey(
        'core.Organization',
        models.DO_NOTHING,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=('organization name')
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return self.get_name()
