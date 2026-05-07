# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import source_get_params, source_list_params, source_delete_params, source_ingest_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.source import Source
from ..types.source_list import SourceList
from ..types.ingest_accepted import IngestAccepted

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-ts-sdk#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-ts-sdk#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        content_type: Optional[str] | Omit = omit,
        extraction_status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        space_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceList:
        """
        List sources in the caller's org, sorted by created_at desc.

        If space_id is provided, returns only sources in that space. Otherwise, returns
        sources across all spaces in the org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_type": content_type,
                        "extraction_status": extraction_status,
                        "limit": limit,
                        "offset": offset,
                        "space_id": space_id,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceList,
        )

    def delete(
        self,
        source_uuid: str,
        *,
        space_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a source document by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_uuid:
            raise ValueError(f"Expected a non-empty value for `source_uuid` but received {source_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/sources/{source_uuid}", source_uuid=source_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"space_uuid": space_uuid}, source_delete_params.SourceDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        source_uuid: str,
        *,
        space_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Get a source by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_uuid:
            raise ValueError(f"Expected a non-empty value for `source_uuid` but received {source_uuid!r}")
        return self._get(
            path_template("/api/v1/sources/{source_uuid}", source_uuid=source_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"space_uuid": space_uuid}, source_get_params.SourceGetParams),
            ),
            cast_to=Source,
        )

    def ingest(
        self,
        *,
        sources: Iterable[source_ingest_params.Source],
        space_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestAccepted:
        """Upload raw content sources for ingestion into the knowledge graph.

        Each source
        is a discrete content payload (text, markdown.) that will be processed by the
        extraction pipeline.

        Args:
          sources: Array of source payloads to ingest

          space_id: Memory space to ingest into

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/sources",
            body=maybe_transform(
                {
                    "sources": sources,
                    "space_id": space_id,
                },
                source_ingest_params.SourceIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestAccepted,
        )


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-ts-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-ts-sdk#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        content_type: Optional[str] | Omit = omit,
        extraction_status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        space_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceList:
        """
        List sources in the caller's org, sorted by created_at desc.

        If space_id is provided, returns only sources in that space. Otherwise, returns
        sources across all spaces in the org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_type": content_type,
                        "extraction_status": extraction_status,
                        "limit": limit,
                        "offset": offset,
                        "space_id": space_id,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceList,
        )

    async def delete(
        self,
        source_uuid: str,
        *,
        space_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a source document by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_uuid:
            raise ValueError(f"Expected a non-empty value for `source_uuid` but received {source_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/sources/{source_uuid}", source_uuid=source_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"space_uuid": space_uuid}, source_delete_params.SourceDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        source_uuid: str,
        *,
        space_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Get a source by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_uuid:
            raise ValueError(f"Expected a non-empty value for `source_uuid` but received {source_uuid!r}")
        return await self._get(
            path_template("/api/v1/sources/{source_uuid}", source_uuid=source_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"space_uuid": space_uuid}, source_get_params.SourceGetParams),
            ),
            cast_to=Source,
        )

    async def ingest(
        self,
        *,
        sources: Iterable[source_ingest_params.Source],
        space_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestAccepted:
        """Upload raw content sources for ingestion into the knowledge graph.

        Each source
        is a discrete content payload (text, markdown.) that will be processed by the
        extraction pipeline.

        Args:
          sources: Array of source payloads to ingest

          space_id: Memory space to ingest into

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/sources",
            body=await async_maybe_transform(
                {
                    "sources": sources,
                    "space_id": space_id,
                },
                source_ingest_params.SourceIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestAccepted,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.delete = to_raw_response_wrapper(
            sources.delete,
        )
        self.get = to_raw_response_wrapper(
            sources.get,
        )
        self.ingest = to_raw_response_wrapper(
            sources.ingest,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sources.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sources.get,
        )
        self.ingest = async_to_raw_response_wrapper(
            sources.ingest,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            sources.delete,
        )
        self.get = to_streamed_response_wrapper(
            sources.get,
        )
        self.ingest = to_streamed_response_wrapper(
            sources.ingest,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sources.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sources.get,
        )
        self.ingest = async_to_streamed_response_wrapper(
            sources.ingest,
        )
