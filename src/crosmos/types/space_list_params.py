# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SpaceListParams"]


class SpaceListParams(TypedDict, total=False):
    name: Optional[str]
    """Exact-match filter on space name within the active org.

    Returns 0 or 1 spaces (names are unique per org).
    """
