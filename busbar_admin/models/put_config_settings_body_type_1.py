from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_config_settings_body_type_1_document_patch import PutConfigSettingsBodyType1DocumentPatch
    from ..models.put_config_settings_body_type_1_providers_patch import PutConfigSettingsBodyType1ProvidersPatch


T = TypeVar("T", bound="PutConfigSettingsBodyType1")


@_attrs_define(repr=False)
class PutConfigSettingsBodyType1:
    """
    Attributes:
        document_patch (PutConfigSettingsBodyType1DocumentPatch): Lowest-priority Store overlay over config.yaml, parsed
            with boot's schema. RFC6901 paths; strict sequence indices replace existing entries, terminal - appends. Within
            one request, indices name the input snapshot; sets precede descending removals. Each subsequent request
            addresses the current authored document. Null is a value, removal is explicit. Omitted values including secrets
            survive. Overlapping paths and edits shadowed by existing typed overlays are refused. Restart-only fields are
            reported. Patch history is bounded to 4096 total operations and 1 MiB; pointer depth is at most 128. Limit
            violations reject the transaction.
        providers_patch (PutConfigSettingsBodyType1ProvidersPatch | Unset): Edits providers.yaml through its boot
            grammar in the same Store transaction. Paths start with catalog entry names. Deployment overrides that shadow an
            edit are refused.
        reset_providers_paths (list[str] | Unset): Forget only these exact prior catalog edits before merging
            providers_patch.
        reset_document_paths (list[str] | Unset): Forget only these exact prior document edits before merging the new
            edit; typed overlays are never removed.
    """

    document_patch: PutConfigSettingsBodyType1DocumentPatch
    providers_patch: PutConfigSettingsBodyType1ProvidersPatch | Unset = UNSET
    reset_providers_paths: list[str] | Unset = UNSET
    reset_document_paths: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        document_patch = self.document_patch.to_dict()

        providers_patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers_patch, Unset):
            providers_patch = self.providers_patch.to_dict()

        reset_providers_paths: list[str] | Unset = UNSET
        if not isinstance(self.reset_providers_paths, Unset):
            reset_providers_paths = self.reset_providers_paths

        reset_document_paths: list[str] | Unset = UNSET
        if not isinstance(self.reset_document_paths, Unset):
            reset_document_paths = self.reset_document_paths

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "document_patch": document_patch,
            }
        )
        if providers_patch is not UNSET:
            field_dict["providers_patch"] = providers_patch
        if reset_providers_paths is not UNSET:
            field_dict["reset_providers_paths"] = reset_providers_paths
        if reset_document_paths is not UNSET:
            field_dict["reset_document_paths"] = reset_document_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_settings_body_type_1_document_patch import PutConfigSettingsBodyType1DocumentPatch  # noqa: PLC0415
        from ..models.put_config_settings_body_type_1_providers_patch import PutConfigSettingsBodyType1ProvidersPatch  # noqa: PLC0415

        d = dict(src_dict)
        document_patch = PutConfigSettingsBodyType1DocumentPatch.from_dict(d.pop("document_patch"))

        _providers_patch = d.pop("providers_patch", UNSET)
        providers_patch: PutConfigSettingsBodyType1ProvidersPatch | Unset
        if isinstance(_providers_patch, Unset):
            providers_patch = UNSET
        else:
            providers_patch = PutConfigSettingsBodyType1ProvidersPatch.from_dict(_providers_patch)

        reset_providers_paths = cast(list[str], d.pop("reset_providers_paths", UNSET))

        reset_document_paths = cast(list[str], d.pop("reset_document_paths", UNSET))

        if d:
            raise ValueError("Unexpected fields for PutConfigSettingsBodyType1")
        put_config_settings_body_type_1 = cls(
            document_patch=document_patch,
            providers_patch=providers_patch,
            reset_providers_paths=reset_providers_paths,
            reset_document_paths=reset_document_paths,
        )

        return put_config_settings_body_type_1
