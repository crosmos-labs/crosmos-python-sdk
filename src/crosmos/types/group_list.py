# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .group import Group
from .._models import BaseModel

__all__ = ["GroupList"]


class GroupList(BaseModel):
    groups: List[Group]
