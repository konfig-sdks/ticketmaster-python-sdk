# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ticketmaster_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DISCOVERY_V2_ATTRACTIONS = "/discovery/v2/attractions"
    DISCOVERY_V2_ATTRACTIONS_ID = "/discovery/v2/attractions/{id}"
    DISCOVERY_V2_CLASSIFICATIONS = "/discovery/v2/classifications"
    DISCOVERY_V2_CLASSIFICATIONS_GENRES_ID = "/discovery/v2/classifications/genres/{id}"
    DISCOVERY_V2_CLASSIFICATIONS_SEGMENTS_ID = "/discovery/v2/classifications/segments/{id}"
    DISCOVERY_V2_CLASSIFICATIONS_SUBGENRES_ID = "/discovery/v2/classifications/subgenres/{id}"
    DISCOVERY_V2_CLASSIFICATIONS_ID = "/discovery/v2/classifications/{id}"
    DISCOVERY_V2_EVENTS = "/discovery/v2/events"
    DISCOVERY_V2_EVENTS_ID = "/discovery/v2/events/{id}"
    DISCOVERY_V2_EVENTS_ID_IMAGES = "/discovery/v2/events/{id}/images"
    DISCOVERY_V2_SUGGEST = "/discovery/v2/suggest"
    DISCOVERY_V2_VENUES = "/discovery/v2/venues"
    DISCOVERY_V2_VENUES_ID = "/discovery/v2/venues/{id}"
