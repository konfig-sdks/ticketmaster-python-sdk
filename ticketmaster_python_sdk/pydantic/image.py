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


class Image(BaseModel):
    # Attribution of the image
    attribution: typing.Optional[str] = Field(None, alias='attribution')

    # true if the image is not the event's image but a fallbak image
    fallback: typing.Optional[bool] = Field(None, alias='fallback')

    # Height of the image
    height: typing.Optional[int] = Field(None, alias='height')

    # Aspect ratio of the image
    ratio: typing.Optional[Literal["169", "32", "43"]] = Field(None, alias='ratio')

    # Public URL of the image
    url: typing.Optional[str] = Field(None, alias='url')

    # Width of the image
    width: typing.Optional[int] = Field(None, alias='width')
    class Config:
        arbitrary_types_allowed = True
