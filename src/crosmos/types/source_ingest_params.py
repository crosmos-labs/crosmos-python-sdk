# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SourceIngestParams", "Source"]


class SourceIngestParams(TypedDict, total=False):
    sources: Required[Iterable[Source]]
    """Array of source payloads to ingest"""

    space_id: Required[str]
    """Memory space to ingest into"""


class Source(TypedDict, total=False):
    content: Required[str]
    """Raw content to ingest"""

    content_type: str
    """Content MIME type: text, markdown, html, json, pdf, image, audio, video"""

    meta: Optional[Dict[str, object]]
    """Optional metadata stored with the source"""

    role: Optional[str]
    """Optional speaker role (e.g. 'user', 'assistant')"""

    sequence: int
    """Order within the batch (0-indexed)"""
