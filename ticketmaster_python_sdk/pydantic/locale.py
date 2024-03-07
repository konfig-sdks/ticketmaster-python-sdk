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
from pydantic import BaseModel, Field, RootModel

from ticketmaster_python_sdk.pydantic.locale_extension_keys import LocaleExtensionKeys
from ticketmaster_python_sdk.pydantic.locale_unicode_locale_attributes import LocaleUnicodeLocaleAttributes
from ticketmaster_python_sdk.pydantic.locale_unicode_locale_keys import LocaleUnicodeLocaleKeys

class Locale(BaseModel):
    country: typing.Optional[str] = Field(None, alias='country')

    display_country: typing.Optional[str] = Field(None, alias='displayCountry')

    display_language: typing.Optional[str] = Field(None, alias='displayLanguage')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    display_script: typing.Optional[str] = Field(None, alias='displayScript')

    display_variant: typing.Optional[str] = Field(None, alias='displayVariant')

    extension_keys: typing.Optional[LocaleExtensionKeys] = Field(None, alias='extensionKeys')

    iso3_country: typing.Optional[str] = Field(None, alias='iso3Country')

    iso3_language: typing.Optional[str] = Field(None, alias='iso3Language')

    language: typing.Optional[str] = Field(None, alias='language')

    script: typing.Optional[str] = Field(None, alias='script')

    unicode_locale_attributes: typing.Optional[LocaleUnicodeLocaleAttributes] = Field(None, alias='unicodeLocaleAttributes')

    unicode_locale_keys: typing.Optional[LocaleUnicodeLocaleKeys] = Field(None, alias='unicodeLocaleKeys')

    variant: typing.Optional[str] = Field(None, alias='variant')
    class Config:
        arbitrary_types_allowed = True
