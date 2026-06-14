# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["VisibilityUpdateGroupParams"]


class VisibilityUpdateGroupParams(TypedDict, total=False):
    org_uuid: Required[str]
    """Path param: the organization the group belongs to."""

    name: Optional[str]
    """Body param: new display name."""

    slug: Optional[str]
    """Body param: new slug."""
