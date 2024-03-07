# coding: utf-8
"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

import typing
import inspect
from datetime import date, datetime
from ticketmaster_python_sdk.client_custom import ClientCustom
from ticketmaster_python_sdk.configuration import Configuration
from ticketmaster_python_sdk.api_client import ApiClient
from ticketmaster_python_sdk.type_util import copy_signature
from ticketmaster_python_sdk.apis.tags.v2_api import V2Api



class Ticketmaster(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.v2: V2Api = V2Api(api_client)
