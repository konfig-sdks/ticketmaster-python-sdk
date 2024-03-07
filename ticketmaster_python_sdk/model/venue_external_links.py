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


class VenueExternalLinks(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    List of external links
    """


    class MetaOapg:
        
        
        class additional_properties(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                @staticmethod
                def items() -> typing.Type['ExternalLink']:
                    return ExternalLink
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple['ExternalLink'], typing.List['ExternalLink']],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> 'ExternalLink':
                return super().__getitem__(i)
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
    ) -> 'VenueExternalLinks':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from ticketmaster_python_sdk.model.external_link import ExternalLink
