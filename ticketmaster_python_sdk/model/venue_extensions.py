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


class VenueExtensions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    All Venue's extensions
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def geolocation() -> typing.Type['GeolocationVenueExtensions']:
                return GeolocationVenueExtensions
            __annotations__ = {
                "geolocation": geolocation,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geolocation"]) -> 'GeolocationVenueExtensions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["geolocation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geolocation"]) -> typing.Union['GeolocationVenueExtensions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["geolocation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        geolocation: typing.Union['GeolocationVenueExtensions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VenueExtensions':
        return super().__new__(
            cls,
            *args,
            geolocation=geolocation,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.geolocation_venue_extensions import GeolocationVenueExtensions
