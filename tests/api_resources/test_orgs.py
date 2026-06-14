# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from crosmos import Crosmos, AsyncCrosmos
from tests.utils import assert_matches_type
from crosmos.types import (
    Invite,
    Member,
    InviteList,
    MemberList,
    AcceptInvite,
    SetActiveOrg,
    InvitePreview,
    OrgListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

org_uuid = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"


class TestOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Crosmos) -> None:
        org = client.orgs.list()
        assert_matches_type(OrgListResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Crosmos) -> None:
        org = client.orgs.list(limit=1)
        assert_matches_type(OrgListResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_active(self, client: Crosmos) -> None:
        org = client.orgs.set_active(org_id=org_uuid)
        assert_matches_type(SetActiveOrg, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_members(self, client: Crosmos) -> None:
        org = client.orgs.list_members(org_uuid)
        assert_matches_type(MemberList, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_member(self, client: Crosmos) -> None:
        org = client.orgs.update_member(user_uuid=org_uuid, org_uuid=org_uuid, role="admin")
        assert_matches_type(Member, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_member(self, client: Crosmos) -> None:
        org = client.orgs.delete_member(user_uuid=org_uuid, org_uuid=org_uuid)
        assert org is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_invite(self, client: Crosmos) -> None:
        org = client.orgs.create_invite(org_uuid, email="dev@stainless.com")
        assert_matches_type(Invite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_invite_with_all_params(self, client: Crosmos) -> None:
        org = client.orgs.create_invite(org_uuid, email="dev@stainless.com", role="admin")
        assert_matches_type(Invite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_invites(self, client: Crosmos) -> None:
        org = client.orgs.list_invites(org_uuid)
        assert_matches_type(InviteList, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_invite(self, client: Crosmos) -> None:
        org = client.orgs.revoke_invite(invite_uuid=org_uuid, org_uuid=org_uuid)
        assert org is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept_invite(self, client: Crosmos) -> None:
        org = client.orgs.accept_invite(token="xxxxxxxxxxxxxxxxxxxx")
        assert_matches_type(AcceptInvite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview_invite(self, client: Crosmos) -> None:
        org = client.orgs.preview_invite(token="token")
        assert_matches_type(InvitePreview, org, path=["response"])


class TestAsyncOrgs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.list()
        assert_matches_type(OrgListResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.list(limit=1)
        assert_matches_type(OrgListResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_active(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.set_active(org_id=org_uuid)
        assert_matches_type(SetActiveOrg, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_members(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.list_members(org_uuid)
        assert_matches_type(MemberList, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_member(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.update_member(user_uuid=org_uuid, org_uuid=org_uuid, role="admin")
        assert_matches_type(Member, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_member(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.delete_member(user_uuid=org_uuid, org_uuid=org_uuid)
        assert org is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_invite(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.create_invite(org_uuid, email="dev@stainless.com")
        assert_matches_type(Invite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_invite_with_all_params(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.create_invite(org_uuid, email="dev@stainless.com", role="admin")
        assert_matches_type(Invite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_invites(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.list_invites(org_uuid)
        assert_matches_type(InviteList, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_invite(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.revoke_invite(invite_uuid=org_uuid, org_uuid=org_uuid)
        assert org is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept_invite(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.accept_invite(token="xxxxxxxxxxxxxxxxxxxx")
        assert_matches_type(AcceptInvite, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview_invite(self, async_client: AsyncCrosmos) -> None:
        org = await async_client.orgs.preview_invite(token="token")
        assert_matches_type(InvitePreview, org, path=["response"])
