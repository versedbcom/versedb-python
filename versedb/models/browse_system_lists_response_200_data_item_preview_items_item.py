from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrowseSystemListsResponse200DataItemPreviewItemsItem")


@_attrs_define
class BrowseSystemListsResponse200DataItemPreviewItemsItem:
    """
    Attributes:
        id (int | Unset):
        image_url (str | Unset):
        is_nsfw (bool | Unset):
    """

    id: int | Unset = UNSET
    image_url: str | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image_url = self.image_url

        is_nsfw = self.is_nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        image_url = d.pop("image_url", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        browse_system_lists_response_200_data_item_preview_items_item = cls(
            id=id,
            image_url=image_url,
            is_nsfw=is_nsfw,
        )

        browse_system_lists_response_200_data_item_preview_items_item.additional_properties = d
        return browse_system_lists_response_200_data_item_preview_items_item

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
