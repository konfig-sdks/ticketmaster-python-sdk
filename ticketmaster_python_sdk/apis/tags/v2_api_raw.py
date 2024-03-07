# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

from ticketmaster_python_sdk.paths.discovery_v2_events.get import EventSearchRaw
from ticketmaster_python_sdk.paths.discovery_v2_suggest.get import FindSuggestRaw
from ticketmaster_python_sdk.paths.discovery_v2_venues.get import FindVenuesRaw
from ticketmaster_python_sdk.paths.discovery_v2_attractions_id.get import GetAttractionDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_classifications_id.get import GetClassificationDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_events_id.get import GetEventDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_events_id_images.get import GetEventImagesRaw
from ticketmaster_python_sdk.paths.discovery_v2_classifications_genres_id.get import GetGenreDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_classifications_segments_id.get import GetSegmentDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_classifications_subgenres_id.get import GetSubgenreDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_venues_id.get import GetVenueDetailsRaw
from ticketmaster_python_sdk.paths.discovery_v2_attractions.get import SearchAttractionsRaw
from ticketmaster_python_sdk.paths.discovery_v2_classifications.get import SearchClassificationsRaw


class V2ApiRaw(
    EventSearchRaw,
    FindSuggestRaw,
    FindVenuesRaw,
    GetAttractionDetailsRaw,
    GetClassificationDetailsRaw,
    GetEventDetailsRaw,
    GetEventImagesRaw,
    GetGenreDetailsRaw,
    GetSegmentDetailsRaw,
    GetSubgenreDetailsRaw,
    GetVenueDetailsRaw,
    SearchAttractionsRaw,
    SearchClassificationsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass