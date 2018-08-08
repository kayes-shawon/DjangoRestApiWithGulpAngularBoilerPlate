import uuid
from django.db import models
from model_utils import Choices

class EntityBaseModel(models.Model):
    STATUSES = Choices(
        (0, 'active', _('active')),
        (1, 'inactive', _('inactive'))   )


    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
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