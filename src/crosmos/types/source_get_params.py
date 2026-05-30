# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceGetParams"]


class SourceGetParams(TypedDict, total=False):
    space_uuid: Required[str]
