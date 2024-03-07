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


class AccessDates(BaseModel):
    # Boolean flag to indicate whether or not the access end date is approximated
    end_approximate: typing.Optional[bool] = Field(None, alias='endApproximate')

    # Event's end access time
    end_date_time: typing.Optional[datetime] = Field(None, alias='endDateTime')

    # Boolean flag to indicate whether or not the access start date is approximated
    start_approximate: typing.Optional[bool] = Field(None, alias='startApproximate')

    # Event's start access time
    start_date_time: typing.Optional[datetime] = Field(None, alias='startDateTime')
    class Config:
        arbitrary_types_allowed = True
