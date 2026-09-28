from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_follows_response_200_data_item_followable import ListFollowsResponse200DataItemFollowable


T = TypeVar("T", bound="ListFollowsResponse200DataItem")


@_attrs_define
class ListFollowsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        followable_type (str | Unset):
        followable_id (int | Unset):
        followable (ListFollowsResponse200DataItemFollowable | Unset):
        created_at (str | Unset):
    """

    id: int | Unset = UNSET
    followable_type: str | Unset = UNSET
    followable_id: int | Unset = UNSET
    followable: ListFollowsResponse200DataItemFollowable | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        followable_type = self.followable_type

        followable_id = self.followable_id

        followable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.followable, Unset):
            followable = self.followable.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if followable_type is not UNSET:
            field_dict["followable_type"] = followable_type
        if followable_id is not UNSET:
            field_dict["followable_id"] = followable_id
        if followable is not UNSET:
            field_dict["followable"] = followable
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_follows_response_200_data_item_followable import (
            ListFollowsResponse200DataItemFollowable,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        followable_type = d.pop("followable_type", UNSET)

        followable_id = d.pop("followable_id", UNSET)

        _followable = d.pop("followable", UNSET)
        followable: ListFollowsResponse200DataItemFollowable | Unset
        if isinstance(_followable, Unset):
            followable = UNSET
        else:
            followable = ListFollowsResponse200DataItemFollowable.from_dict(_followable)

        created_at = d.pop("created_at", UNSET)

        list_follows_response_200_data_item = cls(
            id=id,
            followable_type=followable_type,
            followable_id=followable_id,
            followable=followable,
            created_at=created_at,
        )

        list_follows_response_200_data_item.additional_properties = d
        return list_follows_response_200_data_item

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
