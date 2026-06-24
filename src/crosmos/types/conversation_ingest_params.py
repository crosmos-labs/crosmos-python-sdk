# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConversationIngestParams", "Message"]


class ConversationIngestParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    space_id: Required[str]

    meta: Optional[Dict[str, Optional[object]]]

    session_date: str

    session_id: str

    visibility: Literal["private", "org"]


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
