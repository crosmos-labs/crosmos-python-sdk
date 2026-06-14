# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str

    created_at: datetime

    member_count: int

    name: str

    slug: str

    updated_at: datetime
