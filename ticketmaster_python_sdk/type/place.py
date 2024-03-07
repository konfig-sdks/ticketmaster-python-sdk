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

from ticketmaster_python_sdk.type.address import Address
from ticketmaster_python_sdk.type.area import Area
from ticketmaster_python_sdk.type.city import City
from ticketmaster_python_sdk.type.country import Country
from ticketmaster_python_sdk.type.location import Location
from ticketmaster_python_sdk.type.state import State

class RequiredPlace(TypedDict):
    pass

class OptionalPlace(TypedDict, total=False):
    address: Address

    area: Area

    city: City

    country: Country

    location: Location

    # Name of the entity
    name: str

    # Postal code / zipcode of the place
    postalCode: str

    state: State

class Place(RequiredPlace, OptionalPlace):
    pass
