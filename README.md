<div align="center">

[![Visit Ticketmaster](./header.png)](https://developer.ticketmaster.com&#x2F;products-and-docs&#x2F;apis&#x2F;discovery-api&#x2F;v2&#x2F;)

# Ticketmaster<a id="ticketmaster"></a>

The Ticketmaster Discovery API allows you to search for events, attractions, or venues.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`ticketmaster.v2.event_search`](#ticketmasterv2event_search)
  * [`ticketmaster.v2.find_suggest`](#ticketmasterv2find_suggest)
  * [`ticketmaster.v2.find_venues`](#ticketmasterv2find_venues)
  * [`ticketmaster.v2.get_attraction_details`](#ticketmasterv2get_attraction_details)
  * [`ticketmaster.v2.get_classification_details`](#ticketmasterv2get_classification_details)
  * [`ticketmaster.v2.get_event_details`](#ticketmasterv2get_event_details)
  * [`ticketmaster.v2.get_event_images`](#ticketmasterv2get_event_images)
  * [`ticketmaster.v2.get_genre_details`](#ticketmasterv2get_genre_details)
  * [`ticketmaster.v2.get_segment_details`](#ticketmasterv2get_segment_details)
  * [`ticketmaster.v2.get_subgenre_details`](#ticketmasterv2get_subgenre_details)
  * [`ticketmaster.v2.get_venue_details`](#ticketmasterv2get_venue_details)
  * [`ticketmaster.v2.search_attractions`](#ticketmasterv2search_attractions)
  * [`ticketmaster.v2.search_classifications`](#ticketmasterv2search_classifications)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Ticketmaster&serviceName=Discovery&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from ticketmaster_python_sdk import Ticketmaster, ApiException

ticketmaster = Ticketmaster(
    api_key="YOUR_API_KEY",
)

try:
    # Event Search
    event_search_response = ticketmaster.v2.event_search(
        sort="",
        start_date_time="",
        end_date_time="",
        onsale_start_date_time="",
        onsale_on_start_date="",
        onsale_on_after_start_date="",
        onsale_end_date_time="",
        city="",
        country_code="",
        state_code="",
        postal_code="",
        venue_id="",
        attraction_id="",
        segment_id="",
        segment_name="",
        classification_name=[None],
        classification_id=[None],
        market_id="",
        promoter_id="",
        dma_id="",
        include_tba="",
        include_tbd="",
        client_visibility="",
        latlong="33.80003000,-117.88304300",
        radius="",
        unit="",
        geo_point="dr5rh",
        keyword="",
        id="",
        source="",
        include_test="",
        page="",
        size="",
        locale="en-us,en,fr",
        include_licensed_content="",
        include_spellcheck="",
    )
    print(event_search_response)
except ApiException as e:
    print("Exception when calling V2Api.event_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from ticketmaster_python_sdk import Ticketmaster, ApiException

ticketmaster = Ticketmaster(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Event Search
        event_search_response = await ticketmaster.v2.aevent_search(
            sort="",
            start_date_time="",
            end_date_time="",
            onsale_start_date_time="",
            onsale_on_start_date="",
            onsale_on_after_start_date="",
            onsale_end_date_time="",
            city="",
            country_code="",
            state_code="",
            postal_code="",
            venue_id="",
            attraction_id="",
            segment_id="",
            segment_name="",
            classification_name=[None],
            classification_id=[None],
            market_id="",
            promoter_id="",
            dma_id="",
            include_tba="",
            include_tbd="",
            client_visibility="",
            latlong="33.80003000,-117.88304300",
            radius="",
            unit="",
            geo_point="dr5rh",
            keyword="",
            id="",
            source="",
            include_test="",
            page="",
            size="",
            locale="en-us,en,fr",
            include_licensed_content="",
            include_spellcheck="",
        )
        print(event_search_response)
    except ApiException as e:
        print("Exception when calling V2Api.event_search: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from ticketmaster_python_sdk import Ticketmaster, ApiException

ticketmaster = Ticketmaster(
    api_key="YOUR_API_KEY",
)

try:
    # Event Search
    event_search_response = ticketmaster.v2.raw.event_search(
        sort="",
        start_date_time="",
        end_date_time="",
        onsale_start_date_time="",
        onsale_on_start_date="",
        onsale_on_after_start_date="",
        onsale_end_date_time="",
        city="",
        country_code="",
        state_code="",
        postal_code="",
        venue_id="",
        attraction_id="",
        segment_id="",
        segment_name="",
        classification_name=[None],
        classification_id=[None],
        market_id="",
        promoter_id="",
        dma_id="",
        include_tba="",
        include_tbd="",
        client_visibility="",
        latlong="33.80003000,-117.88304300",
        radius="",
        unit="",
        geo_point="dr5rh",
        keyword="",
        id="",
        source="",
        include_test="",
        page="",
        size="",
        locale="en-us,en,fr",
        include_licensed_content="",
        include_spellcheck="",
    )
    pprint(event_search_response.body)
    pprint(event_search_response.headers)
    pprint(event_search_response.status)
    pprint(event_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling V2Api.event_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `ticketmaster.v2.event_search`<a id="ticketmasterv2event_search"></a>

Find events and filter your search by location, date, availability, and much more.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
event_search_response = ticketmaster.v2.event_search(
    sort="",
    start_date_time="",
    end_date_time="",
    onsale_start_date_time="",
    onsale_on_start_date="",
    onsale_on_after_start_date="",
    onsale_end_date_time="",
    city="",
    country_code="",
    state_code="",
    postal_code="",
    venue_id="",
    attraction_id="",
    segment_id="",
    segment_name="",
    classification_name=[None],
    classification_id=[None],
    market_id="",
    promoter_id="",
    dma_id="",
    include_tba="",
    include_tbd="",
    client_visibility="",
    latlong="33.80003000,-117.88304300",
    radius="",
    unit="",
    geo_point="dr5rh",
    keyword="",
    id="",
    source="",
    include_test="",
    page="",
    size="",
    locale="en-us,en,fr",
    include_licensed_content="",
    include_spellcheck="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sorting order of the search result. Allowable values : 'name,asc', 'name,desc', 'date,asc', 'date,desc', 'relevance,asc', 'relevance,desc', 'distance,asc', 'name,date,asc', 'name,date,desc', 'date,name,asc', 'date,name,desc','onsaleStartDate,asc', 'id,asc'

##### start_date_time: `str`<a id="start_date_time-str"></a>

Filter events with a start date after this date

##### end_date_time: `str`<a id="end_date_time-str"></a>

Filter events with a start date before this date

##### onsale_start_date_time: `str`<a id="onsale_start_date_time-str"></a>

Filter events with onsale start date after this date

##### onsale_on_start_date: `str`<a id="onsale_on_start_date-str"></a>

Filter events with onsale start date on this date

##### onsale_on_after_start_date: `str`<a id="onsale_on_after_start_date-str"></a>

Filter events with onsale range within this date

##### onsale_end_date_time: `str`<a id="onsale_end_date_time-str"></a>

Filter events with onsale end date before this date

##### city: `str`<a id="city-str"></a>

Filter events by city

##### country_code: `str`<a id="country_code-str"></a>

Filter events by country code

##### state_code: `str`<a id="state_code-str"></a>

Filter events by state code

##### postal_code: `str`<a id="postal_code-str"></a>

Filter events by postal code / zipcode

##### venue_id: `str`<a id="venue_id-str"></a>

Filter events by venue id

##### attraction_id: `str`<a id="attraction_id-str"></a>

Filter events by attraction id

##### segment_id: `str`<a id="segment_id-str"></a>

Filter events by segment id

##### segment_name: `str`<a id="segment_name-str"></a>

Filter events by segment name

##### classification_name: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./ticketmaster_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="classification_name-listunionbool-date-datetime-dict-float-int-list-str-noneticketmaster_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter events by classification name: name of any segment, genre, sub-genre, type, sub-type

##### classification_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./ticketmaster_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="classification_id-listunionbool-date-datetime-dict-float-int-list-str-noneticketmaster_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter events by classification id: id of any segment, genre, sub-genre, type, sub-type

##### market_id: `str`<a id="market_id-str"></a>

Filter events by market id

##### promoter_id: `str`<a id="promoter_id-str"></a>

Filter events by promoter id

##### dma_id: `str`<a id="dma_id-str"></a>

Filter events by dma id

##### include_tba: `str`<a id="include_tba-str"></a>

True, to include events with date to be announce (TBA)

##### include_tbd: `str`<a id="include_tbd-str"></a>

True, to include event with a date to be defined (TBD)

##### client_visibility: `str`<a id="client_visibility-str"></a>

Filter events by clientName

##### latlong: `str`<a id="latlong-str"></a>

Filter events by latitude and longitude, this filter is deprecated and maybe removed in a future release, please use geoPoint instead

##### radius: `str`<a id="radius-str"></a>

Radius of the area in which we want to search for events.

##### unit: `str`<a id="unit-str"></a>

Unit of the radius

##### geo_point: `str`<a id="geo_point-str"></a>

filter events by geoHash

##### keyword: `str`<a id="keyword-str"></a>

Keyword to search on

##### id: `str`<a id="id-str"></a>

Filter entities by its id

##### source: `str`<a id="source-str"></a>

Filter entities by its source name

##### include_test: `str`<a id="include_test-str"></a>

True if you want to have entities flag as test in the response. Only, if you only wanted test entities

##### page: `str`<a id="page-str"></a>

Page number

##### size: `str`<a id="size-str"></a>

Page size of the response

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

Yes if you want to display licensed content

##### include_spellcheck: `str`<a id="include_spellcheck-str"></a>

yes, to include spell check suggestions in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`V2EventSearchResponse`](./ticketmaster_python_sdk/pydantic/v2_event_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.find_suggest`<a id="ticketmasterv2find_suggest"></a>

Find search suggestions and filter your suggestions by location, source, etc.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_suggest_response = ticketmaster.v2.find_suggest(
    keyword="",
    source="",
    latlong="33.80003000,-117.88304300",
    radius="",
    unit="",
    size="",
    include_fuzzy="",
    client_visibility="",
    country_code="",
    include_tba="",
    include_tbd="",
    segment_id="",
    geo_point="dr5rh",
    locale="en-us,en,fr",
    include_licensed_content="",
    include_spellcheck="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### keyword: `str`<a id="keyword-str"></a>

Keyword to search on

##### source: `str`<a id="source-str"></a>

Filter entities by its source name

##### latlong: `str`<a id="latlong-str"></a>

Filter events by latitude and longitude, this filter is deprecated and maybe removed in a future release, please use geoPoint instead

##### radius: `str`<a id="radius-str"></a>

Radius of the area in which we want to search for events.

##### unit: `str`<a id="unit-str"></a>

Unit of the radius

##### size: `str`<a id="size-str"></a>

Size of every entity returned in the response

##### include_fuzzy: `str`<a id="include_fuzzy-str"></a>

yes, to include fuzzy matches in the search. This has performance impact.

##### client_visibility: `str`<a id="client_visibility-str"></a>

Filter events to clientName

##### country_code: `str`<a id="country_code-str"></a>

Filter suggestions by country code

##### include_tba: `str`<a id="include_tba-str"></a>

True, to include events with date to be announce (TBA)

##### include_tbd: `str`<a id="include_tbd-str"></a>

True, to include event with a date to be defined (TBD)

##### segment_id: `str`<a id="segment_id-str"></a>

Filter suggestions by segment id

##### geo_point: `str`<a id="geo_point-str"></a>

filter events by geoHash

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

Yes if you want to display licensed content

##### include_spellcheck: `str`<a id="include_spellcheck-str"></a>

yes, to include spell check suggestions in the response.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/suggest` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.find_venues`<a id="ticketmasterv2find_venues"></a>

Find venues and filter your search by name, and much more.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_venues_response = ticketmaster.v2.find_venues(
    sort="",
    state_code="",
    country_code="",
    latlong="33.80003000,-117.88304300",
    radius="",
    unit="",
    geo_point="dr5rh",
    keyword="",
    id="",
    source="",
    include_test="",
    page="",
    size="",
    locale="en-us,en,fr",
    include_licensed_content="",
    include_spellcheck="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sorting order of the search result. Allowable Values: 'name,asc', 'name,desc', 'relevance,asc', 'relevance,desc', 'distance,asc', 'distance,desc'

##### state_code: `str`<a id="state_code-str"></a>

Filter venues by state / province code

##### country_code: `str`<a id="country_code-str"></a>

Filter venues by country code

##### latlong: `str`<a id="latlong-str"></a>

Filter events by latitude and longitude, this filter is deprecated and maybe removed in a future release, please use geoPoint instead

##### radius: `str`<a id="radius-str"></a>

Radius of the area in which we want to search for events.

##### unit: `str`<a id="unit-str"></a>

Unit of the radius

##### geo_point: `str`<a id="geo_point-str"></a>

filter events by geoHash

##### keyword: `str`<a id="keyword-str"></a>

Keyword to search on

##### id: `str`<a id="id-str"></a>

Filter entities by its id

##### source: `str`<a id="source-str"></a>

Filter entities by its source name

##### include_test: `str`<a id="include_test-str"></a>

True if you want to have entities flag as test in the response. Only, if you only wanted test entities

##### page: `str`<a id="page-str"></a>

Page number

##### size: `str`<a id="size-str"></a>

Page size of the response

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

Yes if you want to display licensed content

##### include_spellcheck: `str`<a id="include_spellcheck-str"></a>

yes, to include spell check suggestions in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`V2FindVenuesResponse`](./ticketmaster_python_sdk/pydantic/v2_find_venues_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/venues` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_attraction_details`<a id="ticketmasterv2get_attraction_details"></a>

Get details for a specific attraction using the unique identifier for the attraction.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attraction_details_response = ticketmaster.v2.get_attraction_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the attraction

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Attraction`](./ticketmaster_python_sdk/pydantic/attraction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/attractions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_classification_details`<a id="ticketmasterv2get_classification_details"></a>

Get details for a specific segment, genre, or sub-genre using its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_classification_details_response = ticketmaster.v2.get_classification_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the segment, genre, or sub-genre

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./ticketmaster_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/classifications/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_event_details`<a id="ticketmasterv2get_event_details"></a>

Get details for a specific event using the unique identifier for the event. This includes the venue and location, the attraction(s), and the Ticketmaster Website URL for purchasing tickets for the event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_details_response = ticketmaster.v2.get_event_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the event

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Event`](./ticketmaster_python_sdk/pydantic/event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/events/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_event_images`<a id="ticketmasterv2get_event_images"></a>

Get images for a specific event using the unique identifier for the event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_images_response = ticketmaster.v2.get_event_images(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the event

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`EventImages`](./ticketmaster_python_sdk/pydantic/event_images.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/events/{id}/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_genre_details`<a id="ticketmasterv2get_genre_details"></a>

Get details for a specific genre using its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_genre_details_response = ticketmaster.v2.get_genre_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the genre

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Genre`](./ticketmaster_python_sdk/pydantic/genre.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/classifications/genres/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_segment_details`<a id="ticketmasterv2get_segment_details"></a>

Get details for a specific segment using its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_segment_details_response = ticketmaster.v2.get_segment_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the segment

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Segment`](./ticketmaster_python_sdk/pydantic/segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/classifications/segments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_subgenre_details`<a id="ticketmasterv2get_subgenre_details"></a>

Get details for a specific sub-genre using its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subgenre_details_response = ticketmaster.v2.get_subgenre_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the subgenre

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Level`](./ticketmaster_python_sdk/pydantic/level.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/classifications/subgenres/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.get_venue_details`<a id="ticketmasterv2get_venue_details"></a>

Get details for a specific venue using the unique identifier for the venue.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_venue_details_response = ticketmaster.v2.get_venue_details(
    id="id_example",
    locale="en-us,en,fr",
    include_licensed_content="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

ID of the venue

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

True if you want to display licensed content

#### 🔄 Return<a id="🔄-return"></a>

[`Venue`](./ticketmaster_python_sdk/pydantic/venue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/venues/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.search_attractions`<a id="ticketmasterv2search_attractions"></a>

Find attractions (artists, sports, packages, plays and so on) and filter your search by name, and much more.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_attractions_response = ticketmaster.v2.search_attractions(
    sort="",
    classification_name=[None],
    classification_id=[None],
    keyword="",
    id="",
    source="",
    include_test="",
    page="",
    size="",
    locale="en-us,en,fr",
    include_licensed_content="",
    include_spellcheck="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sorting order of the search result. Allowable Values : 'name,asc', 'name,desc', 'relevance,asc', 'relevance,desc'

##### classification_name: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./ticketmaster_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="classification_name-listunionbool-date-datetime-dict-float-int-list-str-noneticketmaster_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter attractions by classification name: name of any segment, genre, sub-genre, type, sub-type

##### classification_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./ticketmaster_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="classification_id-listunionbool-date-datetime-dict-float-int-list-str-noneticketmaster_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter attractions by classification id: id of any segment, genre, sub-genre, type, sub-type

##### keyword: `str`<a id="keyword-str"></a>

Keyword to search on

##### id: `str`<a id="id-str"></a>

Filter entities by its id

##### source: `str`<a id="source-str"></a>

Filter entities by its source name

##### include_test: `str`<a id="include_test-str"></a>

True if you want to have entities flag as test in the response. Only, if you only wanted test entities

##### page: `str`<a id="page-str"></a>

Page number

##### size: `str`<a id="size-str"></a>

Page size of the response

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

Yes if you want to display licensed content

##### include_spellcheck: `str`<a id="include_spellcheck-str"></a>

yes, to include spell check suggestions in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`V2SearchAttractionsResponse`](./ticketmaster_python_sdk/pydantic/v2_search_attractions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/attractions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ticketmaster.v2.search_classifications`<a id="ticketmasterv2search_classifications"></a>

Find classifications and filter your search by name, and much more. Classifications help define the nature of attractions and events.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_classifications_response = ticketmaster.v2.search_classifications(
    sort="",
    keyword="",
    id="",
    source="",
    include_test="",
    page="",
    size="",
    locale="en-us,en,fr",
    include_licensed_content="",
    include_spellcheck="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sorting order of the search result

##### keyword: `str`<a id="keyword-str"></a>

Keyword to search on

##### id: `str`<a id="id-str"></a>

Filter entities by its id

##### source: `str`<a id="source-str"></a>

Filter entities by its source name

##### include_test: `str`<a id="include_test-str"></a>

True if you want to have entities flag as test in the response. Only, if you only wanted test entities

##### page: `str`<a id="page-str"></a>

Page number

##### size: `str`<a id="size-str"></a>

Page size of the response

##### locale: `str`<a id="locale-str"></a>

The locale in ISO code format. Multiple comma-separated values can be provided. When omitting the country part of the code (e.g. only 'en' or 'fr') then the first matching locale is used. When using a '*' it matches all locales. '*' can only be used at the end (e.g. 'en-us,en,*') 

##### include_licensed_content: `str`<a id="include_licensed_content-str"></a>

Yes if you want to display licensed content

##### include_spellcheck: `str`<a id="include_spellcheck-str"></a>

yes, to include spell check suggestions in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`V2SearchClassificationsResponse`](./ticketmaster_python_sdk/pydantic/v2_search_classifications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/discovery/v2/classifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
