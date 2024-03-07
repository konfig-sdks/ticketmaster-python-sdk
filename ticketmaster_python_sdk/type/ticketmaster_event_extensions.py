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

from ticketmaster_python_sdk.type.display_setting_extension import DisplaySettingExtension

class RequiredTicketmasterEventExtensions(TypedDict):
    pass

class OptionalTicketmasterEventExtensions(TypedDict, total=False):
    displaySettings: DisplaySettingExtension

class TicketmasterEventExtensions(RequiredTicketmasterEventExtensions, OptionalTicketmasterEventExtensions):
    pass
