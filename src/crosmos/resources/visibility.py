# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    visibility_preview_params,
    visibility_create_grant_params,
    visibility_create_group_params,
    visibility_update_group_params,
    visibility_update_settings_params,
)
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
from ..types.grant import Grant
from ..types.group import Group
from .._base_client import make_request_options
from ..types.grant_list import GrantList
from ..types.group_list import GroupList
from ..types.grant_impact import GrantImpact
from ..types.group_member_list import GroupMemberList
from ..types.visibility_settings import VisibilitySettings
from ..types.visibility_preview_response import VisibilityPreviewResponse

__all__ = ["VisibilityResource", "AsyncVisibilityResource"]


class VisibilityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VisibilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return VisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisibilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return VisibilityResourceWithStreamingResponse(self)

    def create_group(
        self,
        org_uuid: str,
        *,
        name: str,
        slug: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a visibility group within an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/groups", org_uuid=org_uuid),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                visibility_create_group_params.VisibilityCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def list_groups(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupList:
        """
        List visibility groups in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/groups", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupList,
        )

    def update_group(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        name: Optional[str] | Omit = omit,
        slug: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Rename a visibility group or change its slug.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        return self._patch(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}", org_uuid=org_uuid, group_uuid=group_uuid
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                visibility_update_group_params.VisibilityUpdateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def delete_group(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}", org_uuid=org_uuid, group_uuid=group_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_group_members(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMemberList:
        """
        List the members of a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        return self._get(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMemberList,
        )

    def add_group_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        group_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a user to a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
                user_uuid=user_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_group_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        group_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user from a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
                user_uuid=user_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_grant(
        self,
        org_uuid: str,
        *,
        subject_group_id: str,
        viewer_group_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """Create a grant: members of the viewer group can read memories owned by members
        of the subject group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants", org_uuid=org_uuid),
            body=maybe_transform(
                {
                    "subject_group_id": subject_group_id,
                    "viewer_group_id": viewer_group_id,
                },
                visibility_create_grant_params.VisibilityCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    def list_grants(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantList:
        """
        List visibility grants in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantList,
        )

    def preview_grant(
        self,
        org_uuid: str,
        *,
        subject_group_id: str,
        viewer_group_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantImpact:
        """Dry-run a proposed grant: returns the transitive set of users it would newly
        expose to the viewer group, without committing it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants/preview", org_uuid=org_uuid),
            body=maybe_transform(
                {
                    "subject_group_id": subject_group_id,
                    "viewer_group_id": viewer_group_id,
                },
                visibility_create_grant_params.VisibilityCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantImpact,
        )

    def delete_grant(
        self,
        grant_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a visibility grant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not grant_uuid:
            raise ValueError(f"Expected a non-empty value for `grant_uuid` but received {grant_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/grants/{grant_uuid}", org_uuid=org_uuid, grant_uuid=grant_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def preview(
        self,
        org_uuid: str,
        *,
        user_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilityPreviewResponse:
        """Preview which users a given user can see under the org's current visibility
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/preview", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, visibility_preview_params.VisibilityPreviewParams),
            ),
            cast_to=VisibilityPreviewResponse,
        )

    def update_settings(
        self,
        org_uuid: str,
        *,
        enabled: bool,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilitySettings:
        """
        Enable or disable the visibility graph for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._patch(
            path_template("/api/v1/orgs/{org_uuid}/visibility/settings", org_uuid=org_uuid),
            body=maybe_transform(
                {"enabled": enabled}, visibility_update_settings_params.VisibilityUpdateSettingsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibilitySettings,
        )


class AsyncVisibilityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVisibilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisibilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return AsyncVisibilityResourceWithStreamingResponse(self)

    async def create_group(
        self,
        org_uuid: str,
        *,
        name: str,
        slug: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a visibility group within an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/groups", org_uuid=org_uuid),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                visibility_create_group_params.VisibilityCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def list_groups(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupList:
        """
        List visibility groups in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/groups", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupList,
        )

    async def update_group(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        name: Optional[str] | Omit = omit,
        slug: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Rename a visibility group or change its slug.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        return await self._patch(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}", org_uuid=org_uuid, group_uuid=group_uuid
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                visibility_update_group_params.VisibilityUpdateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def delete_group(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}", org_uuid=org_uuid, group_uuid=group_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_group_members(
        self,
        group_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMemberList:
        """
        List the members of a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        return await self._get(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMemberList,
        )

    async def add_group_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        group_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a user to a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
                user_uuid=user_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_group_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        group_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user from a visibility group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not group_uuid:
            raise ValueError(f"Expected a non-empty value for `group_uuid` but received {group_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}",
                org_uuid=org_uuid,
                group_uuid=group_uuid,
                user_uuid=user_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_grant(
        self,
        org_uuid: str,
        *,
        subject_group_id: str,
        viewer_group_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Grant:
        """Create a grant: members of the viewer group can read memories owned by members
        of the subject group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants", org_uuid=org_uuid),
            body=await async_maybe_transform(
                {
                    "subject_group_id": subject_group_id,
                    "viewer_group_id": viewer_group_id,
                },
                visibility_create_grant_params.VisibilityCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grant,
        )

    async def list_grants(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantList:
        """
        List visibility grants in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantList,
        )

    async def preview_grant(
        self,
        org_uuid: str,
        *,
        subject_group_id: str,
        viewer_group_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantImpact:
        """Dry-run a proposed grant: returns the transitive set of users it would newly
        expose to the viewer group, without committing it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._post(
            path_template("/api/v1/orgs/{org_uuid}/visibility/grants/preview", org_uuid=org_uuid),
            body=await async_maybe_transform(
                {
                    "subject_group_id": subject_group_id,
                    "viewer_group_id": viewer_group_id,
                },
                visibility_create_grant_params.VisibilityCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantImpact,
        )

    async def delete_grant(
        self,
        grant_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a visibility grant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not grant_uuid:
            raise ValueError(f"Expected a non-empty value for `grant_uuid` but received {grant_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/orgs/{org_uuid}/visibility/grants/{grant_uuid}", org_uuid=org_uuid, grant_uuid=grant_uuid
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def preview(
        self,
        org_uuid: str,
        *,
        user_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilityPreviewResponse:
        """Preview which users a given user can see under the org's current visibility
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._get(
            path_template("/api/v1/orgs/{org_uuid}/visibility/preview", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, visibility_preview_params.VisibilityPreviewParams
                ),
            ),
            cast_to=VisibilityPreviewResponse,
        )

    async def update_settings(
        self,
        org_uuid: str,
        *,
        enabled: bool,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilitySettings:
        """
        Enable or disable the visibility graph for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._patch(
            path_template("/api/v1/orgs/{org_uuid}/visibility/settings", org_uuid=org_uuid),
            body=await async_maybe_transform(
                {"enabled": enabled}, visibility_update_settings_params.VisibilityUpdateSettingsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibilitySettings,
        )


class VisibilityResourceWithRawResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.create_group = to_raw_response_wrapper(
            visibility.create_group,
        )
        self.list_groups = to_raw_response_wrapper(
            visibility.list_groups,
        )
        self.update_group = to_raw_response_wrapper(
            visibility.update_group,
        )
        self.delete_group = to_raw_response_wrapper(
            visibility.delete_group,
        )
        self.list_group_members = to_raw_response_wrapper(
            visibility.list_group_members,
        )
        self.add_group_member = to_raw_response_wrapper(
            visibility.add_group_member,
        )
        self.remove_group_member = to_raw_response_wrapper(
            visibility.remove_group_member,
        )
        self.create_grant = to_raw_response_wrapper(
            visibility.create_grant,
        )
        self.list_grants = to_raw_response_wrapper(
            visibility.list_grants,
        )
        self.preview_grant = to_raw_response_wrapper(
            visibility.preview_grant,
        )
        self.delete_grant = to_raw_response_wrapper(
            visibility.delete_grant,
        )
        self.preview = to_raw_response_wrapper(
            visibility.preview,
        )
        self.update_settings = to_raw_response_wrapper(
            visibility.update_settings,
        )


class AsyncVisibilityResourceWithRawResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.create_group = async_to_raw_response_wrapper(
            visibility.create_group,
        )
        self.list_groups = async_to_raw_response_wrapper(
            visibility.list_groups,
        )
        self.update_group = async_to_raw_response_wrapper(
            visibility.update_group,
        )
        self.delete_group = async_to_raw_response_wrapper(
            visibility.delete_group,
        )
        self.list_group_members = async_to_raw_response_wrapper(
            visibility.list_group_members,
        )
        self.add_group_member = async_to_raw_response_wrapper(
            visibility.add_group_member,
        )
        self.remove_group_member = async_to_raw_response_wrapper(
            visibility.remove_group_member,
        )
        self.create_grant = async_to_raw_response_wrapper(
            visibility.create_grant,
        )
        self.list_grants = async_to_raw_response_wrapper(
            visibility.list_grants,
        )
        self.preview_grant = async_to_raw_response_wrapper(
            visibility.preview_grant,
        )
        self.delete_grant = async_to_raw_response_wrapper(
            visibility.delete_grant,
        )
        self.preview = async_to_raw_response_wrapper(
            visibility.preview,
        )
        self.update_settings = async_to_raw_response_wrapper(
            visibility.update_settings,
        )


class VisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.create_group = to_streamed_response_wrapper(
            visibility.create_group,
        )
        self.list_groups = to_streamed_response_wrapper(
            visibility.list_groups,
        )
        self.update_group = to_streamed_response_wrapper(
            visibility.update_group,
        )
        self.delete_group = to_streamed_response_wrapper(
            visibility.delete_group,
        )
        self.list_group_members = to_streamed_response_wrapper(
            visibility.list_group_members,
        )
        self.add_group_member = to_streamed_response_wrapper(
            visibility.add_group_member,
        )
        self.remove_group_member = to_streamed_response_wrapper(
            visibility.remove_group_member,
        )
        self.create_grant = to_streamed_response_wrapper(
            visibility.create_grant,
        )
        self.list_grants = to_streamed_response_wrapper(
            visibility.list_grants,
        )
        self.preview_grant = to_streamed_response_wrapper(
            visibility.preview_grant,
        )
        self.delete_grant = to_streamed_response_wrapper(
            visibility.delete_grant,
        )
        self.preview = to_streamed_response_wrapper(
            visibility.preview,
        )
        self.update_settings = to_streamed_response_wrapper(
            visibility.update_settings,
        )


class AsyncVisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.create_group = async_to_streamed_response_wrapper(
            visibility.create_group,
        )
        self.list_groups = async_to_streamed_response_wrapper(
            visibility.list_groups,
        )
        self.update_group = async_to_streamed_response_wrapper(
            visibility.update_group,
        )
        self.delete_group = async_to_streamed_response_wrapper(
            visibility.delete_group,
        )
        self.list_group_members = async_to_streamed_response_wrapper(
            visibility.list_group_members,
        )
        self.add_group_member = async_to_streamed_response_wrapper(
            visibility.add_group_member,
        )
        self.remove_group_member = async_to_streamed_response_wrapper(
            visibility.remove_group_member,
        )
        self.create_grant = async_to_streamed_response_wrapper(
            visibility.create_grant,
        )
        self.list_grants = async_to_streamed_response_wrapper(
            visibility.list_grants,
        )
        self.preview_grant = async_to_streamed_response_wrapper(
            visibility.preview_grant,
        )
        self.delete_grant = async_to_streamed_response_wrapper(
            visibility.delete_grant,
        )
        self.preview = async_to_streamed_response_wrapper(
            visibility.preview,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            visibility.update_settings,
        )
