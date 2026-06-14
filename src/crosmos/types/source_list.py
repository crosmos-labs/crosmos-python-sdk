# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .source import Source
from .._models import BaseModel

__all__ = ["SourceList", "SourcesUnionMember0"]


class SourcesUnionMember0(BaseModel):
    id: str

    content_type: str

    created_at: datetime

    extraction_status: str

    space_id: str

    token_count: int

    updated_at: datetime

    content_preview: Optional[str] = None
    """First 200 chars of source content for list views"""

    meta: Optional[object] = None


class SourceList(BaseModel):
    count: int

    sources: Union[List[SourcesUnionMember0], List[Source]]

    total: Optional[int] = None
    """Total matching sources (for pagination)"""
