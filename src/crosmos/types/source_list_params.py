# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SourceListParams"]


class SourceListParams(TypedDict, total=False):
    content_type: Optional[str]

    extraction_status: Optional[str]

    limit: int

    offset: int

    space_id: Optional[str]
