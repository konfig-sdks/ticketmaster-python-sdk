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

from ticketmaster_python_sdk.pydantic.chronology import Chronology
from ticketmaster_python_sdk.pydantic.date_time_field import DateTimeField
from ticketmaster_python_sdk.pydantic.date_time_field_type import DateTimeFieldType
from ticketmaster_python_sdk.pydantic.local_time_values import LocalTimeValues

class LocalTime(BaseModel):
    chronology: typing.Optional[Chronology] = Field(None, alias='chronology')

    field_types: typing.Optional[typing.List[DateTimeFieldType]] = Field(None, alias='fieldTypes')

    fields: typing.Optional[typing.List[DateTimeField]] = Field(None, alias='fields')

    hour_of_day: typing.Optional[int] = Field(None, alias='hourOfDay')

    millis_of_day: typing.Optional[int] = Field(None, alias='millisOfDay')

    millis_of_second: typing.Optional[int] = Field(None, alias='millisOfSecond')

    minute_of_hour: typing.Optional[int] = Field(None, alias='minuteOfHour')

    second_of_minute: typing.Optional[int] = Field(None, alias='secondOfMinute')

    values: typing.Optional[LocalTimeValues] = Field(None, alias='values')
    class Config:
        arbitrary_types_allowed = True
