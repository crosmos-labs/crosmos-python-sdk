# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Job", "Result"]


class Result(BaseModel):
    edge_count: int

    entity_count: int

    failed_source_ids: List[int]

    memory_count: int

    source_ids: List[int]

    tokens_used: int

    error_message: Optional[str] = None

    source_errors: Optional[Dict[str, str]] = None


class Job(BaseModel):
    completed_at: Optional[datetime] = None

    created_at: datetime

    error_message: Optional[str] = None

    job_id: str

    result: Optional[Result] = None

    source_ids: List[int]

    started_at: Optional[datetime] = None

    status: Literal["pending", "processing", "completed", "partial", "failed", "cancelled"]
