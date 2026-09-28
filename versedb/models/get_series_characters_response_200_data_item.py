from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeriesCharactersResponse200DataItem")


@_attrs_define
class GetSeriesCharactersResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        alias (str | Unset):
        image_url (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    alias: str | Unset = UNSET
    image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        alias = self.alias

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        image_url = d.pop("image_url", UNSET)

        get_series_characters_response_200_data_item = cls(
            id=id,
            name=name,
            alias=alias,
            image_url=image_url,
        )

        get_series_characters_response_200_data_item.additional_properties = d
        return get_series_characters_response_200_data_item

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
