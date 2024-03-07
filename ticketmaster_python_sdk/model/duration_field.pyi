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


class DurationField(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            precise = schemas.BoolSchema
            supported = schemas.BoolSchema
        
            @staticmethod
            def type() -> typing.Type['DurationFieldType']:
                return DurationFieldType
            unitMillis = schemas.Int64Schema
            __annotations__ = {
                "name": name,
                "precise": precise,
                "supported": supported,
                "type": type,
                "unitMillis": unitMillis,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["precise"]) -> MetaOapg.properties.precise: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supported"]) -> MetaOapg.properties.supported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'DurationFieldType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unitMillis"]) -> MetaOapg.properties.unitMillis: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "precise", "supported", "type", "unitMillis", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["precise"]) -> typing.Union[MetaOapg.properties.precise, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supported"]) -> typing.Union[MetaOapg.properties.supported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['DurationFieldType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unitMillis"]) -> typing.Union[MetaOapg.properties.unitMillis, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "precise", "supported", "type", "unitMillis", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        precise: typing.Union[MetaOapg.properties.precise, bool, schemas.Unset] = schemas.unset,
        supported: typing.Union[MetaOapg.properties.supported, bool, schemas.Unset] = schemas.unset,
        type: typing.Union['DurationFieldType', schemas.Unset] = schemas.unset,
        unitMillis: typing.Union[MetaOapg.properties.unitMillis, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DurationField':
        return super().__new__(
            cls,
            *args,
            name=name,
            precise=precise,
            supported=supported,
            type=type,
            unitMillis=unitMillis,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.duration_field_type import DurationFieldType