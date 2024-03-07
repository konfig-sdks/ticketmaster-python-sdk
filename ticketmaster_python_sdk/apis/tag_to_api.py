import typing_extensions

from ticketmaster_python_sdk.apis.tags import TagValues
from ticketmaster_python_sdk.apis.tags.v2_api import V2Api

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.V2: V2Api,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.V2: V2Api,
    }
)
