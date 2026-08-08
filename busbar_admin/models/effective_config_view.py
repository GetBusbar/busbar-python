from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auth_view import AuthView
    from ..models.hook_view import HookView
    from ..models.model_view import ModelView
    from ..models.pool_view import PoolView
    from ..models.provider_view import ProviderView


T = TypeVar("T", bound="EffectiveConfigView")


@_attrs_define
class EffectiveConfigView:
    """The EFFECTIVE config snapshot (`GET /api/v1/admin/config`): the running configuration as busbar
    resolved it, for drift detection (compare against your desired config) and one-shot inspection.
    Composed from the same REDACTED reads as the individual endpoints (auth chain names, pool/model/
    provider topology, hook definitions, global-hook wiring), so it carries NO secret: no client
    tokens, no provider keys, no hook payloads. Additive-only; the source-layer annotation (base vs
    overlay) lands with the config overlay substrate.

        Attributes:
            auth (AuthView): The ingress auth chain read (`GET /api/v1/admin/auth`): the ordered module names that
                authenticate
                callers + the upstream-credential mode. Never a secret: module names and the mode are config
                identifiers, not credentials. An empty `chain` is the open front door (admits every request).
            global_hooks (list[str]): Names fired on EVERY request: the hooks attached at the reserved all-pools key
                `pools.hooks:`
                in `config.yaml` (the 1.5.3 replacement for the DELETED `global_hooks:` key; that key no
                longer parses), plus any hook this API declares with `global: true`. The response FIELD name
                stays `global_hooks`; only the config-file spelling changed.
            hooks (list[HookView]):
            models (list[ModelView]):
            pools (list[PoolView]):
            providers (list[ProviderView]):
            version (int): The monotonic config version at the time of this read (see `InfoView.config_version`), so a
                drift-detection read gets the config AND its version in one call.
    """

    auth: AuthView
    global_hooks: list[str]
    hooks: list[HookView]
    models: list[ModelView]
    pools: list[PoolView]
    providers: list[ProviderView]
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        global_hooks = self.global_hooks

        hooks = []
        for hooks_item_data in self.hooks:
            hooks_item = hooks_item_data.to_dict()
            hooks.append(hooks_item)

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
                "global_hooks": global_hooks,
                "hooks": hooks,
                "models": models,
                "pools": pools,
                "providers": providers,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_view import AuthView
        from ..models.hook_view import HookView
        from ..models.model_view import ModelView
        from ..models.pool_view import PoolView
        from ..models.provider_view import ProviderView

        d = dict(src_dict)
        auth = AuthView.from_dict(d.pop("auth"))

        global_hooks = cast(list[str], d.pop("global_hooks"))

        hooks = []
        _hooks = d.pop("hooks")
        for hooks_item_data in _hooks:
            hooks_item = HookView.from_dict(hooks_item_data)

            hooks.append(hooks_item)

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelView.from_dict(models_item_data)

            models.append(models_item)

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = PoolView.from_dict(pools_item_data)

            pools.append(pools_item)

        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = ProviderView.from_dict(providers_item_data)

            providers.append(providers_item)

        version = d.pop("version")

        effective_config_view = cls(
            auth=auth,
            global_hooks=global_hooks,
            hooks=hooks,
            models=models,
            pools=pools,
            providers=providers,
            version=version,
        )

        effective_config_view.additional_properties = d
        return effective_config_view

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
