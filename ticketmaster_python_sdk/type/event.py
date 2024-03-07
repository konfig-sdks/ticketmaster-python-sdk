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

from ticketmaster_python_sdk.type.accessibility import Accessibility
from ticketmaster_python_sdk.type.classification import Classification
from ticketmaster_python_sdk.type.event_dates import EventDates
from ticketmaster_python_sdk.type.event_external_links import EventExternalLinks
from ticketmaster_python_sdk.type.event_sales_dates import EventSalesDates
from ticketmaster_python_sdk.type.image import Image
from ticketmaster_python_sdk.type.location import Location
from ticketmaster_python_sdk.type.outlet import Outlet
from ticketmaster_python_sdk.type.place import Place
from ticketmaster_python_sdk.type.price_range import PriceRange
from ticketmaster_python_sdk.type.product import Product
from ticketmaster_python_sdk.type.promoter import Promoter
from ticketmaster_python_sdk.type.seat_map import SeatMap

class RequiredEvent(TypedDict):
    # Unique id of the entity in the discovery API
    id: str

    # Type of the entity
    type: str

class OptionalEvent(TypedDict, total=False):
    # Any information related to the event
    info: str

    # Description's of the entity
    description: str

    accessibility: Accessibility

    # Additional information of the entity
    additionalInfo: str

    # Event's classifications
    classifications: typing.List[Classification]

    dates: EventDates

    distance: typing.Union[int, float]

    externalLinks: EventExternalLinks

    # Images of the entity
    images: typing.List[Image]

    # Locale in which the content is returned
    locale: str

    location: Location

    # Name of the entity
    name: str

    # Related outlets informations
    outlets: typing.List[Outlet]

    place: Place

    # Any notes related to the event
    pleaseNote: str

    # Price ranges of this event
    priceRanges: typing.List[PriceRange]

    # Related products informations
    products: typing.List[Product]

    promoter: Promoter

    # Event's promoters
    promoters: typing.List[Promoter]

    sales: EventSalesDates

    seatmap: SeatMap

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: bool

    units: str

    # URL of a web site detail page of the entity
    url: str

class Event(RequiredEvent, OptionalEvent):
    pass
