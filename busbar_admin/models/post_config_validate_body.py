from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_config_validate_body_config import PostConfigValidateBodyConfig
    from ..models.post_config_validate_body_providers import PostConfigValidateBodyProviders


T = TypeVar("T", bound="PostConfigValidateBody")


@_attrs_define
class PostConfigValidateBody:
    """Validate a configuration without applying it.

    Attributes:
        config (PostConfigValidateBodyConfig): A `config.yaml` deploy block, as JSON. The accepted shape is the config
            file's own, documented in the configuration reference; it is not restated here because several of its types
            parse a wire shape that does not match their field layout.
        providers (PostConfigValidateBodyProviders | Unset): A `providers.yaml` document, as JSON. The accepted shape is
            the config file's own, documented in the configuration reference; it is not restated here because several of its
            types parse a wire shape that does not match their field layout.
    """

    config: PostConfigValidateBodyConfig
    providers: PostConfigValidateBodyProviders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
            }
        )
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_config_validate_body_config import PostConfigValidateBodyConfig
        from ..models.post_config_validate_body_providers import PostConfigValidateBodyProviders

        d = dict(src_dict)
        config = PostConfigValidateBodyConfig.from_dict(d.pop("config"))

        _providers = d.pop("providers", UNSET)
        providers: PostConfigValidateBodyProviders | Unset
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = PostConfigValidateBodyProviders.from_dict(_providers)

        post_config_validate_body = cls(
            config=config,
            providers=providers,
        )

        return post_config_validate_body
