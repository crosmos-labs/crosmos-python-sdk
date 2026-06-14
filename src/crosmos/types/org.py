# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Org"]


class Org(BaseModel):
    id: str

    billing_email: Optional[str] = None

    created_at: datetime

    name: str

    plan: str

    slug: str

    updated_at: datetime
