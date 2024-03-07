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

from ticketmaster_python_sdk.type.presale import Presale
from ticketmaster_python_sdk.type.public_sale_dates import PublicSaleDates

class RequiredEventSalesDates(TypedDict):
    pass

class OptionalEventSalesDates(TypedDict, total=False):
    # Presale information on this event
    presales: typing.List[Presale]

    public: PublicSaleDates

class EventSalesDates(RequiredEventSalesDates, OptionalEventSalesDates):
    pass
