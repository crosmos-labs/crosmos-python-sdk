# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import date
from typing_extensions import Literal

from .._models import BaseModel
from .usage_metric import UsageMetric

__all__ = ["Usage"]


class Usage(BaseModel):
    period_end: date

    period_start: date

    plan: Literal["free", "developer", "pro", "enterprise"]

    queries: UsageMetric

    rate_limit_per_day: int

    rate_limit_rpm: int

    spaces: UsageMetric

    tokens: UsageMetric
