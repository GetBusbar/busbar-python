from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_config_settings_config_document_modification_document_patch_set import (
        PutConfigSettingsConfigDocumentModificationDocumentPatchSet,
    )


T = TypeVar("T", bound="PutConfigSettingsConfigDocumentModificationDocumentPatch")


@_attrs_define(repr=False)
class PutConfigSettingsConfigDocumentModificationDocumentPatch:
    """Lowest-priority Store overlay over config.yaml, parsed with boot's schema. RFC6901 paths; strict sequence indices
    replace existing entries, terminal - appends. Within one request, indices name the input snapshot; sets precede
    descending removals. Each subsequent request addresses the current authored document. Null is a value, removal is
    explicit. Omitted values including secrets survive. Overlapping paths and edits shadowed by existing typed overlays
    are refused. Restart-only fields are reported. Patch history is bounded to 4096 total operations and 1 MiB; pointer
    depth is at most 128. Limit violations reject the transaction.

        Attributes:
            set_ (PutConfigSettingsConfigDocumentModificationDocumentPatchSet | Unset):
            remove (list[str] | Unset):
    """

    set_: PutConfigSettingsConfigDocumentModificationDocumentPatchSet | Unset = UNSET
    remove: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        set_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = self.set_.to_dict()

        remove: list[str] | Unset = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_settings_config_document_modification_document_patch_set import (
            PutConfigSettingsConfigDocumentModificationDocumentPatchSet,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _set_ = d.pop("set", UNSET)
        set_: PutConfigSettingsConfigDocumentModificationDocumentPatchSet | Unset
        if isinstance(_set_, Unset):
            set_ = UNSET
        else:
            set_ = PutConfigSettingsConfigDocumentModificationDocumentPatchSet.from_dict(_set_)

        remove = cast(list[str], d.pop("remove", UNSET))

        if d:
            raise ValueError("Unexpected fields for PutConfigSettingsConfigDocumentModificationDocumentPatch")
        put_config_settings_config_document_modification_document_patch = cls(
            set_=set_,
            remove=remove,
        )

        return put_config_settings_config_document_modification_document_patch
