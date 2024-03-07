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


class Presale(BaseModel):
    # Description of the presame
    description: typing.Optional[str] = Field(None, alias='description')

    # Presale's end dates. The date and time when the presale will end
    end_date_time: typing.Optional[datetime] = Field(None, alias='endDateTime')

    # Name of the presale
    name: typing.Optional[str] = Field(None, alias='name')

    # Presale's start dates. The date and time when the presale will start
    start_date_time: typing.Optional[datetime] = Field(None, alias='startDateTime')

    # Presale link URL
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
