from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAComicShopResponse200DataRelatedShopsItem")


@_attrs_define
class GetAComicShopResponse200DataRelatedShopsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        city (None | str):
        state_province (None | str):
        country (None | str):
        logo_url (None | str):
        url (str):
    """

    id: int
    name: None | str
    slug: None | str
    city: None | str
    state_province: None | str
    country: None | str
    logo_url: None | str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        city: None | str
        city = self.city

        state_province: None | str
        state_province = self.state_province

        country: None | str
        country = self.country

        logo_url: None | str
        logo_url = self.logo_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "city": city,
                "state_province": state_province,
                "country": country,
                "logo_url": logo_url,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state_province(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_province = _parse_state_province(d.pop("state_province"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        url = d.pop("url")

        get_a_comic_shop_response_200_data_related_shops_item = cls(
            id=id,
            name=name,
            slug=slug,
            city=city,
            state_province=state_province,
            country=country,
            logo_url=logo_url,
            url=url,
        )

        get_a_comic_shop_response_200_data_related_shops_item.additional_properties = d
        return get_a_comic_shop_response_200_data_related_shops_item

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
