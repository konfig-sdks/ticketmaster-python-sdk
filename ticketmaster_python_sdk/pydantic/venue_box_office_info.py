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


class VenueBoxOfficeInfo(BaseModel):
    # Venue box office accepted payment details
    accepted_payment_detail: typing.Optional[str] = Field(None, alias='acceptedPaymentDetail')

    # Venue box office opening hours
    open_hours_detail: typing.Optional[str] = Field(None, alias='openHoursDetail')

    # Venue box office phone number
    phone_number_detail: typing.Optional[str] = Field(None, alias='phoneNumberDetail')

    # Venue box office will call details
    will_call_detail: typing.Optional[str] = Field(None, alias='willCallDetail')
    class Config:
        arbitrary_types_allowed = True
