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


class Attribution(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Attribution
    """


    class MetaOapg:
        
        class properties:
            licenceName = schemas.StrSchema
            licenceUrl = schemas.StrSchema
            sourceName = schemas.StrSchema
            sourceUrl = schemas.StrSchema
            __annotations__ = {
                "licenceName": licenceName,
                "licenceUrl": licenceUrl,
                "sourceName": sourceName,
                "sourceUrl": sourceUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenceName"]) -> MetaOapg.properties.licenceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenceUrl"]) -> MetaOapg.properties.licenceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceName"]) -> MetaOapg.properties.sourceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["licenceName", "licenceUrl", "sourceName", "sourceUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenceName"]) -> typing.Union[MetaOapg.properties.licenceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenceUrl"]) -> typing.Union[MetaOapg.properties.licenceUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceName"]) -> typing.Union[MetaOapg.properties.sourceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceUrl"]) -> typing.Union[MetaOapg.properties.sourceUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["licenceName", "licenceUrl", "sourceName", "sourceUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        licenceName: typing.Union[MetaOapg.properties.licenceName, str, schemas.Unset] = schemas.unset,
        licenceUrl: typing.Union[MetaOapg.properties.licenceUrl, str, schemas.Unset] = schemas.unset,
        sourceName: typing.Union[MetaOapg.properties.sourceName, str, schemas.Unset] = schemas.unset,
        sourceUrl: typing.Union[MetaOapg.properties.sourceUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Attribution':
        return super().__new__(
            cls,
            *args,
            licenceName=licenceName,
            licenceUrl=licenceUrl,
            sourceName=sourceName,
            sourceUrl=sourceUrl,
            _configuration=_configuration,
            **kwargs,
        )
