from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddItemToListResponse201DataVariant")


@_attrs_define
class AddItemToListResponse201DataVariant:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        cover_image_url (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        cover_image_url = self.cover_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        add_item_to_list_response_201_data_variant = cls(
            id=id,
            name=name,
            cover_image_url=cover_image_url,
        )

        add_item_to_list_response_201_data_variant.additional_properties = d
        return add_item_to_list_response_201_data_variant

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
