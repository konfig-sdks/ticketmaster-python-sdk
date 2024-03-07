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

from ticketmaster_python_sdk.pydantic.image import Image

class EventImages(BaseModel):
    # Unique id of the entity in the discovery API
    id: str = Field(alias='id')

    # Type of the entity
    type: Literal["event"] = Field(alias='type')

    # Images of the entity
    images: typing.Optional[typing.List[Image]] = Field(None, alias='images')
    class Config:
        arbitrary_types_allowed = True
