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


class RequiredVenueBoxOfficeInfo(TypedDict):
    pass

class OptionalVenueBoxOfficeInfo(TypedDict, total=False):
    # Venue box office accepted payment details
    acceptedPaymentDetail: str

    # Venue box office opening hours
    openHoursDetail: str

    # Venue box office phone number
    phoneNumberDetail: str

    # Venue box office will call details
    willCallDetail: str

class VenueBoxOfficeInfo(RequiredVenueBoxOfficeInfo, OptionalVenueBoxOfficeInfo):
    pass
