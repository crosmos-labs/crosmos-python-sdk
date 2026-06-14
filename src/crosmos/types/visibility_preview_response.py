# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .visible_principal import VisiblePrincipal

__all__ = ["VisibilityPreviewResponse"]


class VisibilityPreviewResponse(BaseModel):
    user_id: str

    visibility_enabled: bool

    visible_users: List[VisiblePrincipal]
