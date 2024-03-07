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

from ticketmaster_python_sdk.pydantic.local_time import LocalTime

class StartDates(BaseModel):
    # Boolean flag to indicate whether or not the start date is TBA
    date_t_b_a: typing.Optional[bool] = Field(None, alias='dateTBA')

    # Boolean flag to indicate whether or not the start date is TBD
    date_t_b_d: typing.Optional[bool] = Field(None, alias='dateTBD')

    # The event start datetime
    date_time: typing.Optional[datetime] = Field(None, alias='dateTime')

    # The event start date in local date
    local_date: typing.Optional[date] = Field(None, alias='localDate')

    local_time: typing.Optional[LocalTime] = Field(None, alias='localTime')

    # Boolean flag to indicate whether or not the event start time has no specific time
    no_specific_time: typing.Optional[bool] = Field(None, alias='noSpecificTime')

    # Boolean flag to indicate whether or not the start time is TBA
    time_t_b_a: typing.Optional[bool] = Field(None, alias='timeTBA')
    class Config:
        arbitrary_types_allowed = True
