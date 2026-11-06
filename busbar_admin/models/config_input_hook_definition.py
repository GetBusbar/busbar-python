from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.config_input_hook_definition_kind_type_0 import ConfigInputHookDefinitionKindType0
from ..models.config_input_hook_definition_on_empty_type_0 import ConfigInputHookDefinitionOnEmptyType0
from ..models.config_input_hook_definition_on_error_type_0_type_0 import ConfigInputHookDefinitionOnErrorType0Type0
from ..models.config_input_hook_definition_phase_item import ConfigInputHookDefinitionPhaseItem
from ..models.config_input_hook_definition_prompt_type_0 import ConfigInputHookDefinitionPromptType0
from ..models.config_input_hook_definition_user_type_0 import ConfigInputHookDefinitionUserType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_input_hook_definition_on_error_type_0_type_1 import ConfigInputHookDefinitionOnErrorType0Type1
    from ..models.config_input_hook_definition_settings import ConfigInputHookDefinitionSettings


T = TypeVar("T", bound="ConfigInputHookDefinition")


@_attrs_define(repr=False)
class ConfigInputHookDefinition:
    """Actual top-level hooks named-definition input (HookDefCfg). Admin POST/PUT consumes Hook instead. default, signals
    and global are accepted by admin writes, not by this deploy wrapper.

        Attributes:
            module (str):
            settings (ConfigInputHookDefinitionSettings | Unset):
            groups (list[str] | Unset):
            phase (list[ConfigInputHookDefinitionPhaseItem] | Unset):
            kind (ConfigInputHookDefinitionKindType0 | None | Unset):
            timeout_ms (int | None | Unset):
            priority (int | None | Unset):
            on_empty (ConfigInputHookDefinitionOnEmptyType0 | None | Unset):
            prompt (ConfigInputHookDefinitionPromptType0 | None | Unset):
            user (ConfigInputHookDefinitionUserType0 | None | Unset):
            on_error (ConfigInputHookDefinitionOnErrorType0Type0 | ConfigInputHookDefinitionOnErrorType0Type1 | None |
                Unset):
    """

    module: str
    settings: ConfigInputHookDefinitionSettings | Unset = UNSET
    groups: list[str] | Unset = UNSET
    phase: list[ConfigInputHookDefinitionPhaseItem] | Unset = UNSET
    kind: ConfigInputHookDefinitionKindType0 | None | Unset = UNSET
    timeout_ms: int | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    on_empty: ConfigInputHookDefinitionOnEmptyType0 | None | Unset = UNSET
    prompt: ConfigInputHookDefinitionPromptType0 | None | Unset = UNSET
    user: ConfigInputHookDefinitionUserType0 | None | Unset = UNSET
    on_error: ConfigInputHookDefinitionOnErrorType0Type0 | ConfigInputHookDefinitionOnErrorType0Type1 | None | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_input_hook_definition_on_error_type_0_type_1 import (
            ConfigInputHookDefinitionOnErrorType0Type1,  # noqa: PLC0415
        )

        module = self.module

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        phase: list[str] | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = []
            for phase_item_data in self.phase:
                phase_item = phase_item_data.value
                phase.append(phase_item)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, ConfigInputHookDefinitionKindType0):
            kind = self.kind.value
        else:
            kind = self.kind

        timeout_ms: int | None | Unset
        if isinstance(self.timeout_ms, Unset):
            timeout_ms = UNSET
        else:
            timeout_ms = self.timeout_ms

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        on_empty: None | str | Unset
        if isinstance(self.on_empty, Unset):
            on_empty = UNSET
        elif isinstance(self.on_empty, ConfigInputHookDefinitionOnEmptyType0):
            on_empty = self.on_empty.value
        else:
            on_empty = self.on_empty

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        elif isinstance(self.prompt, ConfigInputHookDefinitionPromptType0):
            prompt = self.prompt.value
        else:
            prompt = self.prompt

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, ConfigInputHookDefinitionUserType0):
            user = self.user.value
        else:
            user = self.user

        on_error: dict[str, Any] | None | str | Unset
        if isinstance(self.on_error, Unset):
            on_error = UNSET
        elif isinstance(self.on_error, ConfigInputHookDefinitionOnErrorType0Type0):
            on_error = self.on_error.value
        elif isinstance(self.on_error, ConfigInputHookDefinitionOnErrorType0Type1):
            on_error = self.on_error.to_dict()
        else:
            on_error = self.on_error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "module": module,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings
        if groups is not UNSET:
            field_dict["groups"] = groups
        if phase is not UNSET:
            field_dict["phase"] = phase
        if kind is not UNSET:
            field_dict["kind"] = kind
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms
        if priority is not UNSET:
            field_dict["priority"] = priority
        if on_empty is not UNSET:
            field_dict["on_empty"] = on_empty
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if user is not UNSET:
            field_dict["user"] = user
        if on_error is not UNSET:
            field_dict["on_error"] = on_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_input_hook_definition_on_error_type_0_type_1 import (
            ConfigInputHookDefinitionOnErrorType0Type1,  # noqa: PLC0415
        )
        from ..models.config_input_hook_definition_settings import ConfigInputHookDefinitionSettings  # noqa: PLC0415

        d = dict(src_dict)
        module = d.pop("module")

        _settings = d.pop("settings", UNSET)
        settings: ConfigInputHookDefinitionSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ConfigInputHookDefinitionSettings.from_dict(_settings)

        groups = cast(list[str], d.pop("groups", UNSET))

        _phase = d.pop("phase", UNSET)
        phase: list[ConfigInputHookDefinitionPhaseItem] | Unset = UNSET
        if _phase is not UNSET:
            phase = []
            for phase_item_data in _phase:
                phase_item = ConfigInputHookDefinitionPhaseItem(phase_item_data)

                phase.append(phase_item)

        def _parse_kind(data: object) -> ConfigInputHookDefinitionKindType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = ConfigInputHookDefinitionKindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for kind")

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_timeout_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout_ms = _parse_timeout_ms(d.pop("timeout_ms", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_on_empty(data: object) -> ConfigInputHookDefinitionOnEmptyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_empty_type_0 = ConfigInputHookDefinitionOnEmptyType0(data)

                return on_empty_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for on_empty")

        on_empty = _parse_on_empty(d.pop("on_empty", UNSET))

        def _parse_prompt(data: object) -> ConfigInputHookDefinitionPromptType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prompt_type_0 = ConfigInputHookDefinitionPromptType0(data)

                return prompt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for prompt")

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_user(data: object) -> ConfigInputHookDefinitionUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_type_0 = ConfigInputHookDefinitionUserType0(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for user")

        user = _parse_user(d.pop("user", UNSET))

        def _parse_on_error(
            data: object,
        ) -> ConfigInputHookDefinitionOnErrorType0Type0 | ConfigInputHookDefinitionOnErrorType0Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_error_type_0_type_0 = ConfigInputHookDefinitionOnErrorType0Type0(data)

                return on_error_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                on_error_type_0_type_1 = ConfigInputHookDefinitionOnErrorType0Type1.from_dict(data)

                return on_error_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for on_error")

        on_error = _parse_on_error(d.pop("on_error", UNSET))

        if d:
            raise ValueError("Unexpected fields for ConfigInputHookDefinition")
        config_input_hook_definition = cls(
            module=module,
            settings=settings,
            groups=groups,
            phase=phase,
            kind=kind,
            timeout_ms=timeout_ms,
            priority=priority,
            on_empty=on_empty,
            prompt=prompt,
            user=user,
            on_error=on_error,
        )

        return config_input_hook_definition
