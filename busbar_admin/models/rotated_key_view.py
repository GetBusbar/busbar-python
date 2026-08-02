from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rotated_key_view_labels import RotatedKeyViewLabels


T = TypeVar("T", bound="RotatedKeyView")


@_attrs_define
class RotatedKeyView:
    """`POST /keys/{id}/rotate` — the key metadata plus the ONCE-shown fresh CREDENTIAL. Exactly one of
    `token`+`expires_at` (a 1.5.0 signed-token key: a new token at a new binding generation, every
    prior token now rejected) or `secret` (a legacy hashed-secret key) is present.

        Attributes:
            allowed_pools (list[str] | None):
            created_at (int):
            enabled (bool):
            group (None | str):
            id (str):
            labels (RotatedKeyViewLabels):
            name (str):
            state (str): E-007: same field as `KeyView.state` — rotate does not change `enabled`/revoked/tombstoned
                status, so this reflects whatever the key's disposition already was (rotating a `disabled` or
                `revoked` key is legal and leaves it exactly that; only a `tombstoned` key refuses to rotate,
                which surfaces as 404 instead of this response).
            expires_at (int | None | Unset): Unix-seconds expiry of the re-minted signed token (present with `token`).
            secret (None | str | Unset): The fresh bearer secret — shown EXACTLY once (legacy hashed-secret keys only).
            token (None | str | Unset): The fresh busbar-SIGNED token — shown EXACTLY once (signed-token keys).
    """

    allowed_pools: list[str] | None
    created_at: int
    enabled: bool
    group: None | str
    id: str
    labels: RotatedKeyViewLabels
    name: str
    state: str
    expires_at: int | None | Unset = UNSET
    secret: None | str | Unset = UNSET
    token: None | str | Unset = UNSET
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

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

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
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if secret is not UNSET:
            field_dict["secret"] = secret
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotated_key_view_labels import RotatedKeyViewLabels

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

        labels = RotatedKeyViewLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        state = d.pop("state")

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        rotated_key_view = cls(
            allowed_pools=allowed_pools,
            created_at=created_at,
            enabled=enabled,
            group=group,
            id=id,
            labels=labels,
            name=name,
            state=state,
            expires_at=expires_at,
            secret=secret,
            token=token,
        )

        rotated_key_view.additional_properties = d
        return rotated_key_view

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
