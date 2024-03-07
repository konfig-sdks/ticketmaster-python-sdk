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

from ticketmaster_python_sdk.pydantic.address import Address
from ticketmaster_python_sdk.pydantic.area import Area
from ticketmaster_python_sdk.pydantic.city import City
from ticketmaster_python_sdk.pydantic.country import Country
from ticketmaster_python_sdk.pydantic.location import Location
from ticketmaster_python_sdk.pydantic.state import State

class Place(BaseModel):
    address: typing.Optional[Address] = Field(None, alias='address')

    area: typing.Optional[Area] = Field(None, alias='area')

    city: typing.Optional[City] = Field(None, alias='city')

    country: typing.Optional[Country] = Field(None, alias='country')

    location: typing.Optional[Location] = Field(None, alias='location')

    # Name of the entity
    name: typing.Optional[str] = Field(None, alias='name')

    # Postal code / zipcode of the place
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    state: typing.Optional[State] = Field(None, alias='state')
    class Config:
        arbitrary_types_allowed = True
