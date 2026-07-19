from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatedKeyView")


@_attrs_define
class CreatedKeyView:
    """`POST /keys` (mint) — the key metadata plus the ONCE-shown secret, and (when an AWS SigV4
    credential was requested) the AccessKeyId + secret access key. The AWS fields are absent on a
    bearer-only mint.

        Attributes:
            allowed_pools (list[str]):
            budget_period (str):
            created_at (int):
            enabled (bool):
            id (str):
            max_budget_cents (int | None):
            name (str):
            rpm_limit (int | None):
            secret (str): The bearer secret — shown EXACTLY once, never returned by any read.
            tpm_limit (int | None):
            aws_access_key_id (None | str | Unset): AWS AccessKeyId (present only when `issue_aws_credential` was set). Not
                secret.
            aws_secret_access_key (None | str | Unset): AWS SigV4 secret access key — shown once (present only with an AWS
                credential).
    """

    allowed_pools: list[str]
    budget_period: str
    created_at: int
    enabled: bool
    id: str
    max_budget_cents: int | None
    name: str
    rpm_limit: int | None
    secret: str
    tpm_limit: int | None
    aws_access_key_id: None | str | Unset = UNSET
    aws_secret_access_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_pools = self.allowed_pools

        budget_period = self.budget_period

        created_at = self.created_at

        enabled = self.enabled

        id = self.id

        max_budget_cents: int | None
        max_budget_cents = self.max_budget_cents

        name = self.name

        rpm_limit: int | None
        rpm_limit = self.rpm_limit

        secret = self.secret

        tpm_limit: int | None
        tpm_limit = self.tpm_limit

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
                "budget_period": budget_period,
                "created_at": created_at,
                "enabled": enabled,
                "id": id,
                "max_budget_cents": max_budget_cents,
                "name": name,
                "rpm_limit": rpm_limit,
                "secret": secret,
                "tpm_limit": tpm_limit,
            }
        )
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_pools = cast(list[str], d.pop("allowed_pools"))

        budget_period = d.pop("budget_period")

        created_at = d.pop("created_at")

        enabled = d.pop("enabled")

        id = d.pop("id")

        def _parse_max_budget_cents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_budget_cents = _parse_max_budget_cents(d.pop("max_budget_cents"))

        name = d.pop("name")

        def _parse_rpm_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit"))

        secret = d.pop("secret")

        def _parse_tpm_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit"))

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
            budget_period=budget_period,
            created_at=created_at,
            enabled=enabled,
            id=id,
            max_budget_cents=max_budget_cents,
            name=name,
            rpm_limit=rpm_limit,
            secret=secret,
            tpm_limit=tpm_limit,
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
