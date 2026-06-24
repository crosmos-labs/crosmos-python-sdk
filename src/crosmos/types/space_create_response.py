# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SpaceCreateResponse"]


class SpaceCreateResponse(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    meta: Optional[Dict[str, Optional[object]]] = None

    name: str

    org_id: str

    updated_at: datetime
