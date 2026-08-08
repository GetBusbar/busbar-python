from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_bucket_usage_view import GroupBucketUsageView


T = TypeVar("T", bound="GroupUsageView")


@_attrs_define
class GroupUsageView:
    """`GET /groups/{name}/usage`: one group's DERIVED current-window usage, one row per
    enforcement bucket (each `(window, pool?)` its limits materialise), against that bucket's
    caps. The dashboard read: spend/tokens/requests per tier vs the budgets, straight off the
    ledger x the CURRENT rate card (reprice-on-read, nothing stored). The customer's self-service
    tool consumes this per group (`user:<sub>` leaf = one person's view) and re-scopes it.

        Attributes:
            as_of (int): Epoch seconds the read was taken at (the windows below are current AS OF this instant).
            buckets (list[GroupBucketUsageView]): One row per enforcement bucket, in the group's resolved bucket order.
                Empty for a group
                with only a `concurrent` limit (or none); there is no windowed ledger to read.
            enabled (bool): `false` = the group is FROZEN (`enabled: false`): every request through it rejects.
            group (str): The group name (echoed from the path).
    """

    as_of: int
    buckets: list[GroupBucketUsageView]
    enabled: bool
    group: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        enabled = self.enabled

        group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "buckets": buckets,
                "enabled": enabled,
                "group": group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_bucket_usage_view import GroupBucketUsageView

        d = dict(src_dict)
        as_of = d.pop("as_of")

        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = GroupBucketUsageView.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        enabled = d.pop("enabled")

        group = d.pop("group")

        group_usage_view = cls(
            as_of=as_of,
            buckets=buckets,
            enabled=enabled,
            group=group,
        )

        group_usage_view.additional_properties = d
        return group_usage_view

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
