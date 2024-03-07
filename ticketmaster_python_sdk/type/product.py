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


class RequiredProduct(TypedDict):
    pass

class OptionalProduct(TypedDict, total=False):
    # Product's primary id
    id: str

    # Name of the entity
    name: str

    # Product's type
    type: str

    # Product's url
    url: str

class Product(RequiredProduct, OptionalProduct):
    pass
