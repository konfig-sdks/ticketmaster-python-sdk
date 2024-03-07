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

from ticketmaster_python_sdk.type.access_dates import AccessDates
from ticketmaster_python_sdk.type.end_dates import EndDates
from ticketmaster_python_sdk.type.event_status import EventStatus
from ticketmaster_python_sdk.type.start_dates import StartDates

class RequiredEventDates(TypedDict):
    pass

class OptionalEventDates(TypedDict, total=False):
    access: AccessDates

    end: EndDates

    # Flag indicating if date spans of multiple days
    spanMultipleDays: bool

    start: StartDates

    status: EventStatus

    # Event's timezone
    timezone: str

class EventDates(RequiredEventDates, OptionalEventDates):
    pass
