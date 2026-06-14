# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    org_list_params,
    org_set_active_params,
    org_accept_invite_params,
    org_create_invite_params,
    org_update_member_params,
    org_preview_invite_params,
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
from .._base_client import make_request_options
from ..types.invite import Invite
from ..types.member import Member
from ..types.invite_list import InviteList
from ..types.member_list import MemberList
from ..types.accept_invite import AcceptInvite
from ..types.invite_preview import InvitePreview
from ..types.set_active_org import SetActiveOrg
from ..types.org_list_response import OrgListResponse

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListResponse:
        """
        List the organizations the caller is a member of.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/orgs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, org_list_params.OrgListParams),
            ),
            cast_to=OrgListResponse,
        )

    def set_active(
        self,
        *,
        org_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetActiveOrg:
        """Switch the session's active organization.

        Returns a re-minted access token; the org-agnostic refresh token is unchanged,
        so clients swap only the access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/active-org",
            body=maybe_transform({"org_id": org_id}, org_set_active_params.OrgSetActiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetActiveOrg,
        )

    def list_members(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberList:
        """
        List members of an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._get(
            path_template("/api/v1/orgs/{org_uuid}/members", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberList,
        )

    def update_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        role: Literal["admin", "member"],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Member:
        """
        Update a member's role within an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        return self._patch(
            path_template("/api/v1/orgs/{org_uuid}/members/{user_uuid}", org_uuid=org_uuid, user_uuid=user_uuid),
            body=maybe_transform({"role": role}, org_update_member_params.OrgUpdateMemberParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Member,
        )

    def delete_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a member from an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/orgs/{org_uuid}/members/{user_uuid}", org_uuid=org_uuid, user_uuid=user_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_invite(
        self,
        org_uuid: str,
        *,
        email: str,
        role: Literal["admin", "member"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invite:
        """
        Invite a user to an organization by email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._post(
            path_template("/api/v1/orgs/{org_uuid}/invites", org_uuid=org_uuid),
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                org_create_invite_params.OrgCreateInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    def list_invites(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteList:
        """
        List pending invites for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return self._get(
            path_template("/api/v1/orgs/{org_uuid}/invites", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteList,
        )

    def revoke_invite(
        self,
        invite_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke a pending invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not invite_uuid:
            raise ValueError(f"Expected a non-empty value for `invite_uuid` but received {invite_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/orgs/{org_uuid}/invites/{invite_uuid}", org_uuid=org_uuid, invite_uuid=invite_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def accept_invite(
        self,
        *,
        token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AcceptInvite:
        """Accept an organization invite by token.

        The caller joins the org with the invited role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/orgs/invites/accept",
            body=maybe_transform({"token": token}, org_accept_invite_params.OrgAcceptInviteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AcceptInvite,
        )

    def preview_invite(
        self,
        *,
        token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitePreview:
        """
        Preview an invite (org name, inviter, role) without accepting it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/orgs/invites/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"token": token}, org_preview_invite_params.OrgPreviewInviteParams),
            ),
            cast_to=InvitePreview,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/crosmos-labs/crosmos-python-sdk#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListResponse:
        """
        List the organizations the caller is a member of.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/orgs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, org_list_params.OrgListParams),
            ),
            cast_to=OrgListResponse,
        )

    async def set_active(
        self,
        *,
        org_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetActiveOrg:
        """Switch the session's active organization.

        Returns a re-minted access token; the org-agnostic refresh token is unchanged,
        so clients swap only the access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/active-org",
            body=await async_maybe_transform({"org_id": org_id}, org_set_active_params.OrgSetActiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetActiveOrg,
        )

    async def list_members(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberList:
        """
        List members of an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._get(
            path_template("/api/v1/orgs/{org_uuid}/members", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberList,
        )

    async def update_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        role: Literal["admin", "member"],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Member:
        """
        Update a member's role within an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        return await self._patch(
            path_template("/api/v1/orgs/{org_uuid}/members/{user_uuid}", org_uuid=org_uuid, user_uuid=user_uuid),
            body=await async_maybe_transform({"role": role}, org_update_member_params.OrgUpdateMemberParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Member,
        )

    async def delete_member(
        self,
        user_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a member from an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not user_uuid:
            raise ValueError(f"Expected a non-empty value for `user_uuid` but received {user_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/orgs/{org_uuid}/members/{user_uuid}", org_uuid=org_uuid, user_uuid=user_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_invite(
        self,
        org_uuid: str,
        *,
        email: str,
        role: Literal["admin", "member"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invite:
        """
        Invite a user to an organization by email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._post(
            path_template("/api/v1/orgs/{org_uuid}/invites", org_uuid=org_uuid),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                org_create_invite_params.OrgCreateInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    async def list_invites(
        self,
        org_uuid: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteList:
        """
        List pending invites for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        return await self._get(
            path_template("/api/v1/orgs/{org_uuid}/invites", org_uuid=org_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteList,
        )

    async def revoke_invite(
        self,
        invite_uuid: str,
        *,
        org_uuid: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke a pending invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_uuid:
            raise ValueError(f"Expected a non-empty value for `org_uuid` but received {org_uuid!r}")
        if not invite_uuid:
            raise ValueError(f"Expected a non-empty value for `invite_uuid` but received {invite_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/orgs/{org_uuid}/invites/{invite_uuid}", org_uuid=org_uuid, invite_uuid=invite_uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def accept_invite(
        self,
        *,
        token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AcceptInvite:
        """Accept an organization invite by token.

        The caller joins the org with the invited role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/orgs/invites/accept",
            body=await async_maybe_transform({"token": token}, org_accept_invite_params.OrgAcceptInviteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AcceptInvite,
        )

    async def preview_invite(
        self,
        *,
        token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitePreview:
        """
        Preview an invite (org name, inviter, role) without accepting it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/orgs/invites/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"token": token}, org_preview_invite_params.OrgPreviewInviteParams),
            ),
            cast_to=InvitePreview,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.list = to_raw_response_wrapper(
            orgs.list,
        )
        self.set_active = to_raw_response_wrapper(
            orgs.set_active,
        )
        self.list_members = to_raw_response_wrapper(
            orgs.list_members,
        )
        self.update_member = to_raw_response_wrapper(
            orgs.update_member,
        )
        self.delete_member = to_raw_response_wrapper(
            orgs.delete_member,
        )
        self.create_invite = to_raw_response_wrapper(
            orgs.create_invite,
        )
        self.list_invites = to_raw_response_wrapper(
            orgs.list_invites,
        )
        self.revoke_invite = to_raw_response_wrapper(
            orgs.revoke_invite,
        )
        self.accept_invite = to_raw_response_wrapper(
            orgs.accept_invite,
        )
        self.preview_invite = to_raw_response_wrapper(
            orgs.preview_invite,
        )


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.list = async_to_raw_response_wrapper(
            orgs.list,
        )
        self.set_active = async_to_raw_response_wrapper(
            orgs.set_active,
        )
        self.list_members = async_to_raw_response_wrapper(
            orgs.list_members,
        )
        self.update_member = async_to_raw_response_wrapper(
            orgs.update_member,
        )
        self.delete_member = async_to_raw_response_wrapper(
            orgs.delete_member,
        )
        self.create_invite = async_to_raw_response_wrapper(
            orgs.create_invite,
        )
        self.list_invites = async_to_raw_response_wrapper(
            orgs.list_invites,
        )
        self.revoke_invite = async_to_raw_response_wrapper(
            orgs.revoke_invite,
        )
        self.accept_invite = async_to_raw_response_wrapper(
            orgs.accept_invite,
        )
        self.preview_invite = async_to_raw_response_wrapper(
            orgs.preview_invite,
        )


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.list = to_streamed_response_wrapper(
            orgs.list,
        )
        self.set_active = to_streamed_response_wrapper(
            orgs.set_active,
        )
        self.list_members = to_streamed_response_wrapper(
            orgs.list_members,
        )
        self.update_member = to_streamed_response_wrapper(
            orgs.update_member,
        )
        self.delete_member = to_streamed_response_wrapper(
            orgs.delete_member,
        )
        self.create_invite = to_streamed_response_wrapper(
            orgs.create_invite,
        )
        self.list_invites = to_streamed_response_wrapper(
            orgs.list_invites,
        )
        self.revoke_invite = to_streamed_response_wrapper(
            orgs.revoke_invite,
        )
        self.accept_invite = to_streamed_response_wrapper(
            orgs.accept_invite,
        )
        self.preview_invite = to_streamed_response_wrapper(
            orgs.preview_invite,
        )


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.list = async_to_streamed_response_wrapper(
            orgs.list,
        )
        self.set_active = async_to_streamed_response_wrapper(
            orgs.set_active,
        )
        self.list_members = async_to_streamed_response_wrapper(
            orgs.list_members,
        )
        self.update_member = async_to_streamed_response_wrapper(
            orgs.update_member,
        )
        self.delete_member = async_to_streamed_response_wrapper(
            orgs.delete_member,
        )
        self.create_invite = async_to_streamed_response_wrapper(
            orgs.create_invite,
        )
        self.list_invites = async_to_streamed_response_wrapper(
            orgs.list_invites,
        )
        self.revoke_invite = async_to_streamed_response_wrapper(
            orgs.revoke_invite,
        )
        self.accept_invite = async_to_streamed_response_wrapper(
            orgs.accept_invite,
        )
        self.preview_invite = async_to_streamed_response_wrapper(
            orgs.preview_invite,
        )
