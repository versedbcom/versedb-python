from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSeriesDetailsResponse200DataCharactersItem")


@_attrs_define
class GetSeriesDetailsResponse200DataCharactersItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        real_name (None | str):
        aliases (list[Any]):
        image_url (None | str):
        appearances_count (int):
    """

    id: int
    name: None | str
    slug: None | str
    real_name: None | str
    aliases: list[Any]
    image_url: None | str
    appearances_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        real_name: None | str
        real_name = self.real_name

        aliases = self.aliases

        image_url: None | str
        image_url = self.image_url

        appearances_count = self.appearances_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "real_name": real_name,
                "aliases": aliases,
                "image_url": image_url,
                "appearances_count": appearances_count,
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

        def _parse_real_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        real_name = _parse_real_name(d.pop("real_name"))

        aliases = cast(list[Any], d.pop("aliases"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        appearances_count = d.pop("appearances_count")

        get_series_details_response_200_data_characters_item = cls(
            id=id,
            name=name,
            slug=slug,
            real_name=real_name,
            aliases=aliases,
            image_url=image_url,
            appearances_count=appearances_count,
        )

        get_series_details_response_200_data_characters_item.additional_properties = d
        return get_series_details_response_200_data_characters_item

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
