from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetActivityFeedResponse200DataItemDataType2")


@_attrs_define
class GetActivityFeedResponse200DataItemDataType2:
    """
    Attributes:
        followable_type (str): The followed type, lower-cased (title, character, comicevent, user, ...).
        followable_id (int):
        name (None | str): The followed entity, or null when it is gone.
        image_url (None | str): A followed title's cover; null for other types.
    """

    followable_type: str
    followable_id: int
    name: None | str
    image_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followable_type = self.followable_type

        followable_id = self.followable_id

        name: None | str
        name = self.name

        image_url: None | str
        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followable_type": followable_type,
                "followable_id": followable_id,
                "name": name,
                "image_url": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        followable_type = d.pop("followable_type")

        followable_id = d.pop("followable_id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        get_activity_feed_response_200_data_item_data_type_2 = cls(
            followable_type=followable_type,
            followable_id=followable_id,
            name=name,
            image_url=image_url,
        )

        get_activity_feed_response_200_data_item_data_type_2.additional_properties = d
        return get_activity_feed_response_200_data_item_data_type_2

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
