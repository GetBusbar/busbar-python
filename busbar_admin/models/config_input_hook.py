from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.config_input_hook_kind import ConfigInputHookKind
from ..models.config_input_hook_on_empty_type_0 import ConfigInputHookOnEmptyType0
from ..models.config_input_hook_phase_item import ConfigInputHookPhaseItem
from ..models.config_input_hook_prompt import ConfigInputHookPrompt
from ..models.config_input_hook_signals_item import ConfigInputHookSignalsItem
from ..models.config_input_hook_user import ConfigInputHookUser
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_input_hook_settings import ConfigInputHookSettings


T = TypeVar("T", bound="ConfigInputHook")


@_attrs_define(repr=False)
class ConfigInputHook:
    """Admin hook POST/PUT input. module and phase are the canonical names; use phase:[stage] for a single stage. This
    differs from the deploy HookDefinition wrapper. Settings may contain hidden values and must never be reconstructed
    from HookView.

        Attributes:
            kind (ConfigInputHookKind):
            module (str):
            timeout_ms (int | Unset):  Default: 1.
            on_error (str | Unset):  Default: 'nothing'.
            prompt (ConfigInputHookPrompt | Unset):  Default: ConfigInputHookPrompt.NO.
            user (ConfigInputHookUser | Unset):  Default: ConfigInputHookUser.NO.
            priority (int | Unset):  Default: 0.
            on_empty (ConfigInputHookOnEmptyType0 | None | Unset):
            settings (ConfigInputHookSettings | Unset):
            signals (list[ConfigInputHookSignalsItem] | Unset):
            global_ (bool | Unset):  Default: False.
            default (bool | Unset):  Default: False.
            groups (list[str] | Unset):
            phase (list[ConfigInputHookPhaseItem] | Unset):
    """

    kind: ConfigInputHookKind
    module: str
    timeout_ms: int | Unset = 1
    on_error: str | Unset = "nothing"
    prompt: ConfigInputHookPrompt | Unset = ConfigInputHookPrompt.NO
    user: ConfigInputHookUser | Unset = ConfigInputHookUser.NO
    priority: int | Unset = 0
    on_empty: ConfigInputHookOnEmptyType0 | None | Unset = UNSET
    settings: ConfigInputHookSettings | Unset = UNSET
    signals: list[ConfigInputHookSignalsItem] | Unset = UNSET
    global_: bool | Unset = False
    default: bool | Unset = False
    groups: list[str] | Unset = UNSET
    phase: list[ConfigInputHookPhaseItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        module = self.module

        timeout_ms = self.timeout_ms

        on_error = self.on_error

        prompt: str | Unset = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.value

        user: str | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.value

        priority = self.priority

        on_empty: None | str | Unset
        if isinstance(self.on_empty, Unset):
            on_empty = UNSET
        elif isinstance(self.on_empty, ConfigInputHookOnEmptyType0):
            on_empty = self.on_empty.value
        else:
            on_empty = self.on_empty

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        signals: list[str] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.value
                signals.append(signals_item)

        global_ = self.global_

        default = self.default

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        phase: list[str] | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = []
            for phase_item_data in self.phase:
                phase_item = phase_item_data.value
                phase.append(phase_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "module": module,
            }
        )
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms
        if on_error is not UNSET:
            field_dict["on_error"] = on_error
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if user is not UNSET:
            field_dict["user"] = user
        if priority is not UNSET:
            field_dict["priority"] = priority
        if on_empty is not UNSET:
            field_dict["on_empty"] = on_empty
        if settings is not UNSET:
            field_dict["settings"] = settings
        if signals is not UNSET:
            field_dict["signals"] = signals
        if global_ is not UNSET:
            field_dict["global"] = global_
        if default is not UNSET:
            field_dict["default"] = default
        if groups is not UNSET:
            field_dict["groups"] = groups
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_input_hook_settings import ConfigInputHookSettings  # noqa: PLC0415

        d = dict(src_dict)
        kind = ConfigInputHookKind(d.pop("kind"))

        module = d.pop("module")

        timeout_ms = d.pop("timeout_ms", UNSET)

        on_error = d.pop("on_error", UNSET)

        _prompt = d.pop("prompt", UNSET)
        prompt: ConfigInputHookPrompt | Unset
        if isinstance(_prompt, Unset):
            prompt = UNSET
        else:
            prompt = ConfigInputHookPrompt(_prompt)

        _user = d.pop("user", UNSET)
        user: ConfigInputHookUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ConfigInputHookUser(_user)

        priority = d.pop("priority", UNSET)

        def _parse_on_empty(data: object) -> ConfigInputHookOnEmptyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_empty_type_0 = ConfigInputHookOnEmptyType0(data)

                return on_empty_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for on_empty")

        on_empty = _parse_on_empty(d.pop("on_empty", UNSET))

        _settings = d.pop("settings", UNSET)
        settings: ConfigInputHookSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ConfigInputHookSettings.from_dict(_settings)

        _signals = d.pop("signals", UNSET)
        signals: list[ConfigInputHookSignalsItem] | Unset = UNSET
        if _signals is not UNSET:
            signals = []
            for signals_item_data in _signals:
                signals_item = ConfigInputHookSignalsItem(signals_item_data)

                signals.append(signals_item)

        global_ = d.pop("global", UNSET)

        default = d.pop("default", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        _phase = d.pop("phase", UNSET)
        phase: list[ConfigInputHookPhaseItem] | Unset = UNSET
        if _phase is not UNSET:
            phase = []
            for phase_item_data in _phase:
                phase_item = ConfigInputHookPhaseItem(phase_item_data)

                phase.append(phase_item)

        if d:
            raise ValueError("Unexpected fields for ConfigInputHook")
        config_input_hook = cls(
            kind=kind,
            module=module,
            timeout_ms=timeout_ms,
            on_error=on_error,
            prompt=prompt,
            user=user,
            priority=priority,
            on_empty=on_empty,
            settings=settings,
            signals=signals,
            global_=global_,
            default=default,
            groups=groups,
            phase=phase,
        )

        return config_input_hook
