# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Member"]


class Member(BaseModel):
    email: str

    joined_at: datetime

    name: str

    role: Literal["owner", "admin", "member"]

    user_id: str
