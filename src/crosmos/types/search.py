# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Search", "Candidate"]


class Candidate(BaseModel):
    content: str

    created_at: str

    event_time: Optional[str] = None

    memory_id: str

    memory_type: str

    owner_name: Optional[str] = None

    score: float

    source: Optional[str] = None


class Search(BaseModel):
    candidates: List[Candidate]

    query: str
