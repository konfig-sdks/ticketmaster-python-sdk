# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

import unittest
from unittest.mock import patch

import urllib3

import ticketmaster_python_sdk
from ticketmaster_python_sdk.paths.discovery_v2_venues import get
from ticketmaster_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDiscoveryV2Venues(ApiTestMixin, unittest.TestCase):
    """
    DiscoveryV2Venues unit test stubs
        Venue Search
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
