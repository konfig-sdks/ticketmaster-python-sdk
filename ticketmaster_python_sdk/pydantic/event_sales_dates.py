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

from ticketmaster_python_sdk.pydantic.presale import Presale
from ticketmaster_python_sdk.pydantic.public_sale_dates import PublicSaleDates

class EventSalesDates(BaseModel):
    # Presale information on this event
    presales: typing.Optional[typing.List[Presale]] = Field(None, alias='presales')

    public: typing.Optional[PublicSaleDates] = Field(None, alias='public')
    class Config:
        arbitrary_types_allowed = True
