# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from crosmos import Crosmos, AsyncCrosmos
from tests.utils import assert_matches_type
from crosmos.types import (
    Grant,
    Group,
    GrantList,
    GroupList,
    GrantImpact,
    GroupMemberList,
    VisibilitySettings,
    VisibilityPreviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

org_uuid = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"


class TestVisibility:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_group(self, client: Crosmos) -> None:
        visibility = client.visibility.create_group(org_uuid, name="x")
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_group_with_all_params(self, client: Crosmos) -> None:
        visibility = client.visibility.create_group(org_uuid, name="x", slug="slug")
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_groups(self, client: Crosmos) -> None:
        visibility = client.visibility.list_groups(org_uuid)
        assert_matches_type(GroupList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_group(self, client: Crosmos) -> None:
        visibility = client.visibility.update_group(group_uuid=org_uuid, org_uuid=org_uuid)
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_group(self, client: Crosmos) -> None:
        visibility = client.visibility.delete_group(group_uuid=org_uuid, org_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_group_members(self, client: Crosmos) -> None:
        visibility = client.visibility.list_group_members(group_uuid=org_uuid, org_uuid=org_uuid)
        assert_matches_type(GroupMemberList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_group_member(self, client: Crosmos) -> None:
        visibility = client.visibility.add_group_member(user_uuid=org_uuid, org_uuid=org_uuid, group_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_group_member(self, client: Crosmos) -> None:
        visibility = client.visibility.remove_group_member(user_uuid=org_uuid, org_uuid=org_uuid, group_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_grant(self, client: Crosmos) -> None:
        visibility = client.visibility.create_grant(org_uuid, subject_group_id=org_uuid, viewer_group_id=org_uuid)
        assert_matches_type(Grant, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_grants(self, client: Crosmos) -> None:
        visibility = client.visibility.list_grants(org_uuid)
        assert_matches_type(GrantList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview_grant(self, client: Crosmos) -> None:
        visibility = client.visibility.preview_grant(org_uuid, subject_group_id=org_uuid, viewer_group_id=org_uuid)
        assert_matches_type(GrantImpact, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_grant(self, client: Crosmos) -> None:
        visibility = client.visibility.delete_grant(grant_uuid=org_uuid, org_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: Crosmos) -> None:
        visibility = client.visibility.preview(org_uuid, user_id=org_uuid)
        assert_matches_type(VisibilityPreviewResponse, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: Crosmos) -> None:
        visibility = client.visibility.update_settings(org_uuid, enabled=True)
        assert_matches_type(VisibilitySettings, visibility, path=["response"])


class TestAsyncVisibility:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_group(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.create_group(org_uuid, name="x")
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_group_with_all_params(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.create_group(org_uuid, name="x", slug="slug")
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_groups(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.list_groups(org_uuid)
        assert_matches_type(GroupList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_group(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.update_group(group_uuid=org_uuid, org_uuid=org_uuid)
        assert_matches_type(Group, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_group(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.delete_group(group_uuid=org_uuid, org_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_group_members(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.list_group_members(group_uuid=org_uuid, org_uuid=org_uuid)
        assert_matches_type(GroupMemberList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_group_member(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.add_group_member(
            user_uuid=org_uuid, org_uuid=org_uuid, group_uuid=org_uuid
        )
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_group_member(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.remove_group_member(
            user_uuid=org_uuid, org_uuid=org_uuid, group_uuid=org_uuid
        )
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_grant(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.create_grant(
            org_uuid, subject_group_id=org_uuid, viewer_group_id=org_uuid
        )
        assert_matches_type(Grant, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_grants(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.list_grants(org_uuid)
        assert_matches_type(GrantList, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview_grant(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.preview_grant(
            org_uuid, subject_group_id=org_uuid, viewer_group_id=org_uuid
        )
        assert_matches_type(GrantImpact, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_grant(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.delete_grant(grant_uuid=org_uuid, org_uuid=org_uuid)
        assert visibility is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.preview(org_uuid, user_id=org_uuid)
        assert_matches_type(VisibilityPreviewResponse, visibility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncCrosmos) -> None:
        visibility = await async_client.visibility.update_settings(org_uuid, enabled=True)
        assert_matches_type(VisibilitySettings, visibility, path=["response"])
