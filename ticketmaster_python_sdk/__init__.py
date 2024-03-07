# coding: utf-8

# flake8: noqa

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

__version__ = "v2"

# import ApiClient
from ticketmaster_python_sdk.api_client import ApiClient

# import Configuration
from ticketmaster_python_sdk.configuration import Configuration

# import exceptions
from ticketmaster_python_sdk.exceptions import OpenApiException
from ticketmaster_python_sdk.exceptions import ApiAttributeError
from ticketmaster_python_sdk.exceptions import ApiTypeError
from ticketmaster_python_sdk.exceptions import ApiValueError
from ticketmaster_python_sdk.exceptions import ApiKeyError
from ticketmaster_python_sdk.exceptions import ApiException

from ticketmaster_python_sdk.client import Ticketmaster
