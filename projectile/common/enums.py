from django.utils.translation import gettext as _
from enumerify.enum import Enum


class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
    DRAFT = 3

    i18n = (
        _('Active'),
        _('Inactive'),
        _('Draft'),
    )
