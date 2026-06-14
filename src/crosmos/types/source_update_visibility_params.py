# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SourceUpdateVisibilityParams"]


class SourceUpdateVisibilityParams(TypedDict, total=False):
    space_uuid: Required[str]
    """Memory space the source belongs to (query param)."""

    visibility: Required[Literal["private", "org"]]
    """New read scope. 'private' un-publishes org-shared content."""
