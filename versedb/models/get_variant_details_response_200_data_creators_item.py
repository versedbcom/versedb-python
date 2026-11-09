from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetVariantDetailsResponse200DataCreatorsItem")


@_attrs_define
class GetVariantDetailsResponse200DataCreatorsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        photo_url (None | str):
        role (str):
        is_uncredited (bool):
    """

    id: int
    name: None | str
    slug: None | str
    photo_url: None | str
    role: str
    is_uncredited: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        photo_url: None | str
        photo_url = self.photo_url

        role = self.role

        is_uncredited = self.is_uncredited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "photo_url": photo_url,
                "role": role,
                "is_uncredited": is_uncredited,
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

        def _parse_photo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        photo_url = _parse_photo_url(d.pop("photo_url"))

        role = d.pop("role")

        is_uncredited = d.pop("is_uncredited")

        get_variant_details_response_200_data_creators_item = cls(
            id=id,
            name=name,
            slug=slug,
            photo_url=photo_url,
            role=role,
            is_uncredited=is_uncredited,
        )

        get_variant_details_response_200_data_creators_item.additional_properties = d
        return get_variant_details_response_200_data_creators_item

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
