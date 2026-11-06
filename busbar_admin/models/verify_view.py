from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.verify_since import VerifySince


T = TypeVar("T", bound="VerifyView")


@_attrs_define(repr=False)
class VerifyView:
    """`GET /verify`: everything that has to be true of this node's ledger, checked. A failed
    verification is still a `200`; `ok` is the answer.

        Attributes:
            checkpoints (int): How many sealed checkpoints the node holds.
            since (None | VerifySince): The checkpoint the book was verified against (the last sealed one); null when none
                is sealed.
            book_verified (bool): Whether the book as it stands was measured against `since` (false with no checkpoint, or a
                node that binds no book).
            findings (list[str]): Each thing verification found, in words: a checkpoint edited after it was sealed, a node
                sequence that went backwards, a balance out of identity, a sealed balance no longer in the
                book, a closed window that moved, a balance whose counts the rate card refused to price.
            identity_holds (bool): Whether the ledger's postings reconcile with the previous release's rows.
            discrepancies (int): How many rows do not reconcile (`GET /ledger/reconciliation` names them).
            ok (bool): True when there is no finding and the identity holds.
    """

    checkpoints: int
    since: None | VerifySince
    book_verified: bool
    findings: list[str]
    identity_holds: bool
    discrepancies: int
    ok: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.verify_since import VerifySince  # noqa: PLC0415

        checkpoints = self.checkpoints

        since: dict[str, Any] | None
        if isinstance(self.since, VerifySince):
            since = self.since.to_dict()
        else:
            since = self.since

        book_verified = self.book_verified

        findings = self.findings

        identity_holds = self.identity_holds

        discrepancies = self.discrepancies

        ok = self.ok

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoints": checkpoints,
                "since": since,
                "book_verified": book_verified,
                "findings": findings,
                "identity_holds": identity_holds,
                "discrepancies": discrepancies,
                "ok": ok,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_since import VerifySince  # noqa: PLC0415

        d = dict(src_dict)
        checkpoints = d.pop("checkpoints")

        def _parse_since(data: object) -> None | VerifySince:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                since_type_0 = VerifySince.from_dict(data)

                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for since")

        since = _parse_since(d.pop("since"))

        book_verified = d.pop("book_verified")

        findings = cast(list[str], d.pop("findings"))

        identity_holds = d.pop("identity_holds")

        discrepancies = d.pop("discrepancies")

        ok = d.pop("ok")

        verify_view = cls(
            checkpoints=checkpoints,
            since=since,
            book_verified=book_verified,
            findings=findings,
            identity_holds=identity_holds,
            discrepancies=discrepancies,
            ok=ok,
        )

        verify_view.additional_properties = d
        return verify_view

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
