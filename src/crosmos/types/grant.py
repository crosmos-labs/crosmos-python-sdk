# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Grant"]


class Grant(BaseModel):
    id: str

    created_at: datetime

    subject_group_id: str

    subject_group_slug: str

    viewer_group_id: str

    viewer_group_slug: str
