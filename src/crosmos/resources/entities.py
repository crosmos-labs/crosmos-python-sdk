# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import entity_get_params, entity_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.entity_list import EntityList
from ..types.entity_detail import EntityDetail

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        entity_type: str | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        q: str | Omit = omit,
        sort_by: Literal["name", "edge_count", "created_at"] | Omit = omit,
        space_id: str | Omit = omit,
        space_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityList:
        """
        List entities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_type": entity_type,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "q": q,
                        "sort_by": sort_by,
                        "space_id": space_id,
                        "space_uuid": space_uuid,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=EntityList,
        )

    def get(
        self,
        entity_uuid: str,
        *,
        space_id: str | Omit = omit,
        space_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityDetail:
        """
        Get entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_uuid:
            raise ValueError(f"Expected a non-empty value for `entity_uuid` but received {entity_uuid!r}")
        return self._get(
            path_template("/api/v1/entities/{entity_uuid}", entity_uuid=entity_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "space_id": space_id,
                        "space_uuid": space_uuid,
                    },
                    entity_get_params.EntityGetParams,
                ),
            ),
            cast_to=EntityDetail,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        entity_type: str | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        q: str | Omit = omit,
        sort_by: Literal["name", "edge_count", "created_at"] | Omit = omit,
        space_id: str | Omit = omit,
        space_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityList:
        """
        List entities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_type": entity_type,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "q": q,
                        "sort_by": sort_by,
                        "space_id": space_id,
                        "space_uuid": space_uuid,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=EntityList,
        )

    async def get(
        self,
        entity_uuid: str,
        *,
        space_id: str | Omit = omit,
        space_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityDetail:
        """
        Get entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_uuid:
            raise ValueError(f"Expected a non-empty value for `entity_uuid` but received {entity_uuid!r}")
        return await self._get(
            path_template("/api/v1/entities/{entity_uuid}", entity_uuid=entity_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "space_id": space_id,
                        "space_uuid": space_uuid,
                    },
                    entity_get_params.EntityGetParams,
                ),
            ),
            cast_to=EntityDetail,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.get = to_raw_response_wrapper(
            entities.get,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.get = async_to_raw_response_wrapper(
            entities.get,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.get = to_streamed_response_wrapper(
            entities.get,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.get = async_to_streamed_response_wrapper(
            entities.get,
        )
