# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .entity import Entity
from .._models import BaseModel

__all__ = ["EntityDetail", "EntityDetailMemory"]


class EntityDetailMemory(BaseModel):
    content: str

    created_at: datetime

    memory_id: str

    memory_type: str


class EntityDetail(Entity):
    memories: List[EntityDetailMemory]
