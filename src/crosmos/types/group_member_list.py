# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .group_member import GroupMember

__all__ = ["GroupMemberList"]


class GroupMemberList(BaseModel):
    members: List[GroupMember]
