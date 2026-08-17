# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from crosmos import Crosmos, AsyncCrosmos
from tests.utils import assert_matches_type
from crosmos.types import (
    Source as TypesSource,
    IngestAccepted,
)
from crosmos.pagination import SyncSourcesOffsetPage, AsyncSourcesOffsetPage
from crosmos.types.source_list import Source as SourceListSource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Crosmos) -> None:
        source = client.sources.list()
        assert_matches_type(SyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Crosmos) -> None:
        source = client.sources.list(
            content_type="x",
            extraction_status="pending",
            limit=1,
            offset=0,
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Crosmos) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Crosmos) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SyncSourcesOffsetPage[SourceListSource], source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Crosmos) -> None:
        source = client.sources.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Crosmos) -> None:
        source = client.sources.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Crosmos) -> None:
        response = client.sources.with_raw_response.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Crosmos) -> None:
        with client.sources.with_streaming_response.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Crosmos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_uuid` but received ''"):
            client.sources.with_raw_response.delete(
                source_uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Crosmos) -> None:
        source = client.sources.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Crosmos) -> None:
        source = client.sources.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Crosmos) -> None:
        response = client.sources.with_raw_response.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Crosmos) -> None:
        with client.sources.with_streaming_response.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(TypesSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Crosmos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_uuid` but received ''"):
            client.sources.with_raw_response.get(
                source_uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest(self, client: Crosmos) -> None:
        source = client.sources.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IngestAccepted, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest(self, client: Crosmos) -> None:
        response = client.sources.with_raw_response.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(IngestAccepted, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest(self, client: Crosmos) -> None:
        with client.sources.with_streaming_response.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(IngestAccepted, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.list()
        assert_matches_type(AsyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.list(
            content_type="x",
            extraction_status="pending",
            limit=1,
            offset=0,
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCrosmos) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(AsyncSourcesOffsetPage[SourceListSource], source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCrosmos) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(AsyncSourcesOffsetPage[SourceListSource], source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCrosmos) -> None:
        response = await async_client.sources.with_raw_response.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCrosmos) -> None:
        async with async_client.sources.with_streaming_response.delete(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCrosmos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_uuid` but received ''"):
            await async_client.sources.with_raw_response.delete(
                source_uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            space_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCrosmos) -> None:
        response = await async_client.sources.with_raw_response.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(TypesSource, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCrosmos) -> None:
        async with async_client.sources.with_streaming_response.get(
            source_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(TypesSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCrosmos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_uuid` but received ''"):
            await async_client.sources.with_raw_response.get(
                source_uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest(self, async_client: AsyncCrosmos) -> None:
        source = await async_client.sources.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IngestAccepted, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncCrosmos) -> None:
        response = await async_client.sources.with_raw_response.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(IngestAccepted, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncCrosmos) -> None:
        async with async_client.sources.with_streaming_response.ingest(
            sources=[{"content": "x"}],
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(IngestAccepted, source, path=["response"])

        assert cast(Any, response.is_closed) is True
