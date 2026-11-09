from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FollowUpdatesResponse200Meta")


@_attrs_define
class FollowUpdatesResponse200Meta:
    """
    Attributes:
        days (int):
        total_follows (int):
        current_page (int):
        per_page (int):
        total (int):
        last_page (int):
    """

    days: int
    total_follows: int
    current_page: int
    per_page: int
    total: int
    last_page: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        total_follows = self.total_follows

        current_page = self.current_page

        per_page = self.per_page

        total = self.total

        last_page = self.last_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "total_follows": total_follows,
                "current_page": current_page,
                "per_page": per_page,
                "total": total,
                "last_page": last_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days")

        total_follows = d.pop("total_follows")

        current_page = d.pop("current_page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        last_page = d.pop("last_page")

        follow_updates_response_200_meta = cls(
            days=days,
            total_follows=total_follows,
            current_page=current_page,
            per_page=per_page,
            total=total,
            last_page=last_page,
        )

        follow_updates_response_200_meta.additional_properties = d
        return follow_updates_response_200_meta

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
