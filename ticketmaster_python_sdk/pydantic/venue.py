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
from ticketmaster_python_sdk.pydantic.city import City
from ticketmaster_python_sdk.pydantic.country import Country
from ticketmaster_python_sdk.pydantic.dma import Dma
from ticketmaster_python_sdk.pydantic.image import Image
from ticketmaster_python_sdk.pydantic.location import Location
from ticketmaster_python_sdk.pydantic.market import Market
from ticketmaster_python_sdk.pydantic.social import Social
from ticketmaster_python_sdk.pydantic.state import State
from ticketmaster_python_sdk.pydantic.venue_box_office_info import VenueBoxOfficeInfo
from ticketmaster_python_sdk.pydantic.venue_external_links import VenueExternalLinks
from ticketmaster_python_sdk.pydantic.venue_general_info import VenueGeneralInfo
from ticketmaster_python_sdk.pydantic.venue_upcoming_events import VenueUpcomingEvents

class Venue(BaseModel):
    # Unique id of the entity in the discovery API
    id: str = Field(alias='id')

    # Type of the entity
    type: Literal["event", "venue", "attraction"] = Field(alias='type')

    # Description's of the entity
    description: typing.Optional[str] = Field(None, alias='description')

    # Venue accessible seating detail
    accessible_seating_detail: typing.Optional[str] = Field(None, alias='accessibleSeatingDetail')

    # Additional information of the entity
    additional_info: typing.Optional[str] = Field(None, alias='additionalInfo')

    address: typing.Optional[Address] = Field(None, alias='address')

    box_office_info: typing.Optional[VenueBoxOfficeInfo] = Field(None, alias='boxOfficeInfo')

    city: typing.Optional[City] = Field(None, alias='city')

    country: typing.Optional[Country] = Field(None, alias='country')

    # Default currency of ticket prices for events in this venue
    currency: typing.Optional[str] = Field(None, alias='currency')

    distance: typing.Optional[typing.Union[int, float]] = Field(None, alias='distance')

    # The list of associated DMAs (Designated Market Areas) of the venue
    dma: typing.Optional[typing.List[Dma]] = Field(None, alias='dma')

    external_links: typing.Optional[VenueExternalLinks] = Field(None, alias='externalLinks')

    general_info: typing.Optional[VenueGeneralInfo] = Field(None, alias='generalInfo')

    # Images of the entity
    images: typing.Optional[typing.List[Image]] = Field(None, alias='images')

    # Locale in which the content is returned
    locale: typing.Optional[str] = Field(None, alias='locale')

    location: typing.Optional[Location] = Field(None, alias='location')

    # Markets of the venue
    markets: typing.Optional[typing.List[Market]] = Field(None, alias='markets')

    # Name of the entity
    name: typing.Optional[str] = Field(None, alias='name')

    # Venue parking info
    parking_detail: typing.Optional[str] = Field(None, alias='parkingDetail')

    # Postal code / zipcode of the venue
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    social: typing.Optional[Social] = Field(None, alias='social')

    state: typing.Optional[State] = Field(None, alias='state')

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: typing.Optional[bool] = Field(None, alias='test')

    # Timezone of the venue
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    units: typing.Optional[str] = Field(None, alias='units')

    upcoming_events: typing.Optional[VenueUpcomingEvents] = Field(None, alias='upcomingEvents')

    # URL of a web site detail page of the entity
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
