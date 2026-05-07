# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchHybridParams"]


class SearchHybridParams(TypedDict, total=False):
    query: Required[str]
    """The search query text"""

    space_id: Required[str]
    """The memory space to search within"""

    diversify: bool
    """Apply MMR diversity post-rerank. Enable for broad/summarization intents."""

    graph: bool
    """Include graph traversal signal. Disable for semantic + keyword only."""

    include_source: bool
    """Include original source text in results."""

    limit: int
    """Max number of results to return"""

    recency_bias: Optional[float]
    """Override recency weighting.

    0.0 disables recency, higher values favor recent memories.
    """

    rerank: bool
    """Apply cross-encoder reranking. Disable for lower latency."""
