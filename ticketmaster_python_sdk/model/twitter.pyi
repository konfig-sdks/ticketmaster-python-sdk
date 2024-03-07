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


class Twitter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Twitter data
    """


    class MetaOapg:
        
        class properties:
            
            
            class handle(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def A_TWITTER_HANDLE(cls):
                    return cls("@a Twitter handle")
        
            @staticmethod
            def hashtags() -> typing.Type['TwitterHashtags']:
                return TwitterHashtags
            __annotations__ = {
                "handle": handle,
                "hashtags": hashtags,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashtags"]) -> 'TwitterHashtags': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["handle", "hashtags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> typing.Union[MetaOapg.properties.handle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashtags"]) -> typing.Union['TwitterHashtags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["handle", "hashtags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        handle: typing.Union[MetaOapg.properties.handle, str, schemas.Unset] = schemas.unset,
        hashtags: typing.Union['TwitterHashtags', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Twitter':
        return super().__new__(
            cls,
            *args,
            handle=handle,
            hashtags=hashtags,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.twitter_hashtags import TwitterHashtags