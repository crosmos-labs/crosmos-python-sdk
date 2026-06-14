# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Search", "Candidate"]


class Candidate(BaseModel):
    content: str

    created_at: datetime

    event_time: Optional[datetime] = None

    memory_id: str

    memory_type: str

    recorded_at: datetime

    score: float

    owner_id: Optional[str] = None
    """External id of the user who ingested this memory.

    Null for org-level memories not attributable to a single user.
    """

    owner_name: Optional[str] = None
    """Display name of the owning user, for attribution in shared orgs."""

    source: Optional[str] = None
    """Original source text the memory was extracted from"""


class Search(BaseModel):
    candidates: List[Candidate]

    query: str

    took_ms: float
    """Search execution time in milliseconds"""

    total: int
    """Total number of candidates returned"""
