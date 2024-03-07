# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ticketmaster_python_sdk import schemas  # noqa: F401


class Locale(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            country = schemas.StrSchema
            displayCountry = schemas.StrSchema
            displayLanguage = schemas.StrSchema
            displayName = schemas.StrSchema
            displayScript = schemas.StrSchema
            displayVariant = schemas.StrSchema
        
            @staticmethod
            def extensionKeys() -> typing.Type['LocaleExtensionKeys']:
                return LocaleExtensionKeys
            iso3Country = schemas.StrSchema
            iso3Language = schemas.StrSchema
            language = schemas.StrSchema
            script = schemas.StrSchema
        
            @staticmethod
            def unicodeLocaleAttributes() -> typing.Type['LocaleUnicodeLocaleAttributes']:
                return LocaleUnicodeLocaleAttributes
        
            @staticmethod
            def unicodeLocaleKeys() -> typing.Type['LocaleUnicodeLocaleKeys']:
                return LocaleUnicodeLocaleKeys
            variant = schemas.StrSchema
            __annotations__ = {
                "country": country,
                "displayCountry": displayCountry,
                "displayLanguage": displayLanguage,
                "displayName": displayName,
                "displayScript": displayScript,
                "displayVariant": displayVariant,
                "extensionKeys": extensionKeys,
                "iso3Country": iso3Country,
                "iso3Language": iso3Language,
                "language": language,
                "script": script,
                "unicodeLocaleAttributes": unicodeLocaleAttributes,
                "unicodeLocaleKeys": unicodeLocaleKeys,
                "variant": variant,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayCountry"]) -> MetaOapg.properties.displayCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayLanguage"]) -> MetaOapg.properties.displayLanguage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayScript"]) -> MetaOapg.properties.displayScript: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayVariant"]) -> MetaOapg.properties.displayVariant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extensionKeys"]) -> 'LocaleExtensionKeys': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso3Country"]) -> MetaOapg.properties.iso3Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso3Language"]) -> MetaOapg.properties.iso3Language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unicodeLocaleAttributes"]) -> 'LocaleUnicodeLocaleAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unicodeLocaleKeys"]) -> 'LocaleUnicodeLocaleKeys': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variant"]) -> MetaOapg.properties.variant: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country", "displayCountry", "displayLanguage", "displayName", "displayScript", "displayVariant", "extensionKeys", "iso3Country", "iso3Language", "language", "script", "unicodeLocaleAttributes", "unicodeLocaleKeys", "variant", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayCountry"]) -> typing.Union[MetaOapg.properties.displayCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayLanguage"]) -> typing.Union[MetaOapg.properties.displayLanguage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayScript"]) -> typing.Union[MetaOapg.properties.displayScript, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayVariant"]) -> typing.Union[MetaOapg.properties.displayVariant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extensionKeys"]) -> typing.Union['LocaleExtensionKeys', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso3Country"]) -> typing.Union[MetaOapg.properties.iso3Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso3Language"]) -> typing.Union[MetaOapg.properties.iso3Language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> typing.Union[MetaOapg.properties.script, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unicodeLocaleAttributes"]) -> typing.Union['LocaleUnicodeLocaleAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unicodeLocaleKeys"]) -> typing.Union['LocaleUnicodeLocaleKeys', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variant"]) -> typing.Union[MetaOapg.properties.variant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country", "displayCountry", "displayLanguage", "displayName", "displayScript", "displayVariant", "extensionKeys", "iso3Country", "iso3Language", "language", "script", "unicodeLocaleAttributes", "unicodeLocaleKeys", "variant", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        displayCountry: typing.Union[MetaOapg.properties.displayCountry, str, schemas.Unset] = schemas.unset,
        displayLanguage: typing.Union[MetaOapg.properties.displayLanguage, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        displayScript: typing.Union[MetaOapg.properties.displayScript, str, schemas.Unset] = schemas.unset,
        displayVariant: typing.Union[MetaOapg.properties.displayVariant, str, schemas.Unset] = schemas.unset,
        extensionKeys: typing.Union['LocaleExtensionKeys', schemas.Unset] = schemas.unset,
        iso3Country: typing.Union[MetaOapg.properties.iso3Country, str, schemas.Unset] = schemas.unset,
        iso3Language: typing.Union[MetaOapg.properties.iso3Language, str, schemas.Unset] = schemas.unset,
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        unicodeLocaleAttributes: typing.Union['LocaleUnicodeLocaleAttributes', schemas.Unset] = schemas.unset,
        unicodeLocaleKeys: typing.Union['LocaleUnicodeLocaleKeys', schemas.Unset] = schemas.unset,
        variant: typing.Union[MetaOapg.properties.variant, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Locale':
        return super().__new__(
            cls,
            *args,
            country=country,
            displayCountry=displayCountry,
            displayLanguage=displayLanguage,
            displayName=displayName,
            displayScript=displayScript,
            displayVariant=displayVariant,
            extensionKeys=extensionKeys,
            iso3Country=iso3Country,
            iso3Language=iso3Language,
            language=language,
            script=script,
            unicodeLocaleAttributes=unicodeLocaleAttributes,
            unicodeLocaleKeys=unicodeLocaleKeys,
            variant=variant,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.locale_extension_keys import LocaleExtensionKeys
from ticketmaster_python_sdk.model.locale_unicode_locale_attributes import LocaleUnicodeLocaleAttributes
from ticketmaster_python_sdk.model.locale_unicode_locale_keys import LocaleUnicodeLocaleKeys
