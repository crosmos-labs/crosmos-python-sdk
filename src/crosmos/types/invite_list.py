# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .invite import Invite
from .._models import BaseModel

__all__ = ["InviteList"]


class InviteList(BaseModel):
    invites: List[Invite]
