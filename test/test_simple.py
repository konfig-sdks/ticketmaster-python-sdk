# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

import unittest

import os
from pprint import pprint
from ticketmaster_python_sdk import Ticketmaster

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        ticketmaster = Ticketmaster(
        
                        api_key = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(ticketmaster)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
