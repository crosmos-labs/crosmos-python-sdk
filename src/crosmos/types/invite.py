# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Invite"]


class Invite(BaseModel):
    id: str

    email: str

    expires_at: datetime

    invited_by: str

    role: Literal["admin", "member"]

    status: Literal["pending", "expired", "accepted"]
