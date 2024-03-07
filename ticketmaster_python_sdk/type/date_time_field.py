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

from ticketmaster_python_sdk.type.date_time_field_type import DateTimeFieldType
from ticketmaster_python_sdk.type.duration_field import DurationField

class RequiredDateTimeField(TypedDict):
    pass

class OptionalDateTimeField(TypedDict, total=False):
    durationField: DurationField

    leapDurationField: DurationField

    lenient: bool

    maximumValue: int

    minimumValue: int

    name: str

    rangeDurationField: DurationField

    supported: bool

    type: DateTimeFieldType

class DateTimeField(RequiredDateTimeField, OptionalDateTimeField):
    pass
