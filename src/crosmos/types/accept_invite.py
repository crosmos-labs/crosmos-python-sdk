# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .org import Org
from .._models import BaseModel

__all__ = ["AcceptInvite"]


class AcceptInvite(BaseModel):
    org: Org

    role: Literal["admin", "member"]
