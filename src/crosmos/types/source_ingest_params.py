# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SourceIngestParams", "Source"]


class SourceIngestParams(TypedDict, total=False):
    sources: Required[Iterable[Source]]

    space_id: Required[str]


class Source(TypedDict, total=False):
    content: Required[str]

    content_type: Literal["text", "markdown", "conversation", "html", "json", "pdf", "image", "audio", "video"]
    """Today only `text` and `markdown` are processable."""

    meta: Optional[Dict[str, Optional[object]]]

    role: str

    visibility: Literal["private", "org"]
