# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EntityListParams"]


class EntityListParams(TypedDict, total=False):
    entity_type: str

    limit: int

    offset: Optional[int]

    order: Literal["asc", "desc"]

    q: str

    sort_by: Literal["name", "edge_count", "created_at"]

    space_id: str

    space_uuid: str
