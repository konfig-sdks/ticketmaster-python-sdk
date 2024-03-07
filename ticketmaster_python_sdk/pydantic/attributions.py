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

from ticketmaster_python_sdk.pydantic.attribution import Attribution
from ticketmaster_python_sdk.pydantic.attributions_descriptions import AttributionsDescriptions

class Attributions(BaseModel):
    description: typing.Optional[Attribution] = Field(None, alias='description')

    descriptions: typing.Optional[AttributionsDescriptions] = Field(None, alias='descriptions')
    class Config:
        arbitrary_types_allowed = True
