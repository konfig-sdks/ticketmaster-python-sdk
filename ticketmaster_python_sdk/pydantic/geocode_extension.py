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

from ticketmaster_python_sdk.pydantic.geometry import Geometry

class GeocodeExtension(BaseModel):
    city: typing.Optional[str] = Field(None, alias='city')

    country: typing.Optional[str] = Field(None, alias='country')

    county: typing.Optional[str] = Field(None, alias='county')

    formatted_address: typing.Optional[str] = Field(None, alias='formattedAddress')

    geometry: typing.Optional[Geometry] = Field(None, alias='geometry')

    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    route: typing.Optional[str] = Field(None, alias='route')

    state: typing.Optional[str] = Field(None, alias='state')

    street_number: typing.Optional[str] = Field(None, alias='streetNumber')
    class Config:
        arbitrary_types_allowed = True
