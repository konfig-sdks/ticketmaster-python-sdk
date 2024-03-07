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

from ticketmaster_python_sdk.pydantic.level import Level
from ticketmaster_python_sdk.pydantic.segment import Segment

class Classification(BaseModel):
    genre: typing.Optional[Level] = Field(None, alias='genre')

    # True if this is the entity's primary classification
    primary: typing.Optional[bool] = Field(None, alias='primary')

    segment: typing.Optional[Segment] = Field(None, alias='segment')

    sub_genre: typing.Optional[Level] = Field(None, alias='subGenre')

    sub_type: typing.Optional[Level] = Field(None, alias='subType')

    type: typing.Optional[Level] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
