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

from ticketmaster_python_sdk.type.local_time import LocalTime

class RequiredEndDates(TypedDict):
    pass

class OptionalEndDates(TypedDict, total=False):
    # Boolean flag to indicate whether or not the end date is approximated
    approximate: bool

    # The event end date time
    dateTime: datetime

    # The event end date in local date
    localDate: date

    localTime: LocalTime

    # Boolean flag to indicate whether or not the event end time has no specific time
    noSpecificTime: bool

class EndDates(RequiredEndDates, OptionalEndDates):
    pass
