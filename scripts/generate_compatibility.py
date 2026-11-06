"""Preserve established endpoint module imports after operation IDs were added."""

import json
from pathlib import Path

from openapi_python_client.strings import PythonIdentifier

LEGACY_ENDPOINTS = {
    "delete_api_v1_admin_hooks_name": ("/api/v1/admin/hooks/{name}", "delete"),
    "delete_api_v1_admin_keys_id": ("/api/v1/admin/keys/{id}", "delete"),
    "get_api_v1_admin_admin_auth": ("/api/v1/admin/admin-auth", "get"),
    "get_api_v1_admin_audit": ("/api/v1/admin/audit", "get"),
    "get_api_v1_admin_auth": ("/api/v1/admin/auth", "get"),
    "get_api_v1_admin_config": ("/api/v1/admin/config", "get"),
    "get_api_v1_admin_config_diff": ("/api/v1/admin/config/diff", "get"),
    "get_api_v1_admin_config_versions": ("/api/v1/admin/config/versions", "get"),
    "get_api_v1_admin_config_versions_v": ("/api/v1/admin/config/versions/{v}", "get"),
    "get_api_v1_admin_hooks": ("/api/v1/admin/hooks", "get"),
    "get_api_v1_admin_hooks_name": ("/api/v1/admin/hooks/{name}", "get"),
    "get_api_v1_admin_hooks_name_health": ("/api/v1/admin/hooks/{name}/health", "get"),
    "get_api_v1_admin_hooks_name_schema": ("/api/v1/admin/hooks/{name}/schema", "get"),
    "get_api_v1_admin_hooks_name_status": ("/api/v1/admin/hooks/{name}/status", "get"),
    "get_api_v1_admin_info": ("/api/v1/admin/info", "get"),
    "get_api_v1_admin_keys": ("/api/v1/admin/keys", "get"),
    "get_api_v1_admin_keys_id": ("/api/v1/admin/keys/{id}", "get"),
    "get_api_v1_admin_keys_id_usage": ("/api/v1/admin/keys/{id}/usage", "get"),
    "get_api_v1_admin_models": ("/api/v1/admin/models", "get"),
    "get_api_v1_admin_openapi_json": ("/api/v1/admin/openapi.json", "get"),
    "get_api_v1_admin_plugins": ("/api/v1/admin/plugins", "get"),
    "get_api_v1_admin_pools": ("/api/v1/admin/pools", "get"),
    "get_api_v1_admin_pools_name": ("/api/v1/admin/pools/{name}", "get"),
    "get_api_v1_admin_providers": ("/api/v1/admin/providers", "get"),
    "get_api_v1_admin_usage": ("/api/v1/admin/usage", "get"),
    "patch_api_v1_admin_hooks_name_settings": ("/api/v1/admin/hooks/{name}/settings", "patch"),
    "patch_api_v1_admin_keys_id": ("/api/v1/admin/keys/{id}", "patch"),
    "post_api_v1_admin_auth_cache_flush": ("/api/v1/admin/auth/cache/flush", "post"),
    "post_api_v1_admin_config_apply": ("/api/v1/admin/config/apply", "post"),
    "post_api_v1_admin_config_reload": ("/api/v1/admin/config/reload", "post"),
    "post_api_v1_admin_config_rollback": ("/api/v1/admin/config/rollback", "post"),
    "post_api_v1_admin_config_validate": ("/api/v1/admin/config/validate", "post"),
    "post_api_v1_admin_hooks": ("/api/v1/admin/hooks", "post"),
    "post_api_v1_admin_keys": ("/api/v1/admin/keys", "post"),
    "post_api_v1_admin_keys_id_rotate": ("/api/v1/admin/keys/{id}/rotate", "post"),
    "put_api_v1_admin_admin_auth": ("/api/v1/admin/admin-auth", "put"),
    "put_api_v1_admin_hooks_name": ("/api/v1/admin/hooks/{name}", "put"),
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    schema = json.loads((root / "openapi.json").read_text())
    error_code = schema["components"]["schemas"]["Error"]["properties"]["error"]["properties"]["code"]
    if error_code.get("x-busbar-extensible-enum") is not True:
        raise RuntimeError("Review the ErrorErrorCode extensible-enum template against the current schema")
    target_dir = root / "busbar_admin/api/default"
    names = (
        "_build_response",
        "_get_kwargs",
        "_parse_response",
        "asyncio",
        "asyncio_detailed",
        "sync",
        "sync_detailed",
    )
    for legacy, (path, method) in LEGACY_ENDPOINTS.items():
        operation = schema["paths"][path][method]
        target = PythonIdentifier(operation["operationId"], prefix="field_")
        if target == legacy:
            continue
        if not (target_dir / f"{target}.py").is_file():
            raise RuntimeError(f"Missing generated compatibility target: {target}")
        imports = "\n".join(f"from .{target} import {name} as {name}" for name in names)
        content = f'"""Compatibility import for `{target}`."""\n\n{imports}\n'
        (target_dir / f"{legacy}.py").write_text(content)


if __name__ == "__main__":
    main()
