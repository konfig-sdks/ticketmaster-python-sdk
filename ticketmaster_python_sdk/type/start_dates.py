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

class RequiredStartDates(TypedDict):
    pass

class OptionalStartDates(TypedDict, total=False):
    # Boolean flag to indicate whether or not the start date is TBA
    dateTBA: bool

    # Boolean flag to indicate whether or not the start date is TBD
    dateTBD: bool

    # The event start datetime
    dateTime: datetime

    # The event start date in local date
    localDate: date

    localTime: LocalTime

    # Boolean flag to indicate whether or not the event start time has no specific time
    noSpecificTime: bool

    # Boolean flag to indicate whether or not the start time is TBA
    timeTBA: bool

class StartDates(RequiredStartDates, OptionalStartDates):
    pass
