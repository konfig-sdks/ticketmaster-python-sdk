# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from ticketmaster_python_sdk.type.locale_extension_keys import LocaleExtensionKeys
from ticketmaster_python_sdk.type.locale_unicode_locale_attributes import LocaleUnicodeLocaleAttributes
from ticketmaster_python_sdk.type.locale_unicode_locale_keys import LocaleUnicodeLocaleKeys

class RequiredLocale(TypedDict):
    pass

class OptionalLocale(TypedDict, total=False):
    country: str

    displayCountry: str

    displayLanguage: str

    displayName: str

    displayScript: str

    displayVariant: str

    extensionKeys: LocaleExtensionKeys

    iso3Country: str

    iso3Language: str

    language: str

    script: str

    unicodeLocaleAttributes: LocaleUnicodeLocaleAttributes

    unicodeLocaleKeys: LocaleUnicodeLocaleKeys

    variant: str

class Locale(RequiredLocale, OptionalLocale):
    pass
