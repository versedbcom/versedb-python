from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeAListIntoThisOneResponse200Data")


@_attrs_define
class MergeAListIntoThisOneResponse200Data:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        item_types (list[str] | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    item_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        item_types: list[str] | Unset = UNSET
        if not isinstance(self.item_types, Unset):
            item_types = self.item_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if item_types is not UNSET:
            field_dict["item_types"] = item_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        item_types = cast(list[str], d.pop("item_types", UNSET))

        merge_a_list_into_this_one_response_200_data = cls(
            id=id,
            title=title,
            item_types=item_types,
        )

        merge_a_list_into_this_one_response_200_data.additional_properties = d
        return merge_a_list_into_this_one_response_200_data

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
