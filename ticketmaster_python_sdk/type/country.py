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


class RequiredCountry(TypedDict):
    pass

class OptionalCountry(TypedDict, total=False):
    # Country code (ISO 3166)
    countryCode: str

    # Name of the entity
    name: str

class Country(RequiredCountry, OptionalCountry):
    pass
