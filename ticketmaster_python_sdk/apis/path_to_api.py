import typing_extensions

from ticketmaster_python_sdk.paths import PathValues
from ticketmaster_python_sdk.apis.paths.discovery_v2_attractions import DiscoveryV2Attractions
from ticketmaster_python_sdk.apis.paths.discovery_v2_attractions_id import DiscoveryV2AttractionsId
from ticketmaster_python_sdk.apis.paths.discovery_v2_classifications import DiscoveryV2Classifications
from ticketmaster_python_sdk.apis.paths.discovery_v2_classifications_genres_id import DiscoveryV2ClassificationsGenresId
from ticketmaster_python_sdk.apis.paths.discovery_v2_classifications_segments_id import DiscoveryV2ClassificationsSegmentsId
from ticketmaster_python_sdk.apis.paths.discovery_v2_classifications_subgenres_id import DiscoveryV2ClassificationsSubgenresId
from ticketmaster_python_sdk.apis.paths.discovery_v2_classifications_id import DiscoveryV2ClassificationsId
from ticketmaster_python_sdk.apis.paths.discovery_v2_events import DiscoveryV2Events
from ticketmaster_python_sdk.apis.paths.discovery_v2_events_id import DiscoveryV2EventsId
from ticketmaster_python_sdk.apis.paths.discovery_v2_events_id_images import DiscoveryV2EventsIdImages
from ticketmaster_python_sdk.apis.paths.discovery_v2_suggest import DiscoveryV2Suggest
from ticketmaster_python_sdk.apis.paths.discovery_v2_venues import DiscoveryV2Venues
from ticketmaster_python_sdk.apis.paths.discovery_v2_venues_id import DiscoveryV2VenuesId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DISCOVERY_V2_ATTRACTIONS: DiscoveryV2Attractions,
        PathValues.DISCOVERY_V2_ATTRACTIONS_ID: DiscoveryV2AttractionsId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS: DiscoveryV2Classifications,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_GENRES_ID: DiscoveryV2ClassificationsGenresId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_SEGMENTS_ID: DiscoveryV2ClassificationsSegmentsId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_SUBGENRES_ID: DiscoveryV2ClassificationsSubgenresId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_ID: DiscoveryV2ClassificationsId,
        PathValues.DISCOVERY_V2_EVENTS: DiscoveryV2Events,
        PathValues.DISCOVERY_V2_EVENTS_ID: DiscoveryV2EventsId,
        PathValues.DISCOVERY_V2_EVENTS_ID_IMAGES: DiscoveryV2EventsIdImages,
        PathValues.DISCOVERY_V2_SUGGEST: DiscoveryV2Suggest,
        PathValues.DISCOVERY_V2_VENUES: DiscoveryV2Venues,
        PathValues.DISCOVERY_V2_VENUES_ID: DiscoveryV2VenuesId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DISCOVERY_V2_ATTRACTIONS: DiscoveryV2Attractions,
        PathValues.DISCOVERY_V2_ATTRACTIONS_ID: DiscoveryV2AttractionsId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS: DiscoveryV2Classifications,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_GENRES_ID: DiscoveryV2ClassificationsGenresId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_SEGMENTS_ID: DiscoveryV2ClassificationsSegmentsId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_SUBGENRES_ID: DiscoveryV2ClassificationsSubgenresId,
        PathValues.DISCOVERY_V2_CLASSIFICATIONS_ID: DiscoveryV2ClassificationsId,
        PathValues.DISCOVERY_V2_EVENTS: DiscoveryV2Events,
        PathValues.DISCOVERY_V2_EVENTS_ID: DiscoveryV2EventsId,
        PathValues.DISCOVERY_V2_EVENTS_ID_IMAGES: DiscoveryV2EventsIdImages,
        PathValues.DISCOVERY_V2_SUGGEST: DiscoveryV2Suggest,
        PathValues.DISCOVERY_V2_VENUES: DiscoveryV2Venues,
        PathValues.DISCOVERY_V2_VENUES_ID: DiscoveryV2VenuesId,
    }
)
