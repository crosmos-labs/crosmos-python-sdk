# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrgUpdateMemberParams"]


class OrgUpdateMemberParams(TypedDict, total=False):
    org_uuid: Required[str]
    """Path param: the organization the member belongs to."""

    role: Required[Literal["admin", "member"]]
    """Body param: the new role to assign."""
