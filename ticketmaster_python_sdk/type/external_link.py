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


class RequiredExternalLink(TypedDict):
    pass

class OptionalExternalLink(TypedDict, total=False):
    # An external link id is the unique identifier of a resource on a different domain or api
    id: str

    # An external link url is a url that goes to a different domain or api
    url: str

class ExternalLink(RequiredExternalLink, OptionalExternalLink):
    pass
