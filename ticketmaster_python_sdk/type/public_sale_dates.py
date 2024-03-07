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


class RequiredPublicSaleDates(TypedDict):
    pass

class OptionalPublicSaleDates(TypedDict, total=False):
    # Public sale's end dates. The date and time when the public sale will end
    endDateTime: datetime

    # Public sale's start dates. The date and time when the public sale will start
    startDateTime: datetime

    # True if the public sale's date is to be determined
    startTBD: bool

class PublicSaleDates(RequiredPublicSaleDates, OptionalPublicSaleDates):
    pass
