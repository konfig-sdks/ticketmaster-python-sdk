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


class RequiredAccessDates(TypedDict):
    pass

class OptionalAccessDates(TypedDict, total=False):
    # Boolean flag to indicate whether or not the access end date is approximated
    endApproximate: bool

    # Event's end access time
    endDateTime: datetime

    # Boolean flag to indicate whether or not the access start date is approximated
    startApproximate: bool

    # Event's start access time
    startDateTime: datetime

class AccessDates(RequiredAccessDates, OptionalAccessDates):
    pass
