from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_comic_shops_response_200_data_item_images import ListComicShopsResponse200DataItemImages


T = TypeVar("T", bound="ListComicShopsResponse200DataItem")


@_attrs_define
class ListComicShopsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        city (str | Unset):
        state_province (str | Unset):
        country (str | Unset):
        logo_url (str | Unset):
        images (ListComicShopsResponse200DataItemImages | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    city: str | Unset = UNSET
    state_province: str | Unset = UNSET
    country: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: ListComicShopsResponse200DataItemImages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        city = self.city

        state_province = self.state_province

        country = self.country

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["state_province"] = state_province
        if country is not UNSET:
            field_dict["country"] = country
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_comic_shops_response_200_data_item_images import (
            ListComicShopsResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        city = d.pop("city", UNSET)

        state_province = d.pop("state_province", UNSET)

        country = d.pop("country", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListComicShopsResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListComicShopsResponse200DataItemImages.from_dict(_images)

        list_comic_shops_response_200_data_item = cls(
            id=id,
            name=name,
            city=city,
            state_province=state_province,
            country=country,
            logo_url=logo_url,
            images=images,
        )

        list_comic_shops_response_200_data_item.additional_properties = d
        return list_comic_shops_response_200_data_item

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
