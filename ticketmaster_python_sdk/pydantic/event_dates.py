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
from pydantic import BaseModel, Field, RootModel

from ticketmaster_python_sdk.pydantic.access_dates import AccessDates
from ticketmaster_python_sdk.pydantic.end_dates import EndDates
from ticketmaster_python_sdk.pydantic.event_status import EventStatus
from ticketmaster_python_sdk.pydantic.start_dates import StartDates

class EventDates(BaseModel):
    access: typing.Optional[AccessDates] = Field(None, alias='access')

    end: typing.Optional[EndDates] = Field(None, alias='end')

    # Flag indicating if date spans of multiple days
    span_multiple_days: typing.Optional[bool] = Field(None, alias='spanMultipleDays')

    start: typing.Optional[StartDates] = Field(None, alias='start')

    status: typing.Optional[EventStatus] = Field(None, alias='status')

    # Event's timezone
    timezone: typing.Optional[str] = Field(None, alias='timezone')
    class Config:
        arbitrary_types_allowed = True
