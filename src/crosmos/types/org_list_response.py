# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OrgListResponse", "Org"]


class Org(BaseModel):
    id: str

    billing_email: Optional[str] = None

    created_at: datetime

    member_count: int

    name: str

    plan: str

    slug: str

    updated_at: datetime

    your_role: Literal["owner", "admin", "member"]


class OrgListResponse(BaseModel):
    orgs: List[Org]

    next_cursor: Optional[str] = None
