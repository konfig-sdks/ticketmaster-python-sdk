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

from ticketmaster_python_sdk.pydantic.attraction_external_links import AttractionExternalLinks
from ticketmaster_python_sdk.pydantic.attraction_upcoming_events import AttractionUpcomingEvents
from ticketmaster_python_sdk.pydantic.classification import Classification
from ticketmaster_python_sdk.pydantic.image import Image

class Attraction(BaseModel):
    # Unique id of the entity in the discovery API
    id: str = Field(alias='id')

    # Type of the entity
    type: Literal["event", "venue", "attraction"] = Field(alias='type')

    # Description's of the entity
    description: typing.Optional[str] = Field(None, alias='description')

    # Additional information of the entity
    additional_info: typing.Optional[str] = Field(None, alias='additionalInfo')

    # Attraction's classifications
    classifications: typing.Optional[typing.List[Classification]] = Field(None, alias='classifications')

    external_links: typing.Optional[AttractionExternalLinks] = Field(None, alias='externalLinks')

    # Images of the entity
    images: typing.Optional[typing.List[Image]] = Field(None, alias='images')

    # Locale in which the content is returned
    locale: typing.Optional[str] = Field(None, alias='locale')

    # Name of the entity
    name: typing.Optional[str] = Field(None, alias='name')

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: typing.Optional[bool] = Field(None, alias='test')

    upcoming_events: typing.Optional[AttractionUpcomingEvents] = Field(None, alias='upcomingEvents')

    # URL of a web site detail page of the entity
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
