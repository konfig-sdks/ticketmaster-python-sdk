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

from ticketmaster_python_sdk.pydantic.date_time_field_type import DateTimeFieldType
from ticketmaster_python_sdk.pydantic.duration_field import DurationField

class DateTimeField(BaseModel):
    duration_field: typing.Optional[DurationField] = Field(None, alias='durationField')

    leap_duration_field: typing.Optional[DurationField] = Field(None, alias='leapDurationField')

    lenient: typing.Optional[bool] = Field(None, alias='lenient')

    maximum_value: typing.Optional[int] = Field(None, alias='maximumValue')

    minimum_value: typing.Optional[int] = Field(None, alias='minimumValue')

    name: typing.Optional[str] = Field(None, alias='name')

    range_duration_field: typing.Optional[DurationField] = Field(None, alias='rangeDurationField')

    supported: typing.Optional[bool] = Field(None, alias='supported')

    type: typing.Optional[DateTimeFieldType] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
