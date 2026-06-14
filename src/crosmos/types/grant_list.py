# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .grant import Grant
from .._models import BaseModel

__all__ = ["GrantList"]


class GrantList(BaseModel):
    grants: List[Grant]
