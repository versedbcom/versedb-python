from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeriesDetailsResponse200DataCharactersItem")


@_attrs_define
class GetSeriesDetailsResponse200DataCharactersItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        real_name (str | Unset):
        aliases (list[Any] | Unset):
        image_url (str | Unset):
        appearances_count (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    real_name: str | Unset = UNSET
    aliases: list[Any] | Unset = UNSET
    image_url: str | Unset = UNSET
    appearances_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        real_name = self.real_name

        aliases: list[Any] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        image_url = self.image_url

        appearances_count = self.appearances_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if real_name is not UNSET:
            field_dict["real_name"] = real_name
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if appearances_count is not UNSET:
            field_dict["appearances_count"] = appearances_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        real_name = d.pop("real_name", UNSET)

        aliases = cast(list[Any], d.pop("aliases", UNSET))

        image_url = d.pop("image_url", UNSET)

        appearances_count = d.pop("appearances_count", UNSET)

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
