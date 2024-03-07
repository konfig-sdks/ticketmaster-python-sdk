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

from ticketmaster_python_sdk.type.attraction_external_links import AttractionExternalLinks
from ticketmaster_python_sdk.type.attraction_upcoming_events import AttractionUpcomingEvents
from ticketmaster_python_sdk.type.classification import Classification
from ticketmaster_python_sdk.type.image import Image

class RequiredAttraction(TypedDict):
    # Unique id of the entity in the discovery API
    id: str

    # Type of the entity
    type: str

class OptionalAttraction(TypedDict, total=False):
    # Description's of the entity
    description: str

    # Additional information of the entity
    additionalInfo: str

    # Attraction's classifications
    classifications: typing.List[Classification]

    externalLinks: AttractionExternalLinks

    # Images of the entity
    images: typing.List[Image]

    # Locale in which the content is returned
    locale: str

    # Name of the entity
    name: str

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: bool

    upcomingEvents: AttractionUpcomingEvents

    # URL of a web site detail page of the entity
    url: str

class Attraction(RequiredAttraction, OptionalAttraction):
    pass
