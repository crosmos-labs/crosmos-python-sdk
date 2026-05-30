# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityDetail", "Memory"]


class Memory(BaseModel):
    content: str

    created_at: datetime

    memory_id: str

    memory_type: str


class EntityDetail(BaseModel):
    id: str

    created_at: datetime

    edge_count: int
    """Total incoming + outgoing edges"""

    entity_type: Optional[str] = None

    memories: List[Memory]
    """Recent memories mentioning this entity"""

    name: str

    space_id: str

    updated_at: datetime
