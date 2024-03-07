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


class RequiredPresale(TypedDict):
    pass

class OptionalPresale(TypedDict, total=False):
    # Description of the presame
    description: str

    # Presale's end dates. The date and time when the presale will end
    endDateTime: datetime

    # Name of the presale
    name: str

    # Presale's start dates. The date and time when the presale will start
    startDateTime: datetime

    # Presale link URL
    url: str

class Presale(RequiredPresale, OptionalPresale):
    pass
