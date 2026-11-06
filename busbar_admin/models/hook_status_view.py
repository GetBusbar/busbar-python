from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hook_desired_status import HookDesiredStatus
    from ..models.hook_reported_status import HookReportedStatus


T = TypeVar("T", bound="HookStatusView")


@_attrs_define(repr=False)
class HookStatusView:
    """`GET /hooks/{name}/status`, the hook's OBSERVED state: desired vs reported settings with a
    `drift` verdict, plus the hook's self-reported metrics. `reported`/`drift` are `null` and `note`
    is present when the hook did not answer (fail-open); `metrics` is invariantly an array.

        Attributes:
            name (str):
            desired (HookDesiredStatus): The DESIRED settings side of `hooks/{name}/status`: busbar's registry copy of the
                hook's settings
                (KEY NAMES only, see [`super::HookView::settings_keys`]) and their version.
            reported (HookReportedStatus | None):
            drift (bool | None):
            drift_keys (list[str]): The DESIRED settings KEY NAMES the hook is not actually running: the actionable half of
                `drift`, carrying names this body already serves and no value from either bag. Invariantly an
                array (empty on the no-answer branch, where no drift is known).
            metrics (list[Any]): Validated + bounded self-reported metrics; each entry carries `{name, type, value}` and,
                when
                the hook sent them, optional `labels`/`quantiles`/`estimated`/`ci_low`/`ci_high`/`help`/
                `label`/`unit`/`viz`/`max` members.

                schemars' blanket `JsonSchema` impl for
                `serde_json::Value` renders as the JSON-Schema-2020-12 boolean `true` (`schemars-1.2.1`'s
                `json_schema_impls/serdejson.rs`), which is legal 2020-12 but, nested here as this array's
                `items`, is a boolean SUB-schema, and `kin-openapi` (the parser under `oapi-codegen`, which
                every published SDK generates through) cannot represent one at all: the parse aborts, taking
                out Python/TS/Go SDK regeneration simultaneously. `#[schemars(schema_with)]` overrides just
                this field's schema to `{"type": "array", "items": {}}`; `{}` is the equivalent "accepts
                anything" schema every generator DOES understand, and is what busbar-ui's own
                `openapi-prep.py` already rewrites `items: true` into client-side. This is the only
                `items: true` in the document; every other `additionalProperties: true` schemars emits
                elsewhere is a boolean in a position `kin-openapi` handles fine and is deliberately untouched.
            as_of (int):
            source (str): Always `"live"` (the read is a live transport query).
            note (None | str | Unset): A short human note present only on the fail-open (no-answer) branch.
    """

    name: str
    desired: HookDesiredStatus
    reported: HookReportedStatus | None
    drift: bool | None
    drift_keys: list[str]
    metrics: list[Any]
    as_of: int
    source: str
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hook_reported_status import HookReportedStatus  # noqa: PLC0415

        name = self.name

        desired = self.desired.to_dict()

        reported: dict[str, Any] | None
        if isinstance(self.reported, HookReportedStatus):
            reported = self.reported.to_dict()
        else:
            reported = self.reported

        drift: bool | None
        drift = self.drift

        drift_keys = self.drift_keys

        metrics = self.metrics

        as_of = self.as_of

        source = self.source

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "desired": desired,
                "reported": reported,
                "drift": drift,
                "drift_keys": drift_keys,
                "metrics": metrics,
                "as_of": as_of,
                "source": source,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_desired_status import HookDesiredStatus  # noqa: PLC0415
        from ..models.hook_reported_status import HookReportedStatus  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        desired = HookDesiredStatus.from_dict(d.pop("desired"))

        def _parse_reported(data: object) -> HookReportedStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reported_type_0 = HookReportedStatus.from_dict(data)

                return reported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for reported")

        reported = _parse_reported(d.pop("reported"))

        def _parse_drift(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        drift = _parse_drift(d.pop("drift"))

        drift_keys = cast(list[str], d.pop("drift_keys"))

        metrics = cast(list[Any], d.pop("metrics"))

        as_of = d.pop("as_of")

        source = d.pop("source")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        hook_status_view = cls(
            name=name,
            desired=desired,
            reported=reported,
            drift=drift,
            drift_keys=drift_keys,
            metrics=metrics,
            as_of=as_of,
            source=source,
            note=note,
        )

        hook_status_view.additional_properties = d
        return hook_status_view

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
