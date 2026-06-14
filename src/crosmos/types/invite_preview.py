# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvitePreview"]


class InvitePreview(BaseModel):
    email: str

    expires_at: datetime

    inviter_name: Optional[str] = None

    org_name: str

    role: Literal["admin", "member"]
