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

from ticketmaster_python_sdk.type.chronology import Chronology
from ticketmaster_python_sdk.type.date_time_field import DateTimeField
from ticketmaster_python_sdk.type.date_time_field_type import DateTimeFieldType
from ticketmaster_python_sdk.type.local_time_values import LocalTimeValues

class RequiredLocalTime(TypedDict):
    pass

class OptionalLocalTime(TypedDict, total=False):
    chronology: Chronology

    fieldTypes: typing.List[DateTimeFieldType]

    fields: typing.List[DateTimeField]

    hourOfDay: int

    millisOfDay: int

    millisOfSecond: int

    minuteOfHour: int

    secondOfMinute: int

    values: LocalTimeValues

class LocalTime(RequiredLocalTime, OptionalLocalTime):
    pass
