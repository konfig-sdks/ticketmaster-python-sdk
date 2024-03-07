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


class Location(BaseModel):
    # Latitude
    latitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='latitude')

    # Longitude
    longitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='longitude')
    class Config:
        arbitrary_types_allowed = True
