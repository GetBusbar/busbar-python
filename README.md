# busbar-admin (Python SDK)

A typed Python client for the **Busbar Admin API** (`/api/v1/admin`).

The client is generated from the typed OpenAPI 3.1 schema in
[`openapi.json`](./openapi.json) with
[`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client),
so every response is a real dataclass (`InfoView`, `TopologyInfo`, ...) — not
`Any`/`dict`.

> **PyPI package name:** `busbar-admin`.
> (`busbar` is already taken on PyPI, so the admin SDK ships as `busbar-admin`.)

## Versioning

- **SDK version:** `0.4.0`. The SDK carries its own semantic version, independent of
  the busbar server it talks to.
- **Generated from:** busbar OpenAPI `info.version` `1.5.3`, the bundled
  [`openapi.json`](./openapi.json).

A given SDK release targets the frozen, additive-only `/api/v1/admin` surface and will
keep working across server versions on that surface.

Neither number above is maintained by hand alone: CI runs
`.github/check-readme-versions.py`, which fails the build if this section stops matching
`setup.py` and `openapi.json`. They went stale silently once, so now they cannot.

### History

`0.2.0` was the breaking release: the busbar `1.5.0` spec added `operationId`s, which
renamed every generated function.

## Install

```bash
pip install busbar-admin
```

## Usage

The admin API authenticates with an `x-admin-token` header. Construct an
`AuthenticatedClient` that sends the token under that header name (no `Bearer`
prefix):

```python
from busbar_admin import AuthenticatedClient
from busbar_admin.api.default import get_info
from busbar_admin.models import InfoView

client = AuthenticatedClient(
    base_url="http://localhost:8081",
    token="YOUR_ADMIN_TOKEN",
    # send the credential as `x-admin-token: <token>` instead of Authorization: Bearer
    auth_header_name="x-admin-token",
    prefix="",
)

with client as client:
    info: InfoView = get_info.sync(client=client)
    # `info` is TYPED — your editor autocompletes .version, .topology, .build, ...
    print("busbar version:", info.version)                 # -> "1.5.3"
    print("pools:", info.topology.pools)
    print("config version:", info.config_version)
```

> Prefer `Authorization: Bearer`? Drop the `auth_header_name`/`prefix` overrides —
> the default `AuthenticatedClient` sends `Authorization: Bearer <token>`, which
> the admin API also accepts.

Async is available too (`get_info.asyncio` / `.asyncio_detailed`).

## Regenerating the client

The committed client is generated from `openapi.json`. To re-derive it:

```bash
make generate     # pins openapi-python-client via requirements-dev.txt
```

CI regenerates on every PR/push and fails if the committed client drifts from
`openapi.json` (`git diff --exit-code`).

## License

Apache-2.0 © Busbar, Inc.
