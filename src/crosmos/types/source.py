# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    id: str

    content: str

    content_type: str

    created_at: datetime

    extraction_status: str

    space_id: str

    token_count: int

    updated_at: datetime

    meta: Optional[object] = None
