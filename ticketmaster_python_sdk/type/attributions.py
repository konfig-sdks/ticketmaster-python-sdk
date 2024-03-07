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

from ticketmaster_python_sdk.type.attribution import Attribution
from ticketmaster_python_sdk.type.attributions_descriptions import AttributionsDescriptions

class RequiredAttributions(TypedDict):
    pass

class OptionalAttributions(TypedDict, total=False):
    description: Attribution

    descriptions: AttributionsDescriptions

class Attributions(RequiredAttributions, OptionalAttributions):
    pass
