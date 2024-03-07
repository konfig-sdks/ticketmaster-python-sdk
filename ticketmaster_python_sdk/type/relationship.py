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

from ticketmaster_python_sdk.type.relationship_references import RelationshipReferences

class RequiredRelationship(TypedDict):
    pass

class OptionalRelationship(TypedDict, total=False):
    # The ID of the related entity
    id: str

    references: RelationshipReferences

    # The source name of the related entity
    source: str

    # The type of the relationship
    type: str

class Relationship(RequiredRelationship, OptionalRelationship):
    pass
