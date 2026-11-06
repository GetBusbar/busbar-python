from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SigningKeyRotateView")


@_attrs_define(repr=False)
class SigningKeyRotateView:
    """`POST /signing-key/rotate`: the current key-signing key id plus the REVOKE-ALL warning. 1.5.0 is
    single-key: the actual swap is an operator action, so this reports intent, not an in-process swap.

        Attributes:
            current_kid (str): The current signing-key id (`kid`) that tokens are minted under.
            revoke_all (bool): Always `true`: rotating the signing key revokes every outstanding key (all must be re-
                minted).
            message (str): Human-readable guidance for the operator-driven lockstep rotation.
    """

    current_kid: str
    revoke_all: bool
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_kid = self.current_kid

        revoke_all = self.revoke_all

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_kid": current_kid,
                "revoke_all": revoke_all,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_kid = d.pop("current_kid")

        revoke_all = d.pop("revoke_all")

        message = d.pop("message")

        signing_key_rotate_view = cls(
            current_kid=current_kid,
            revoke_all=revoke_all,
            message=message,
        )

        signing_key_rotate_view.additional_properties = d
        return signing_key_rotate_view

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
