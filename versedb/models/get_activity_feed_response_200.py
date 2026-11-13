from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_activity_feed_response_200_data_item import GetActivityFeedResponse200DataItem
    from ..models.get_activity_feed_response_200_meta import GetActivityFeedResponse200Meta


T = TypeVar("T", bound="GetActivityFeedResponse200")


@_attrs_define
class GetActivityFeedResponse200:
    """
    Attributes:
        data (list[GetActivityFeedResponse200DataItem]):
        meta (GetActivityFeedResponse200Meta):
    """

    data: list[GetActivityFeedResponse200DataItem]
    meta: GetActivityFeedResponse200Meta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_feed_response_200_data_item import GetActivityFeedResponse200DataItem  # noqa: PLC0415
        from ..models.get_activity_feed_response_200_meta import GetActivityFeedResponse200Meta  # noqa: PLC0415

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetActivityFeedResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        meta = GetActivityFeedResponse200Meta.from_dict(d.pop("meta"))

        get_activity_feed_response_200 = cls(
            data=data,
            meta=meta,
        )

        get_activity_feed_response_200.additional_properties = d
        return get_activity_feed_response_200

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
