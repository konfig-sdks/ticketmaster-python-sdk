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


class Attributions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Attributions
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def description() -> typing.Type['Attribution']:
                return Attribution
        
            @staticmethod
            def descriptions() -> typing.Type['AttributionsDescriptions']:
                return AttributionsDescriptions
            __annotations__ = {
                "description": description,
                "descriptions": descriptions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'Attribution': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptions"]) -> 'AttributionsDescriptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "descriptions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['Attribution', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptions"]) -> typing.Union['AttributionsDescriptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "descriptions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union['Attribution', schemas.Unset] = schemas.unset,
        descriptions: typing.Union['AttributionsDescriptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Attributions':
        return super().__new__(
            cls,
            *args,
            description=description,
            descriptions=descriptions,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.attribution import Attribution
from ticketmaster_python_sdk.model.attributions_descriptions import AttributionsDescriptions
