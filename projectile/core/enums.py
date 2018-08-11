from django.utils.translation import gettext as _
from enumerify.enum import Enum

class PersonGroupType(Enum):
    GUEST = 1
    MANAGER = 2
    STACK_HOLDER = 3
    HOUSEKEEPING = 4
    BOARD_OF_DIRECTOR = 5
    SYSTEM_ADMIN = 6
    OTHER = 7

    i18n = (
        _('Guest'),
        _('Manager'),
        _('Stack Holder'),
        _('Housekeeping'),
        _('Board of Director'),
        _('System Admin'),
        _('Other'),
    )
