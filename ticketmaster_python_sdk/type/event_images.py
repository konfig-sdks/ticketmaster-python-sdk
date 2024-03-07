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

from ticketmaster_python_sdk.type.image import Image

class RequiredEventImages(TypedDict):
    # Unique id of the entity in the discovery API
    id: str

    # Type of the entity
    type: str

class OptionalEventImages(TypedDict, total=False):
    # Images of the entity
    images: typing.List[Image]

class EventImages(RequiredEventImages, OptionalEventImages):
    pass
