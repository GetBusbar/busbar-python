# busbar-admin (Python SDK)

[![Coverage](https://codecov.io/gh/GetBusbar/busbar-python/branch/dev/graph/badge.svg)](https://codecov.io/gh/GetBusbar/busbar-python)

A typed Python client for the **Busbar Admin API** (`/api/v1/admin`).

The client is generated from the typed OpenAPI 3.1 schema in
[`openapi.json`](./openapi.json) with
[`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client),
so every response is a real dataclass (`InfoView`, `TopologyInfo`, ...) — not
`Any`/`dict`.

> **PyPI package name:** `busbar-admin`.
> (`busbar` is already taken on PyPI, so the admin SDK ships as `busbar-admin`.)

## Versioning

The SDK carries its **own** semantic version, independent of the busbar server /
OpenAPI `info.version` (currently `1.6.0`). This first cut is **`0.1.0`**. A given
SDK release targets the frozen, additive-only `/api/v1/admin` surface and will
keep working across server versions on that surface.

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
from busbar_admin.api.default import get_api_v1_admin_info
from busbar_admin.models import InfoView

client = AuthenticatedClient(
    base_url="http://localhost:8081",
    token="YOUR_ADMIN_TOKEN",
    # send the credential as `x-admin-token: <token>` instead of Authorization: Bearer
    auth_header_name="x-admin-token",
    prefix="",
)

with client as client:
    response = get_api_v1_admin_info.sync_detailed(client=client)
    info = response.parsed
    if not isinstance(info, InfoView):
        raise RuntimeError(f"Admin info failed (HTTP {response.status_code})")
    # `info` is TYPED — your editor autocompletes .version, .topology, .build, ...
    print("busbar version:", info.version)                 # -> "1.6.0"
    print("pools:", info.topology.pools)
    print("config version:", info.config_version)
```

> Prefer `Authorization: Bearer`? Drop the `auth_header_name`/`prefix` overrides —
> the default `AuthenticatedClient` sends `Authorization: Bearer <token>`, which
> the admin API also accepts.

Async is available too (`get_api_v1_admin_info.asyncio` / `.asyncio_detailed`).

## Regenerating the client

The committed client is generated from `openapi.json`. To re-derive it:

```bash
make install-generator  # installs the pinned generator
make generate           # verifies the pin before regenerating
```

CI regenerates on every PR/push and fails if the committed client drifts from
`openapi.json` (`git diff --exit-code`).

## License

Apache-2.0 © Busbar, Inc.

## Client safety and customization

The checked-in `templates/` directory customizes the pinned generator. Keep it
when regenerating: `make generate` applies these templates automatically.
Client builder methods return independent configurations and do not mutate the
original client's transports. Client and response representations omit credentials
and payloads; model representations omit fields because arbitrary API settings
and extension properties may contain secrets. Explicit attributes and `to_dict()`
still expose the requested data. Unexpected-status exceptions retain the raw
response in `.content`, but omit it from their diagnostic text. Nonstandard HTTP
status codes are retained as integers; standard codes remain `HTTPStatus` values.

## Differences from 1.5.5

For the admin-token authentication surface present in server 1.5.5, this SDK
rejects malformed authentication fields, including control characters and
surrounding header whitespace, before handing them to the
HTTP transport, preventing malformed credentials from being echoed in transport
errors. Well-formed credentials retain the same wire format.

Custom authentication headers such as `x-admin-token` are sent only to the
configured origin, including when redirect following is enabled. Same-origin
redirects retain the credential. Manually supplied HTTPX clients retain their own
authentication and redirect configuration.

After `set_httpx_client()` or `set_async_httpx_client()`, configure the supplied
HTTPX client directly. The `with_headers`, `with_cookies`, and `with_timeout`
builders reject this combination because a caller-owned transport cannot safely
be copied; silently dropping it could change the request destination.

SDK endpoint calls limit accumulated decoded response bodies, including redirect
responses, to 32 MiB per call by default.
Set `max_response_bytes` to a positive integer on either client to allow larger
trusted admin responses. Oversized responses raise `ValueError` and close their
streams. HTTPX continues to handle content decoding; this limit bounds SDK
accumulation rather than the decoder's transient allocation.

The schema is the canonical 1.6.0 Admin API snapshot. Existing path-derived
endpoint module imports remain available as compatibility aliases for the new
operation-ID modules. Request models carry the documented JSON bodies, and key
responses expose signed `token` credentials and group metadata. Hook reads expose
`settings_keys`, preserving the server's redacted projection. Models whose schemas
forbid unknown fields reject them in `from_dict()` instead of silently dropping
configuration such as removed key limits. Malformed nullable model objects raise
a parsing error; a genuine JSON `null` remains accepted.

The response budget also applies to SDK calls made through a manually supplied
HTTPX client. Other calls through that HTTPX client keep their existing behavior.
