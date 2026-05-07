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

    source: Optional[str] = None
    """Original source text the memory was extracted from"""


class Search(BaseModel):
    candidates: List[Candidate]

    query: str

    took_ms: float
    """Search execution time in milliseconds"""

    total: int
    """Total number of candidates returned"""
