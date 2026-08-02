from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_hooks_body_config import PostHooksBodyConfig


T = TypeVar("T", bound="PostHooksBody")


@_attrs_define
class PostHooksBody:
    """
    Attributes:
        config (PostHooksBodyConfig): A `hooks:` entry, as JSON. The accepted shape is the config file's own, documented
            in the configuration reference; it is not restated here because several of its types parse a wire shape that
            does not match their field layout.
        name (str): The hook name.
    """

    config: PostHooksBodyConfig
    name: str

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_hooks_body_config import PostHooksBodyConfig

        d = dict(src_dict)
        config = PostHooksBodyConfig.from_dict(d.pop("config"))

        name = d.pop("name")

        post_hooks_body = cls(
            config=config,
            name=name,
        )

        return post_hooks_body
