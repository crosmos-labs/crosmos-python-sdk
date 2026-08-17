# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    id: str

    content: str

    content_type: str

    created_at: datetime

    extraction_status: Literal["pending", "processing", "completed", "failed"]

    meta: Optional[Dict[str, Optional[object]]] = None

    space_id: str

    token_count: int

    updated_at: datetime
