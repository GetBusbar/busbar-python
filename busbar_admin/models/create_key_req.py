from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_key_req_labels import CreateKeyReqLabels


T = TypeVar("T", bound="CreateKeyReq")


@_attrs_define
class CreateKeyReq:
    """`POST /keys` body (1.5.0 signed-token keys, S1): PURE AUTH + a signed expiring token. A minted
    key is a busbar-signed `{sub, exp, kid}` token, returned ONCE. No rpm/tpm/budget on a key - all
    enforcement flows through the bound `group`. `#[serde(deny_unknown_fields)]` so the removed
    1.4.x fields (max_budget_cents/rpm_limit/tpm_limit/budget_period) fail loudly.

        Attributes:
            name (str):
            allowed_pools (list[str] | None | Unset): Pools this key may target. OMITTED = ALL pools; an explicit `[]` = NO
                pools (C6).
            expires_at (int | None | Unset): Token expiry as an absolute Unix-seconds timestamp. Mutually exclusive with
                `expires_in`.
            expires_in (None | str | Unset): Token lifetime as a duration string (`7d`, `24h`, `30m`, `3600s`) - the token's
                `exp` is
                `now + expires_in`. Mutually exclusive with `expires_at`. Absent (and no `expires_at`) => a
                sane long default (see `DEFAULT_KEY_TTL_SECS`).
            group (None | str | Unset): The `groups:` bucket this key binds to (at most one). A key with NO group is authed
                +
                unlimited (access only). If the named group EXISTS, the key binds to it. If it does NOT
                exist, the mint 400s UNLESS `parent` is given — then it is AUTO-PROVISIONED as a leaf under
                `parent` (self-service D2; see `parent`).
            issue_aws_credential (bool | Unset): When true, ALSO issue an AWS-style access-key-id + secret access key (the
                MinIO/S3-compatible
                model) so a Bedrock-SDK client can authenticate via inbound SigV4. Both are returned ONCE. Default: False.
            labels (CreateKeyReqLabels | Unset): Optional mint-time labels echoed onto this key's metric series; never
                interpreted by
                enforcement.
            parent (None | str | Unset): AUTO-PROVISION target: the EXISTING parent group under which to create
                `group` as a leaf when `group` does not yet exist — the first-self-mint materialization of a
                `user:<sub>` personal budget bucket. The new leaf's limits come from the nearest-ancestor
                `child_default` template (inherit-only when none up the chain), created through the same
                validate-at-the-door path as `POST /groups`. If `group` ALREADY exists, `parent` must equal
                its actual parent (else 409) — a mint never re-homes an existing group. Ignored when `group`
                is absent (a key with no group has nothing to provision).
    """

    name: str
    allowed_pools: list[str] | None | Unset = UNSET
    expires_at: int | None | Unset = UNSET
    expires_in: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    issue_aws_credential: bool | Unset = False
    labels: CreateKeyReqLabels | Unset = UNSET
    parent: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        allowed_pools: list[str] | None | Unset
        if isinstance(self.allowed_pools, Unset):
            allowed_pools = UNSET
        elif isinstance(self.allowed_pools, list):
            allowed_pools = self.allowed_pools

        else:
            allowed_pools = self.allowed_pools

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        expires_in: None | str | Unset
        if isinstance(self.expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = self.expires_in

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        issue_aws_credential = self.issue_aws_credential

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if allowed_pools is not UNSET:
            field_dict["allowed_pools"] = allowed_pools
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if group is not UNSET:
            field_dict["group"] = group
        if issue_aws_credential is not UNSET:
            field_dict["issue_aws_credential"] = issue_aws_credential
        if labels is not UNSET:
            field_dict["labels"] = labels
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_key_req_labels import CreateKeyReqLabels

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_allowed_pools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_pools_type_0 = cast(list[str], data)

                return allowed_pools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_pools = _parse_allowed_pools(d.pop("allowed_pools", UNSET))

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_expires_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_in = _parse_expires_in(d.pop("expires_in", UNSET))

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        issue_aws_credential = d.pop("issue_aws_credential", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: CreateKeyReqLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CreateKeyReqLabels.from_dict(_labels)

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        create_key_req = cls(
            name=name,
            allowed_pools=allowed_pools,
            expires_at=expires_at,
            expires_in=expires_in,
            group=group,
            issue_aws_credential=issue_aws_credential,
            labels=labels,
            parent=parent,
        )

        return create_key_req
