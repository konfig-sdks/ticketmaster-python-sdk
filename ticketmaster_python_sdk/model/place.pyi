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


class Place(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Place
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def area() -> typing.Type['Area']:
                return Area
        
            @staticmethod
            def city() -> typing.Type['City']:
                return City
        
            @staticmethod
            def country() -> typing.Type['Country']:
                return Country
        
            @staticmethod
            def location() -> typing.Type['Location']:
                return Location
            name = schemas.StrSchema
            postalCode = schemas.StrSchema
        
            @staticmethod
            def state() -> typing.Type['State']:
                return State
            __annotations__ = {
                "address": address,
                "area": area,
                "city": city,
                "country": country,
                "location": location,
                "name": name,
                "postalCode": postalCode,
                "state": state,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> 'Area': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> 'City': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'Country': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'Location': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'State': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "area", "city", "country", "location", "name", "postalCode", "state", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> typing.Union['Area', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union['City', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union['Country', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union['Location', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union['State', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "area", "city", "country", "location", "name", "postalCode", "state", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union['Address', schemas.Unset] = schemas.unset,
        area: typing.Union['Area', schemas.Unset] = schemas.unset,
        city: typing.Union['City', schemas.Unset] = schemas.unset,
        country: typing.Union['Country', schemas.Unset] = schemas.unset,
        location: typing.Union['Location', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        state: typing.Union['State', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Place':
        return super().__new__(
            cls,
            *args,
            address=address,
            area=area,
            city=city,
            country=country,
            location=location,
            name=name,
            postalCode=postalCode,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.address import Address
from ticketmaster_python_sdk.model.area import Area
from ticketmaster_python_sdk.model.city import City
from ticketmaster_python_sdk.model.country import Country
from ticketmaster_python_sdk.model.location import Location
from ticketmaster_python_sdk.model.state import State
