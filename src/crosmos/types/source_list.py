# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceList", "Source"]


class Source(BaseModel):
    id: str

    content_preview: str

    content_type: str

    created_at: datetime

    extraction_status: Literal["pending", "processing", "completed", "failed"]

    meta: Optional[Dict[str, Optional[object]]] = None

    space_id: str

    token_count: int

    updated_at: datetime


class SourceList(BaseModel):
    count: int

    sources: List[Source]

    total: int
