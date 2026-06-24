# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemoryListParams"]


class MemoryListParams(TypedDict, total=False):
    limit: int

    memory_type: Literal["viewpoint", "semantic", "episode", "inference"]

    offset: Optional[int]

    order: Literal["asc", "desc"]

    sort_by: Literal["created_at", "importance_score", "event_time", "last_accessed_at", "access_frequency"]

    space_id: str

    space_uuid: str
