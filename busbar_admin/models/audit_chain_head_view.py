from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_chain_signed_head import AuditChainSignedHead


T = TypeVar("T", bound="AuditChainHeadView")


@_attrs_define(repr=False)
class AuditChainHeadView:
    """`GET /audit/head`: where the audit record chain is now, and the recipe a verifier applies.

    Attributes:
        recipe (str): The name of the published digest recipe.
        signature_domain (str): The signature domain-separation string.
        algorithm (str): The signature algorithm.
        next_seq (int): The position the NEXT record will take.
        head (AuditChainSignedHead | None): The tip, or null when the chain has sealed nothing (a true answer, not an
            error).
    """

    recipe: str
    signature_domain: str
    algorithm: str
    next_seq: int
    head: AuditChainSignedHead | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415

        recipe = self.recipe

        signature_domain = self.signature_domain

        algorithm = self.algorithm

        next_seq = self.next_seq

        head: dict[str, Any] | None
        if isinstance(self.head, AuditChainSignedHead):
            head = self.head.to_dict()
        else:
            head = self.head

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipe": recipe,
                "signature_domain": signature_domain,
                "algorithm": algorithm,
                "next_seq": next_seq,
                "head": head,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415

        d = dict(src_dict)
        recipe = d.pop("recipe")

        signature_domain = d.pop("signature_domain")

        algorithm = d.pop("algorithm")

        next_seq = d.pop("next_seq")

        def _parse_head(data: object) -> AuditChainSignedHead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                head_type_0 = AuditChainSignedHead.from_dict(data)

                return head_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for head")

        head = _parse_head(d.pop("head"))

        audit_chain_head_view = cls(
            recipe=recipe,
            signature_domain=signature_domain,
            algorithm=algorithm,
            next_seq=next_seq,
            head=head,
        )

        audit_chain_head_view.additional_properties = d
        return audit_chain_head_view

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
