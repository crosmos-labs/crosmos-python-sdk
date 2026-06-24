# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SourceListParams"]


class SourceListParams(TypedDict, total=False):
    content_type: str

    extraction_status: Literal["pending", "processing", "completed", "failed"]

    limit: int

    offset: Optional[int]

    space_id: str

    space_uuid: str
