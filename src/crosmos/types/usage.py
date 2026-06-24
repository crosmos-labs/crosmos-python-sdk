# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Usage", "Queries", "Spaces", "Tokens"]


class Queries(BaseModel):
    limit: int

    remaining: int

    used: int


class Spaces(BaseModel):
    limit: int

    remaining: int

    used: int


class Tokens(BaseModel):
    limit: int

    remaining: int

    used: int


class Usage(BaseModel):
    period_end: date

    period_start: date

    plan: Literal["free", "developer", "pro", "enterprise"]

    queries: Queries

    rate_limit_per_day: int

    rate_limit_rpm: int

    spaces: Spaces

    tokens: Tokens
