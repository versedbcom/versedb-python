from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWishlistResponse200DataItemEntitySeries")


@_attrs_define
class ListWishlistResponse200DataItemEntitySeries:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        start_year (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    start_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        start_year = self.start_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if start_year is not UNSET:
            field_dict["start_year"] = start_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        start_year = d.pop("start_year", UNSET)

        list_wishlist_response_200_data_item_entity_series = cls(
            id=id,
            name=name,
            start_year=start_year,
        )

        list_wishlist_response_200_data_item_entity_series.additional_properties = d
        return list_wishlist_response_200_data_item_entity_series

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
