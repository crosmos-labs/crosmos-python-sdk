# Spaces

Types:

```python
from crosmos.types import SpaceList, SpaceCreateResponse, SpaceGetResponse
```

Methods:

- <code title="post /api/v1/spaces">client.spaces.<a href="./src/crosmos/resources/spaces.py">create</a>(\*\*<a href="src/crosmos/types/space_create_params.py">params</a>) -> <a href="./src/crosmos/types/space_create_response.py">SpaceCreateResponse</a></code>
- <code title="get /api/v1/spaces">client.spaces.<a href="./src/crosmos/resources/spaces.py">list</a>(\*\*<a href="src/crosmos/types/space_list_params.py">params</a>) -> <a href="./src/crosmos/types/space_list.py">SpaceList</a></code>
- <code title="delete /api/v1/spaces/{space_uuid}">client.spaces.<a href="./src/crosmos/resources/spaces.py">delete</a>(space_uuid) -> None</code>
- <code title="get /api/v1/spaces/{space_uuid}">client.spaces.<a href="./src/crosmos/resources/spaces.py">get</a>(space_uuid) -> <a href="./src/crosmos/types/space_get_response.py">SpaceGetResponse</a></code>

# Search

Types:

```python
from crosmos.types import Search
```

Methods:

- <code title="post /api/v1/search">client.search.<a href="./src/crosmos/resources/search.py">hybrid</a>(\*\*<a href="src/crosmos/types/search_hybrid_params.py">params</a>) -> <a href="./src/crosmos/types/search.py">Search</a></code>

# Sources

Types:

```python
from crosmos.types import IngestAccepted, Source, SourceList
```

Methods:

- <code title="get /api/v1/sources">client.sources.<a href="./src/crosmos/resources/sources.py">list</a>(\*\*<a href="src/crosmos/types/source_list_params.py">params</a>) -> <a href="./src/crosmos/types/source_list.py">SourceList</a></code>
- <code title="delete /api/v1/sources/{source_uuid}">client.sources.<a href="./src/crosmos/resources/sources.py">delete</a>(source_uuid, \*\*<a href="src/crosmos/types/source_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/sources/{source_uuid}">client.sources.<a href="./src/crosmos/resources/sources.py">get</a>(source_uuid, \*\*<a href="src/crosmos/types/source_get_params.py">params</a>) -> <a href="./src/crosmos/types/source.py">Source</a></code>
- <code title="post /api/v1/sources">client.sources.<a href="./src/crosmos/resources/sources.py">ingest</a>(\*\*<a href="src/crosmos/types/source_ingest_params.py">params</a>) -> <a href="./src/crosmos/types/ingest_accepted.py">IngestAccepted</a></code>

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
from crosmos.types import JobGetStatusResponse
```

Methods:

- <code title="get /api/v1/jobs/{job_id}">client.jobs.<a href="./src/crosmos/resources/jobs.py">get_status</a>(job_id) -> <a href="./src/crosmos/types/job_get_status_response.py">JobGetStatusResponse</a></code>

# Usage

Types:

```python
from crosmos.types import Usage
```

Methods:

- <code title="get /api/v1/usage">client.usage.<a href="./src/crosmos/resources/usage.py">get</a>(\*\*<a href="src/crosmos/types/usage_get_params.py">params</a>) -> <a href="./src/crosmos/types/usage.py">Usage</a></code>
