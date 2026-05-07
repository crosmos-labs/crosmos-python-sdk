# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["IngestConversation"]


class IngestConversation(BaseModel):
    job_id: str

    source_ids: List[str]

    status: Optional[str] = None
