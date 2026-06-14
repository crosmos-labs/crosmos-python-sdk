# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceVisibility"]


class SourceVisibility(BaseModel):
    id: str

    edges_updated: int
    """Derived edges re-classified"""

    memories_updated: int
    """Derived memories re-classified"""

    visibility: Literal["private", "org"]
