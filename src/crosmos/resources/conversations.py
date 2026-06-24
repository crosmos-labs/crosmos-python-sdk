# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import conversation_ingest_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ingest_conversation import IngestConversation

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def ingest(
        self,
        *,
        messages: Iterable[conversation_ingest_params.Message],
        space_id: str,
        meta: Optional[Dict[str, Optional[object]]] | Omit = omit,
        session_date: str | Omit = omit,
        session_id: str | Omit = omit,
        visibility: Literal["private", "org"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestConversation:
        """Ingest a multi-turn conversation.

        The conversation is stored as a single source
        and segmented at ingestion into windows of 4 turns; each window is extracted
        independently with the prior window as lookback context for pronoun resolution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/conversations",
            body=maybe_transform(
                {
                    "messages": messages,
                    "space_id": space_id,
                    "meta": meta,
                    "session_date": session_date,
                    "session_id": session_id,
                    "visibility": visibility,
                },
                conversation_ingest_params.ConversationIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestConversation,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def ingest(
        self,
        *,
        messages: Iterable[conversation_ingest_params.Message],
        space_id: str,
        meta: Optional[Dict[str, Optional[object]]] | Omit = omit,
        session_date: str | Omit = omit,
        session_id: str | Omit = omit,
        visibility: Literal["private", "org"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestConversation:
        """Ingest a multi-turn conversation.

        The conversation is stored as a single source
        and segmented at ingestion into windows of 4 turns; each window is extracted
        independently with the prior window as lookback context for pronoun resolution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/conversations",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "space_id": space_id,
                    "meta": meta,
                    "session_date": session_date,
                    "session_id": session_id,
                    "visibility": visibility,
                },
                conversation_ingest_params.ConversationIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestConversation,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.ingest = to_raw_response_wrapper(
            conversations.ingest,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.ingest = async_to_raw_response_wrapper(
            conversations.ingest,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.ingest = to_streamed_response_wrapper(
            conversations.ingest,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.ingest = async_to_streamed_response_wrapper(
            conversations.ingest,
        )
