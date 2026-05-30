# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntityListParams"]


class EntityListParams(TypedDict, total=False):
    space_uuid: Required[str]

    entity_type: Optional[str]
    """Filter by entity type"""

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    q: Optional[str]
    """Search entities by name"""

    sort_by: Literal["name", "edge_count", "created_at"]
