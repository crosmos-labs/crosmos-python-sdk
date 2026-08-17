# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from crosmos import Crosmos, AsyncCrosmos
from tests.utils import assert_matches_type
from crosmos.types import Search

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hybrid(self, client: Crosmos) -> None:
        search = client.search.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hybrid_with_all_params(self, client: Crosmos) -> None:
        search = client.search.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            diversify=True,
            graph=True,
            include_source=True,
            limit=1,
            recall_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recency_bias=0,
            rerank=True,
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_hybrid(self, client: Crosmos) -> None:
        response = client.search.with_raw_response.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_hybrid(self, client: Crosmos) -> None:
        with client.search.with_streaming_response.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hybrid(self, async_client: AsyncCrosmos) -> None:
        search = await async_client.search.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hybrid_with_all_params(self, async_client: AsyncCrosmos) -> None:
        search = await async_client.search.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            diversify=True,
            graph=True,
            include_source=True,
            limit=1,
            recall_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recency_bias=0,
            rerank=True,
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_hybrid(self, async_client: AsyncCrosmos) -> None:
        response = await async_client.search.with_raw_response.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_hybrid(self, async_client: AsyncCrosmos) -> None:
        async with async_client.search.with_streaming_response.hybrid(
            query="x",
            space_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True
