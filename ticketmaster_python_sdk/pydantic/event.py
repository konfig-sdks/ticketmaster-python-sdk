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

from ticketmaster_python_sdk.pydantic.accessibility import Accessibility
from ticketmaster_python_sdk.pydantic.classification import Classification
from ticketmaster_python_sdk.pydantic.event_dates import EventDates
from ticketmaster_python_sdk.pydantic.event_external_links import EventExternalLinks
from ticketmaster_python_sdk.pydantic.event_sales_dates import EventSalesDates
from ticketmaster_python_sdk.pydantic.image import Image
from ticketmaster_python_sdk.pydantic.location import Location
from ticketmaster_python_sdk.pydantic.outlet import Outlet
from ticketmaster_python_sdk.pydantic.place import Place
from ticketmaster_python_sdk.pydantic.price_range import PriceRange
from ticketmaster_python_sdk.pydantic.product import Product
from ticketmaster_python_sdk.pydantic.promoter import Promoter
from ticketmaster_python_sdk.pydantic.seat_map import SeatMap

class Event(BaseModel):
    # Unique id of the entity in the discovery API
    id: str = Field(alias='id')

    # Type of the entity
    type: Literal["event", "venue", "attraction"] = Field(alias='type')

    # Any information related to the event
    info: typing.Optional[str] = Field(None, alias='info')

    # Description's of the entity
    description: typing.Optional[str] = Field(None, alias='description')

    accessibility: typing.Optional[Accessibility] = Field(None, alias='accessibility')

    # Additional information of the entity
    additional_info: typing.Optional[str] = Field(None, alias='additionalInfo')

    # Event's classifications
    classifications: typing.Optional[typing.List[Classification]] = Field(None, alias='classifications')

    dates: typing.Optional[EventDates] = Field(None, alias='dates')

    distance: typing.Optional[typing.Union[int, float]] = Field(None, alias='distance')

    external_links: typing.Optional[EventExternalLinks] = Field(None, alias='externalLinks')

    # Images of the entity
    images: typing.Optional[typing.List[Image]] = Field(None, alias='images')

    # Locale in which the content is returned
    locale: typing.Optional[str] = Field(None, alias='locale')

    location: typing.Optional[Location] = Field(None, alias='location')

    # Name of the entity
    name: typing.Optional[str] = Field(None, alias='name')

    # Related outlets informations
    outlets: typing.Optional[typing.List[Outlet]] = Field(None, alias='outlets')

    place: typing.Optional[Place] = Field(None, alias='place')

    # Any notes related to the event
    please_note: typing.Optional[str] = Field(None, alias='pleaseNote')

    # Price ranges of this event
    price_ranges: typing.Optional[typing.List[PriceRange]] = Field(None, alias='priceRanges')

    # Related products informations
    products: typing.Optional[typing.List[Product]] = Field(None, alias='products')

    promoter: typing.Optional[Promoter] = Field(None, alias='promoter')

    # Event's promoters
    promoters: typing.Optional[typing.List[Promoter]] = Field(None, alias='promoters')

    sales: typing.Optional[EventSalesDates] = Field(None, alias='sales')

    seatmap: typing.Optional[SeatMap] = Field(None, alias='seatmap')

    # Indicate if this is a test entity, by default test entities won't appear in discovery API
    test: typing.Optional[bool] = Field(None, alias='test')

    units: typing.Optional[str] = Field(None, alias='units')

    # URL of a web site detail page of the entity
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
