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
from ticketmaster_python_sdk.type.city import City
from ticketmaster_python_sdk.type.country import Country
from ticketmaster_python_sdk.type.dma import Dma
from ticketmaster_python_sdk.type.image import Image
from ticketmaster_python_sdk.type.location import Location
from ticketmaster_python_sdk.type.market import Market
from ticketmaster_python_sdk.type.social import Social
from ticketmaster_python_sdk.type.state import State
from ticketmaster_python_sdk.type.venue_box_office_info import VenueBoxOfficeInfo
from ticketmaster_python_sdk.type.venue_external_links import VenueExternalLinks
from ticketmaster_python_sdk.type.venue_general_info import VenueGeneralInfo
from ticketmaster_python_sdk.type.venue_upcoming_events import VenueUpcomingEvents

class RequiredVenue(TypedDict):
    # Unique id of the entity in the discovery API
    id: str

    # Type of the entity
    type: str

class OptionalVenue(TypedDict, total=False):
    # Description's of the entity
    description: str

    # Venue accessible seating detail
    accessibleSeatingDetail: str

    # Additional information of the entity
    additionalInfo: str

    address: Address

    boxOfficeInfo: VenueBoxOfficeInfo

    city: City

    country: Country

    # Default currency of ticket prices for events in this venue
    currency: str

    distance: typing.Union[int, float]

    # The list of associated DMAs (Designated Market Areas) of the venue
    dma: typing.List[Dma]

    externalLinks: VenueExternalLinks

    generalInfo: VenueGeneralInfo

    # Images of the entity
    images: typing.List[Image]

    # Locale in which the content is returned
    locale: str

    location: Location

    # Markets of the venue
    markets: typing.List[Market]

    # Name of the entity
    name: str

    # Venue parking info
    parkingDetail: str

    # Postal code / zipcode of the venue
    postalCode: str

    social: Social

    state: State

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: bool

    # Timezone of the venue
    timezone: str

    units: str

    upcomingEvents: VenueUpcomingEvents

    # URL of a web site detail page of the entity
    url: str

class Venue(RequiredVenue, OptionalVenue):
    pass
