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


class RequiredPriceRange(TypedDict):
    pass

class OptionalPriceRange(TypedDict, total=False):
    # Currency
    currency: str

    # Maximum price
    max: typing.Union[int, float]

    # Minimum price
    min: typing.Union[int, float]

    # Type of price
    type: str

class PriceRange(RequiredPriceRange, OptionalPriceRange):
    pass
