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


class PersonGender(Enum):
    MALE = 0
    FEMALE = 1
    TRANSSEXUAL = 2
    ANY = 3

    i18n = (
        _('Male'),
        _('Female'),
        _('Transsexual'),
        _('Any'),
    )


class Themes(Enum):
    LIGHT = 0
    DARK = 1

    i18n = (
        _('Light'),
        _('Dark'),
    )


class TextSize(Enum):
    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4

    i18n = (
        _('h1'),
        _('h2'),
        _('h3'),
        _('h4'),
    )


class OrganizationType(Enum):
    MOTHER = 0
    BRANCH = 1
    UNITE = 2
    PRIVATE_PRACTITIONERS = 3
    PHARMACY = 4

    i18n = (
        _('Mother'),
        _('Branch'),
        _('Unite'),
        _('Private Practitioners'),
        _('Pharmacy'),
    )


class PaginationType(Enum):
    DEFAULT = 1
    SCROLL = 2

    i18n = (
        _('Default'),
        _('Scroll'),
    )
