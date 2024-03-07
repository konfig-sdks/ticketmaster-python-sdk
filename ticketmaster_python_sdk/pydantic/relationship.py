# coding: utf-8

"""
    Discovery API

    The Ticketmaster Discovery API allows you to search for events, attractions, or venues.

    The version of the OpenAPI document: v2
    Created by: http://developer.ticketmaster.com/support/contact-us/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from ticketmaster_python_sdk.pydantic.relationship_references import RelationshipReferences

class Relationship(BaseModel):
    # The ID of the related entity
    id: typing.Optional[str] = Field(None, alias='id')

    references: typing.Optional[RelationshipReferences] = Field(None, alias='references')

    # The source name of the related entity
    source: typing.Optional[str] = Field(None, alias='source')

    # The type of the relationship
    type: typing.Optional[Literal["duplicate"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
