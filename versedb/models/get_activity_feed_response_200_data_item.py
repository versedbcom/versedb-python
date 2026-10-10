from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_activity_feed_response_200_data_item_data import GetActivityFeedResponse200DataItemData


T = TypeVar("T", bound="GetActivityFeedResponse200DataItem")


@_attrs_define
class GetActivityFeedResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        action (str | Unset):
        created_at (str | Unset):
        data (GetActivityFeedResponse200DataItemData | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    action: str | Unset = UNSET
    created_at: str | Unset = UNSET
    data: GetActivityFeedResponse200DataItemData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        action = self.action

        created_at = self.created_at

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_feed_response_200_data_item_data import GetActivityFeedResponse200DataItemData  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        action = d.pop("action", UNSET)

        created_at = d.pop("created_at", UNSET)

        _data = d.pop("data", UNSET)
        data: GetActivityFeedResponse200DataItemData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetActivityFeedResponse200DataItemData.from_dict(_data)

        get_activity_feed_response_200_data_item = cls(
            id=id,
            type_=type_,
            action=action,
            created_at=created_at,
            data=data,
        )

        get_activity_feed_response_200_data_item.additional_properties = d
        return get_activity_feed_response_200_data_item

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
