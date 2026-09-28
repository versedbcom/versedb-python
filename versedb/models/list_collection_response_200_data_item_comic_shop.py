from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCollectionResponse200DataItemComicShop")


@_attrs_define
class ListCollectionResponse200DataItemComicShop:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        city (str | Unset):
        state_province (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    city: str | Unset = UNSET
    state_province: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        city = self.city

        state_province = self.state_province

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["state_province"] = state_province

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        city = d.pop("city", UNSET)

        state_province = d.pop("state_province", UNSET)

        list_collection_response_200_data_item_comic_shop = cls(
            id=id,
            name=name,
            slug=slug,
            city=city,
            state_province=state_province,
        )

        list_collection_response_200_data_item_comic_shop.additional_properties = d
        return list_collection_response_200_data_item_comic_shop

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
