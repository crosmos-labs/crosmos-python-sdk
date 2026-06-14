# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConversationIngestParams", "Message"]


class ConversationIngestParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Ordered conversation messages"""

    space_id: Required[str]
    """Memory space to ingest into"""

    meta: Optional[Dict[str, object]]
    """Optional metadata attached to all created sources"""

    session_date: Optional[str]
    """ISO date string for when the session occurred"""

    session_id: Optional[str]
    """Session identifier. Auto-generated if not provided."""

    visibility: Literal["private", "org"]
    """Read scope: 'private' (gated by the visibility graph) or 'org' (readable by
    everyone in the org)"""


class Message(TypedDict, total=False):
    content: Required[str]
    """Message content"""

    role: Required[str]
    """Speaker role (e.g. 'user', 'assistant')"""
