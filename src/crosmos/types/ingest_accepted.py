# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestAccepted", "Job"]


class Job(BaseModel):
    job_id: str

    source_ids: List[str]


class IngestAccepted(BaseModel):
    job_id: str

    jobs: List[Job]
    """One entry per job the request was split into."""

    source_ids: List[str]

    status: Literal["pending"]
