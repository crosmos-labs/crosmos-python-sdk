# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VisibilityPreviewParams"]


class VisibilityPreviewParams(TypedDict, total=False):
    user_id: Required[str]
    """The user whose visibility to preview."""
