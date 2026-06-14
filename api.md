# Spaces

Types:

```python
from crosmos.types import Space, SpaceList
```

Methods:

- <code title="post /api/v1/spaces">client.spaces.<a href="./src/crosmos/resources/spaces.py">create</a>(\*\*<a href="src/crosmos/types/space_create_params.py">params</a>) -> <a href="./src/crosmos/types/space.py">Space</a></code>
- <code title="get /api/v1/spaces">client.spaces.<a href="./src/crosmos/resources/spaces.py">list</a>(\*\*<a href="src/crosmos/types/space_list_params.py">params</a>) -> <a href="./src/crosmos/types/space_list.py">SpaceList</a></code>
- <code title="delete /api/v1/spaces/{space_uuid}">client.spaces.<a href="./src/crosmos/resources/spaces.py">delete</a>(space_uuid) -> None</code>
- <code title="get /api/v1/spaces/{space_uuid}">client.spaces.<a href="./src/crosmos/resources/spaces.py">get</a>(space_uuid) -> <a href="./src/crosmos/types/space.py">Space</a></code>

# Search

Types:

```python
from crosmos.types import Search
```

Methods:

- <code title="post /api/v1/search">client.search.<a href="./src/crosmos/resources/search.py">hybrid</a>(\*\*<a href="src/crosmos/types/search_hybrid_params.py">params</a>) -> <a href="./src/crosmos/types/search.py">Search</a></code>

# Orgs

Types:

```python
from crosmos.types import (
    AcceptInvite,
    Invite,
    InviteList,
    InvitePreview,
    Member,
    MemberList,
    Org,
    OrgListResponse,
    SetActiveOrg,
)
```

Methods:

- <code title="get /api/v1/orgs">client.orgs.<a href="./src/crosmos/resources/orgs.py">list</a>(\*\*<a href="src/crosmos/types/org_list_params.py">params</a>) -> <a href="./src/crosmos/types/org_list_response.py">OrgListResponse</a></code>
- <code title="post /api/v1/auth/active-org">client.orgs.<a href="./src/crosmos/resources/orgs.py">set_active</a>(\*\*<a href="src/crosmos/types/org_set_active_params.py">params</a>) -> <a href="./src/crosmos/types/set_active_org.py">SetActiveOrg</a></code>
- <code title="get /api/v1/orgs/{org_uuid}/members">client.orgs.<a href="./src/crosmos/resources/orgs.py">list_members</a>(org_uuid) -> <a href="./src/crosmos/types/member_list.py">MemberList</a></code>
- <code title="patch /api/v1/orgs/{org_uuid}/members/{user_uuid}">client.orgs.<a href="./src/crosmos/resources/orgs.py">update_member</a>(user_uuid, \*\*<a href="src/crosmos/types/org_update_member_params.py">params</a>) -> <a href="./src/crosmos/types/member.py">Member</a></code>
- <code title="delete /api/v1/orgs/{org_uuid}/members/{user_uuid}">client.orgs.<a href="./src/crosmos/resources/orgs.py">delete_member</a>(user_uuid, \*, org_uuid) -> None</code>
- <code title="post /api/v1/orgs/{org_uuid}/invites">client.orgs.<a href="./src/crosmos/resources/orgs.py">create_invite</a>(org_uuid, \*\*<a href="src/crosmos/types/org_create_invite_params.py">params</a>) -> <a href="./src/crosmos/types/invite.py">Invite</a></code>
- <code title="get /api/v1/orgs/{org_uuid}/invites">client.orgs.<a href="./src/crosmos/resources/orgs.py">list_invites</a>(org_uuid) -> <a href="./src/crosmos/types/invite_list.py">InviteList</a></code>
- <code title="delete /api/v1/orgs/{org_uuid}/invites/{invite_uuid}">client.orgs.<a href="./src/crosmos/resources/orgs.py">revoke_invite</a>(invite_uuid, \*, org_uuid) -> None</code>
- <code title="post /api/v1/orgs/invites/accept">client.orgs.<a href="./src/crosmos/resources/orgs.py">accept_invite</a>(\*\*<a href="src/crosmos/types/org_accept_invite_params.py">params</a>) -> <a href="./src/crosmos/types/accept_invite.py">AcceptInvite</a></code>
- <code title="get /api/v1/orgs/invites/preview">client.orgs.<a href="./src/crosmos/resources/orgs.py">preview_invite</a>(\*\*<a href="src/crosmos/types/org_preview_invite_params.py">params</a>) -> <a href="./src/crosmos/types/invite_preview.py">InvitePreview</a></code>

# Sources

Types:

```python
from crosmos.types import IngestAccepted, Source, SourceList, SourceVisibility
```

Methods:

- <code title="get /api/v1/sources">client.sources.<a href="./src/crosmos/resources/sources.py">list</a>(\*\*<a href="src/crosmos/types/source_list_params.py">params</a>) -> <a href="./src/crosmos/types/source_list.py">SourceList</a></code>
- <code title="delete /api/v1/sources/{source_uuid}">client.sources.<a href="./src/crosmos/resources/sources.py">delete</a>(source_uuid, \*\*<a href="src/crosmos/types/source_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/sources/{source_uuid}">client.sources.<a href="./src/crosmos/resources/sources.py">get</a>(source_uuid, \*\*<a href="src/crosmos/types/source_get_params.py">params</a>) -> <a href="./src/crosmos/types/source.py">Source</a></code>
- <code title="post /api/v1/sources">client.sources.<a href="./src/crosmos/resources/sources.py">ingest</a>(\*\*<a href="src/crosmos/types/source_ingest_params.py">params</a>) -> <a href="./src/crosmos/types/ingest_accepted.py">IngestAccepted</a></code>
- <code title="patch /api/v1/sources/{source_uuid}/visibility">client.sources.<a href="./src/crosmos/resources/sources.py">update_visibility</a>(source_uuid, \*\*<a href="src/crosmos/types/source_update_visibility_params.py">params</a>) -> <a href="./src/crosmos/types/source_visibility.py">SourceVisibility</a></code>

# Visibility

Types:

```python
from crosmos.types import (
    Grant,
    GrantImpact,
    GrantList,
    Group,
    GroupList,
    GroupMember,
    GroupMemberList,
    VisibilityPreviewResponse,
    VisibilitySettings,
    VisiblePrincipal,
)
```

Methods:

- <code title="post /api/v1/orgs/{org_uuid}/visibility/groups">client.visibility.<a href="./src/crosmos/resources/visibility.py">create_group</a>(org_uuid, \*\*<a href="src/crosmos/types/visibility_create_group_params.py">params</a>) -> <a href="./src/crosmos/types/group.py">Group</a></code>
- <code title="get /api/v1/orgs/{org_uuid}/visibility/groups">client.visibility.<a href="./src/crosmos/resources/visibility.py">list_groups</a>(org_uuid) -> <a href="./src/crosmos/types/group_list.py">GroupList</a></code>
- <code title="patch /api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}">client.visibility.<a href="./src/crosmos/resources/visibility.py">update_group</a>(group_uuid, \*\*<a href="src/crosmos/types/visibility_update_group_params.py">params</a>) -> <a href="./src/crosmos/types/group.py">Group</a></code>
- <code title="delete /api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}">client.visibility.<a href="./src/crosmos/resources/visibility.py">delete_group</a>(group_uuid, \*, org_uuid) -> None</code>
- <code title="get /api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members">client.visibility.<a href="./src/crosmos/resources/visibility.py">list_group_members</a>(group_uuid, \*, org_uuid) -> <a href="./src/crosmos/types/group_member_list.py">GroupMemberList</a></code>
- <code title="post /api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}">client.visibility.<a href="./src/crosmos/resources/visibility.py">add_group_member</a>(user_uuid, \*, org_uuid, group_uuid) -> None</code>
- <code title="delete /api/v1/orgs/{org_uuid}/visibility/groups/{group_uuid}/members/{user_uuid}">client.visibility.<a href="./src/crosmos/resources/visibility.py">remove_group_member</a>(user_uuid, \*, org_uuid, group_uuid) -> None</code>
- <code title="post /api/v1/orgs/{org_uuid}/visibility/grants">client.visibility.<a href="./src/crosmos/resources/visibility.py">create_grant</a>(org_uuid, \*\*<a href="src/crosmos/types/visibility_create_grant_params.py">params</a>) -> <a href="./src/crosmos/types/grant.py">Grant</a></code>
- <code title="get /api/v1/orgs/{org_uuid}/visibility/grants">client.visibility.<a href="./src/crosmos/resources/visibility.py">list_grants</a>(org_uuid) -> <a href="./src/crosmos/types/grant_list.py">GrantList</a></code>
- <code title="post /api/v1/orgs/{org_uuid}/visibility/grants/preview">client.visibility.<a href="./src/crosmos/resources/visibility.py">preview_grant</a>(org_uuid, \*\*<a href="src/crosmos/types/visibility_create_grant_params.py">params</a>) -> <a href="./src/crosmos/types/grant_impact.py">GrantImpact</a></code>
- <code title="delete /api/v1/orgs/{org_uuid}/visibility/grants/{grant_uuid}">client.visibility.<a href="./src/crosmos/resources/visibility.py">delete_grant</a>(grant_uuid, \*, org_uuid) -> None</code>
- <code title="get /api/v1/orgs/{org_uuid}/visibility/preview">client.visibility.<a href="./src/crosmos/resources/visibility.py">preview</a>(org_uuid, \*\*<a href="src/crosmos/types/visibility_preview_params.py">params</a>) -> <a href="./src/crosmos/types/visibility_preview_response.py">VisibilityPreviewResponse</a></code>
- <code title="patch /api/v1/orgs/{org_uuid}/visibility/settings">client.visibility.<a href="./src/crosmos/resources/visibility.py">update_settings</a>(org_uuid, \*\*<a href="src/crosmos/types/visibility_update_settings_params.py">params</a>) -> <a href="./src/crosmos/types/visibility_settings.py">VisibilitySettings</a></code>

# Memories

Types:

```python
from crosmos.types import Memory, MemoryList
```

Methods:

- <code title="get /api/v1/memories">client.memories.<a href="./src/crosmos/resources/memories.py">list</a>(\*\*<a href="src/crosmos/types/memory_list_params.py">params</a>) -> <a href="./src/crosmos/types/memory_list.py">MemoryList</a></code>
- <code title="delete /api/v1/memories/{memory_uuid}">client.memories.<a href="./src/crosmos/resources/memories.py">delete</a>(memory_uuid, \*\*<a href="src/crosmos/types/memory_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/memories/{memory_uuid}">client.memories.<a href="./src/crosmos/resources/memories.py">get</a>(memory_uuid, \*\*<a href="src/crosmos/types/memory_get_params.py">params</a>) -> <a href="./src/crosmos/types/memory.py">Memory</a></code>

# Entities

Types:

```python
from crosmos.types import Entity, EntityDetail, EntityList
```

Methods:

- <code title="get /api/v1/entities">client.entities.<a href="./src/crosmos/resources/entities.py">list</a>(\*\*<a href="src/crosmos/types/entity_list_params.py">params</a>) -> <a href="./src/crosmos/types/entity_list.py">EntityList</a></code>
- <code title="get /api/v1/entities/{entity_uuid}">client.entities.<a href="./src/crosmos/resources/entities.py">get</a>(entity_uuid, \*\*<a href="src/crosmos/types/entity_get_params.py">params</a>) -> <a href="./src/crosmos/types/entity_detail.py">EntityDetail</a></code>

# Conversations

Types:

```python
from crosmos.types import IngestConversation
```

Methods:

- <code title="post /api/v1/conversations">client.conversations.<a href="./src/crosmos/resources/conversations.py">ingest</a>(\*\*<a href="src/crosmos/types/conversation_ingest_params.py">params</a>) -> <a href="./src/crosmos/types/ingest_conversation.py">IngestConversation</a></code>

# Jobs

Types:

```python
from crosmos.types import Job
```

Methods:

- <code title="get /api/v1/jobs/{job_id}">client.jobs.<a href="./src/crosmos/resources/jobs.py">get_status</a>(job_id) -> <a href="./src/crosmos/types/job.py">Job</a></code>

# Usage

Types:

```python
from crosmos.types import Usage
```

Methods:

- <code title="get /api/v1/usage">client.usage.<a href="./src/crosmos/resources/usage.py">get</a>(\*\*<a href="src/crosmos/types/usage_get_params.py">params</a>) -> <a href="./src/crosmos/types/usage.py">Usage</a></code>

# Health

Types:

```python
from crosmos.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/crosmos/resources/health.py">check</a>() -> <a href="./src/crosmos/types/health_check_response.py">HealthCheckResponse</a></code>
