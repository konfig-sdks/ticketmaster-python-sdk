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


class RequiredAddress(TypedDict):
    pass

class OptionalAddress(TypedDict, total=False):
    # Address first line
    line1: str

    # Address second line
    line2: str

    # Address third line
    line3: str

class Address(RequiredAddress, OptionalAddress):
    pass
