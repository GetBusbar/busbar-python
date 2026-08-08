from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.created_key_view_labels import CreatedKeyViewLabels


T = TypeVar("T", bound="CreatedKeyView")


@_attrs_define
class CreatedKeyView:
    """`POST /keys` (mint): the key metadata plus the ONCE-shown signed token, and (when an AWS SigV4
    credential was requested) the AccessKeyId + secret access key. The AWS fields are absent on a
    bearer-only mint.

        Attributes:
            allowed_pools (list[str] | None):
            created_at (int):
            enabled (bool):
            expires_at (int): Unix-seconds expiry of the signed token.
            group (None | str):
            group_provisioned (bool): Whether this mint AUTO-PROVISIONED its bound group leaf (self-service); lets a portal
                distinguish "bound to an existing bucket" from "created your personal bucket + bound".
            id (str):
            labels (CreatedKeyViewLabels):
            name (str):
            state (str): Same field as `KeyView.state`; a fresh mint is always `"active"` (enabled, not
                revoked, not deleted).
            token (str): The busbar-SIGNED token: the key credential (1.5.0), shown EXACTLY once and never
                returned by any read. (This is the field a client must capture to authenticate.)
            aws_access_key_id (None | str | Unset): AWS AccessKeyId (present only when `issue_aws_credential` was set). Not
                secret.
            aws_secret_access_key (None | str | Unset): AWS SigV4 secret access key, shown once (present only with an AWS
                credential).
    """

    allowed_pools: list[str] | None
    created_at: int
    enabled: bool
    expires_at: int
    group: None | str
    group_provisioned: bool
    id: str
    labels: CreatedKeyViewLabels
    name: str
    state: str
    token: str
    aws_access_key_id: None | str | Unset = UNSET
    aws_secret_access_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_pools: list[str] | None
        if isinstance(self.allowed_pools, list):
            allowed_pools = self.allowed_pools

        else:
            allowed_pools = self.allowed_pools

        created_at = self.created_at

        enabled = self.enabled

        expires_at = self.expires_at

        group: None | str
        group = self.group

        group_provisioned = self.group_provisioned

        id = self.id

        labels = self.labels.to_dict()

        name = self.name

        state = self.state

        token = self.token

        aws_access_key_id: None | str | Unset
        if isinstance(self.aws_access_key_id, Unset):
            aws_access_key_id = UNSET
        else:
            aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key: None | str | Unset
        if isinstance(self.aws_secret_access_key, Unset):
            aws_secret_access_key = UNSET
        else:
            aws_secret_access_key = self.aws_secret_access_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_pools": allowed_pools,
                "created_at": created_at,
                "enabled": enabled,
                "expires_at": expires_at,
                "group": group,
                "group_provisioned": group_provisioned,
                "id": id,
                "labels": labels,
                "name": name,
                "state": state,
                "token": token,
            }
        )
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_key_view_labels import CreatedKeyViewLabels

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

        expires_at = d.pop("expires_at")

        def _parse_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group = _parse_group(d.pop("group"))

        group_provisioned = d.pop("group_provisioned")

        id = d.pop("id")

        labels = CreatedKeyViewLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        state = d.pop("state")

        token = d.pop("token")

        def _parse_aws_access_key_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_access_key_id = _parse_aws_access_key_id(d.pop("aws_access_key_id", UNSET))

        def _parse_aws_secret_access_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_secret_access_key = _parse_aws_secret_access_key(d.pop("aws_secret_access_key", UNSET))

        created_key_view = cls(
            allowed_pools=allowed_pools,
            created_at=created_at,
            enabled=enabled,
            expires_at=expires_at,
            group=group,
            group_provisioned=group_provisioned,
            id=id,
            labels=labels,
            name=name,
            state=state,
            token=token,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

        created_key_view.additional_properties = d
        return created_key_view

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
