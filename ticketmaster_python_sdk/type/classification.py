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

from ticketmaster_python_sdk.type.level import Level
from ticketmaster_python_sdk.type.segment import Segment

class RequiredClassification(TypedDict):
    pass

class OptionalClassification(TypedDict, total=False):
    genre: Level

    # True if this is the entity's primary classification
    primary: bool

    segment: Segment

    subGenre: Level

    subType: Level

    type: Level

class Classification(RequiredClassification, OptionalClassification):
    pass
