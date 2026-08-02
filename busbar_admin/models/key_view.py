from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.key_view_labels import KeyViewLabels


T = TypeVar("T", bound="KeyView")


@_attrs_define
class KeyView:
    """Virtual-key metadata — the `key_meta()` shape returned by `GET /keys/{id}`, `PATCH /keys/{id}`,
    and as each item of `GET /keys`. Never the secret or its hash. 1.5.0: keys are PURE AUTH, no
    inline limits; `allowed_pools` is `null` = all pools, `[]` = no pools (C6); `group` names the
    bound `groups:` entry (`null` = unlimited).

        Attributes:
            allowed_pools (list[str] | None):
            created_at (int):
            enabled (bool):
            group (None | str):
            id (str):
            labels (KeyViewLabels):
            name (str):
            state (str): E-007: `enabled` alone cannot distinguish a reversible pause from either of the two permanent
                dispositions — `PATCH {enabled:false}`, `POST /keys/{id}/revoke`, and `DELETE /keys/{id}` all
                used to leave `enabled: false` with nothing else to tell them apart. One of exactly four
                values, additive and derived (never independently settable):
                - `"active"` — enabled, not revoked, not deleted.
                - `"disabled"` — `PATCH {enabled:false}`. Reversible: `PATCH {enabled:true}` restores it.
                - `"revoked"` — `POST /keys/{id}/revoke`. Permanent: denylisted, but the binding row (and
                  `GET /keys/{id}`) stays live for audit/usage attribution.
                - `"tombstoned"` — `DELETE /keys/{id}`. Permanent: denylisted AND hard-deleted; the row is
                  kept only so id-attributed billing/audit history keeps resolving. Omitted from a plain
                  `GET /keys` by default; visible there with `?include=tombstoned`.
    """

    allowed_pools: list[str] | None
    created_at: int
    enabled: bool
    group: None | str
    id: str
    labels: KeyViewLabels
    name: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_pools: list[str] | None
        if isinstance(self.allowed_pools, list):
            allowed_pools = self.allowed_pools

        else:
            allowed_pools = self.allowed_pools

        created_at = self.created_at

        enabled = self.enabled

        group: None | str
        group = self.group

        id = self.id

        labels = self.labels.to_dict()

        name = self.name

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_pools": allowed_pools,
                "created_at": created_at,
                "enabled": enabled,
                "group": group,
                "id": id,
                "labels": labels,
                "name": name,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_view_labels import KeyViewLabels

        d = dict(src_dict)

        def _parse_allowed_pools(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_pools_type_0 = cast(list[str], data)

                return allowed_pools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        allowed_pools = _parse_allowed_pools(d.pop("allowed_pools"))

        created_at = d.pop("created_at")

        enabled = d.pop("enabled")

        def _parse_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group = _parse_group(d.pop("group"))

        id = d.pop("id")

        labels = KeyViewLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        state = d.pop("state")

        key_view = cls(
            allowed_pools=allowed_pools,
            created_at=created_at,
            enabled=enabled,
            group=group,
            id=id,
            labels=labels,
            name=name,
            state=state,
        )

        key_view.additional_properties = d
        return key_view

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
