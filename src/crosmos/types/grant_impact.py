# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .visible_principal import VisiblePrincipal

__all__ = ["GrantImpact"]


class GrantImpact(BaseModel):
    newly_visible: List[VisiblePrincipal]
    """The transitive set of users this grant would newly expose to the viewer group."""

    subject_group_id: str

    viewer_group_id: str
