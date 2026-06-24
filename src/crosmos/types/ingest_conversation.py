# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestConversation"]


class IngestConversation(BaseModel):
    job_id: str

    source_id: str

    status: Literal["pending"]
