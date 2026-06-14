# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VisibilityCreateGrantParams"]


class VisibilityCreateGrantParams(TypedDict, total=False):
    subject_group_id: Required[str]

    viewer_group_id: Required[str]
