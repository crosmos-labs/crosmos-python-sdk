# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import date

from .._models import BaseModel

__all__ = ["Usage", "Queries", "Spaces", "Tokens"]


class Queries(BaseModel):
    """Used / limit / remaining triple. ``-1`` limit means unlimited."""

    limit: int

    remaining: int

    used: int


class Spaces(BaseModel):
    """Used / limit / remaining triple. ``-1`` limit means unlimited."""

    limit: int

    remaining: int

    used: int


class Tokens(BaseModel):
    """Used / limit / remaining triple. ``-1`` limit means unlimited."""

    limit: int

    remaining: int

    used: int


class Usage(BaseModel):
    """Aggregated org-level usage and current plan limits."""

    period_end: date

    period_start: date

    plan: str

    queries: Queries
    """Used / limit / remaining triple. `-1` limit means unlimited."""

    rate_limit_per_day: int

    rate_limit_rpm: int

    spaces: Spaces
    """Used / limit / remaining triple. `-1` limit means unlimited."""

    tokens: Tokens
    """Used / limit / remaining triple. `-1` limit means unlimited."""
