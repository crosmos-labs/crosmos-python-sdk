# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Entity"]


class Entity(BaseModel):
    id: str

    created_at: datetime

    edge_count: int

    entity_type: Optional[str] = None

    name: str

    space_id: str

    updated_at: datetime
