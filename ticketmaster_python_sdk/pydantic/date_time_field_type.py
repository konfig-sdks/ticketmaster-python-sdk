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

from ticketmaster_python_sdk.pydantic.duration_field_type import DurationFieldType

class DateTimeFieldType(BaseModel):
    duration_type: typing.Optional[DurationFieldType] = Field(None, alias='durationType')

    name: typing.Optional[str] = Field(None, alias='name')

    range_duration_type: typing.Optional[DurationFieldType] = Field(None, alias='rangeDurationType')
    class Config:
        arbitrary_types_allowed = True