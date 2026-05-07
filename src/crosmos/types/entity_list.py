# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .entity import Entity
from .._models import BaseModel

__all__ = ["EntityList"]


class EntityList(BaseModel):
    entities: List[Entity]

    total: int
