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


class PublicSaleDates(BaseModel):
    # Public sale's end dates. The date and time when the public sale will end
    end_date_time: typing.Optional[datetime] = Field(None, alias='endDateTime')

    # Public sale's start dates. The date and time when the public sale will start
    start_date_time: typing.Optional[datetime] = Field(None, alias='startDateTime')

    # True if the public sale's date is to be determined
    start_t_b_d: typing.Optional[bool] = Field(None, alias='startTBD')
    class Config:
        arbitrary_types_allowed = True
