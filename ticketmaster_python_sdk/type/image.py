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


class RequiredImage(TypedDict):
    pass

class OptionalImage(TypedDict, total=False):
    # Attribution of the image
    attribution: str

    # true if the image is not the event's image but a fallbak image
    fallback: bool

    # Height of the image
    height: int

    # Aspect ratio of the image
    ratio: str

    # Public URL of the image
    url: str

    # Width of the image
    width: int

class Image(RequiredImage, OptionalImage):
    pass
