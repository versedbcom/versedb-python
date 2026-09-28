from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeriesDetailsResponse200DataCreatorsItem")


@_attrs_define
class GetSeriesDetailsResponse200DataCreatorsItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        photo_url (str | Unset):
        role (str | Unset):
        is_uncredited (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    photo_url: str | Unset = UNSET
    role: str | Unset = UNSET
    is_uncredited: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        photo_url = self.photo_url

        role = self.role

        is_uncredited = self.is_uncredited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url
        if role is not UNSET:
            field_dict["role"] = role
        if is_uncredited is not UNSET:
            field_dict["is_uncredited"] = is_uncredited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        photo_url = d.pop("photo_url", UNSET)

        role = d.pop("role", UNSET)

        is_uncredited = d.pop("is_uncredited", UNSET)

        get_series_details_response_200_data_creators_item = cls(
            id=id,
            name=name,
            slug=slug,
            photo_url=photo_url,
            role=role,
            is_uncredited=is_uncredited,
        )

        get_series_details_response_200_data_creators_item.additional_properties = d
        return get_series_details_response_200_data_creators_item

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
