# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from ticketmaster_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from ticketmaster_python_sdk.api_response import AsyncGeneratorResponse
from ticketmaster_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ticketmaster_python_sdk import schemas  # noqa: F401

from ticketmaster_python_sdk.model.v2_find_venues_response import V2FindVenuesResponse as V2FindVenuesResponseSchema

from ticketmaster_python_sdk.type.v2_find_venues_response import V2FindVenuesResponse

from ...api_client import Dictionary
from ticketmaster_python_sdk.pydantic.v2_find_venues_response import V2FindVenuesResponse as V2FindVenuesResponsePydantic

from . import path

# Query params


class SortSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^(name|relevance|distance),(asc|desc)$',
        }]
StateCodeSchema = schemas.StrSchema
CountryCodeSchema = schemas.StrSchema


class LatlongSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*$|^-?(90(\.0+)?|[0-8]?[0-9](\.\d+)?),-?(180(\.0+)?|(1[0-7][0-9]|\d{1,2})(\.\d+)?)$',
        }]


class RadiusSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*$|^0*1?\d{1,4}$',
        }]


class UnitSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*|miles|km$',
        }]
        enum_value_to_name = {
            "miles": "MILES",
            "km": "KM",
        }
    
    @schemas.classproperty
    def MILES(cls):
        return cls("miles")
    
    @schemas.classproperty
    def KM(cls):
        return cls("km")


class GeoPointSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*$|^-?(90(\.0+)?|[0-8]?[0-9](\.\d+)?),-?(180(\.0+)?|(1[0-7][0-9]|\d{1,2})(\.\d+)?)$|^[a-zA-Z0-9]{1,9}$',
        }]
KeywordSchema = schemas.StrSchema
IdSchema = schemas.StrSchema


class SourceSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "ticketmaster": "TICKETMASTER",
            " universe": "UNIVERSE",
            " frontgate": "FRONTGATE",
            " tmr": "TMR",
        }
    
    @schemas.classproperty
    def TICKETMASTER(cls):
        return cls("ticketmaster")
    
    @schemas.classproperty
    def UNIVERSE(cls):
        return cls(" universe")
    
    @schemas.classproperty
    def FRONTGATE(cls):
        return cls(" frontgate")
    
    @schemas.classproperty
    def TMR(cls):
        return cls(" tmr")


class IncludeTestSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*|yes|no|only$',
        }]
        enum_value_to_name = {
            "true": "TRUE",
            " no": "NO",
            " only": "ONLY",
        }
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def NO(cls):
        return cls(" no")
    
    @schemas.classproperty
    def ONLY(cls):
        return cls(" only")


class PageSchema(
    schemas.StrSchema
):


    class MetaOapg:


class SizeSchema(
    schemas.StrSchema
):


    class MetaOapg:
LocaleSchema = schemas.StrSchema


class IncludeLicensedContentSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*|yes|no$',
        }]
        enum_value_to_name = {
            "true": "TRUE",
            " no": "NO",
        }
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def NO(cls):
        return cls(" no")


class IncludeSpellcheckSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\s*|yes|no',
        }]
        enum_value_to_name = {
            "true": "TRUE",
            " no": "NO",
        }
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def NO(cls):
        return cls(" no")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'sort': typing.Union[SortSchema, str, ],
        'stateCode': typing.Union[StateCodeSchema, str, ],
        'countryCode': typing.Union[CountryCodeSchema, str, ],
        'latlong': typing.Union[LatlongSchema, str, ],
        'radius': typing.Union[RadiusSchema, str, ],
        'unit': typing.Union[UnitSchema, str, ],
        'geoPoint': typing.Union[GeoPointSchema, str, ],
        'keyword': typing.Union[KeywordSchema, str, ],
        'id': typing.Union[IdSchema, str, ],
        'source': typing.Union[SourceSchema, str, ],
        'includeTest': typing.Union[IncludeTestSchema, str, ],
        'page': typing.Union[PageSchema, str, ],
        'size': typing.Union[SizeSchema, str, ],
        'locale': typing.Union[LocaleSchema, str, ],
        'includeLicensedContent': typing.Union[IncludeLicensedContentSchema, str, ],
        'includeSpellcheck': typing.Union[IncludeSpellcheckSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_state_code = api_client.QueryParameter(
    name="stateCode",
    style=api_client.ParameterStyle.FORM,
    schema=StateCodeSchema,
    explode=True,
)
request_query_country_code = api_client.QueryParameter(
    name="countryCode",
    style=api_client.ParameterStyle.FORM,
    schema=CountryCodeSchema,
    explode=True,
)
request_query_latlong = api_client.QueryParameter(
    name="latlong",
    style=api_client.ParameterStyle.FORM,
    schema=LatlongSchema,
    explode=True,
)
request_query_radius = api_client.QueryParameter(
    name="radius",
    style=api_client.ParameterStyle.FORM,
    schema=RadiusSchema,
    explode=True,
)
request_query_unit = api_client.QueryParameter(
    name="unit",
    style=api_client.ParameterStyle.FORM,
    schema=UnitSchema,
    explode=True,
)
request_query_geo_point = api_client.QueryParameter(
    name="geoPoint",
    style=api_client.ParameterStyle.FORM,
    schema=GeoPointSchema,
    explode=True,
)
request_query_keyword = api_client.QueryParameter(
    name="keyword",
    style=api_client.ParameterStyle.FORM,
    schema=KeywordSchema,
    explode=True,
)
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_source = api_client.QueryParameter(
    name="source",
    style=api_client.ParameterStyle.FORM,
    schema=SourceSchema,
    explode=True,
)
request_query_include_test = api_client.QueryParameter(
    name="includeTest",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeTestSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_size = api_client.QueryParameter(
    name="size",
    style=api_client.ParameterStyle.FORM,
    schema=SizeSchema,
    explode=True,
)
request_query_locale = api_client.QueryParameter(
    name="locale",
    style=api_client.ParameterStyle.FORM,
    schema=LocaleSchema,
    explode=True,
)
request_query_include_licensed_content = api_client.QueryParameter(
    name="includeLicensedContent",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeLicensedContentSchema,
    explode=True,
)
request_query_include_spellcheck = api_client.QueryParameter(
    name="includeSpellcheck",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeSpellcheckSchema,
    explode=True,
)
_auth = [
    'apiKey',
]
SchemaFor200ResponseBody = V2FindVenuesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: V2FindVenuesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: V2FindVenuesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    '*/*',
)


class BaseApi(api_client.Api):

    def _find_venues_mapped_args(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if sort is not None:
            _query_params["sort"] = sort
        if state_code is not None:
            _query_params["stateCode"] = state_code
        if country_code is not None:
            _query_params["countryCode"] = country_code
        if latlong is not None:
            _query_params["latlong"] = latlong
        if radius is not None:
            _query_params["radius"] = radius
        if unit is not None:
            _query_params["unit"] = unit
        if geo_point is not None:
            _query_params["geoPoint"] = geo_point
        if keyword is not None:
            _query_params["keyword"] = keyword
        if id is not None:
            _query_params["id"] = id
        if source is not None:
            _query_params["source"] = source
        if include_test is not None:
            _query_params["includeTest"] = include_test
        if page is not None:
            _query_params["page"] = page
        if size is not None:
            _query_params["size"] = size
        if locale is not None:
            _query_params["locale"] = locale
        if include_licensed_content is not None:
            _query_params["includeLicensedContent"] = include_licensed_content
        if include_spellcheck is not None:
            _query_params["includeSpellcheck"] = include_spellcheck
        args.query = _query_params
        return args

    async def _afind_venues_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Venue Search
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_sort,
            request_query_state_code,
            request_query_country_code,
            request_query_latlong,
            request_query_radius,
            request_query_unit,
            request_query_geo_point,
            request_query_keyword,
            request_query_id,
            request_query_source,
            request_query_include_test,
            request_query_page,
            request_query_size,
            request_query_locale,
            request_query_include_licensed_content,
            request_query_include_spellcheck,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/discovery/v2/venues',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _find_venues_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Venue Search
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_sort,
            request_query_state_code,
            request_query_country_code,
            request_query_latlong,
            request_query_radius,
            request_query_unit,
            request_query_geo_point,
            request_query_keyword,
            request_query_id,
            request_query_source,
            request_query_include_test,
            request_query_page,
            request_query_size,
            request_query_locale,
            request_query_include_licensed_content,
            request_query_include_spellcheck,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/discovery/v2/venues',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class FindVenuesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_venues(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_venues_mapped_args(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
        )
        return await self._afind_venues_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def find_venues(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_venues_mapped_args(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
        )
        return self._find_venues_oapg(
            query_params=args.query,
        )

class FindVenues(BaseApi):

    async def afind_venues(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> V2FindVenuesResponsePydantic:
        raw_response = await self.raw.afind_venues(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
            **kwargs,
        )
        if validate:
            return RootModel[V2FindVenuesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(V2FindVenuesResponsePydantic, raw_response.body)
    
    
    def find_venues(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
        validate: bool = False,
    ) -> V2FindVenuesResponsePydantic:
        raw_response = self.raw.find_venues(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
        )
        if validate:
            return RootModel[V2FindVenuesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(V2FindVenuesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_venues_mapped_args(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
        )
        return await self._afind_venues_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        sort: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        latlong: typing.Optional[str] = None,
        radius: typing.Optional[str] = None,
        unit: typing.Optional[str] = None,
        geo_point: typing.Optional[str] = None,
        keyword: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        include_test: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        include_licensed_content: typing.Optional[str] = None,
        include_spellcheck: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_venues_mapped_args(
            sort=sort,
            state_code=state_code,
            country_code=country_code,
            latlong=latlong,
            radius=radius,
            unit=unit,
            geo_point=geo_point,
            keyword=keyword,
            id=id,
            source=source,
            include_test=include_test,
            page=page,
            size=size,
            locale=locale,
            include_licensed_content=include_licensed_content,
            include_spellcheck=include_spellcheck,
        )
        return self._find_venues_oapg(
            query_params=args.query,
        )

