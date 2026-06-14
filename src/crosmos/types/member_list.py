# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .member import Member
from .._models import BaseModel

__all__ = ["MemberList"]


class MemberList(BaseModel):
    members: List[Member]

    next_cursor: Optional[str] = None
