from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeAListIntoThisOneBody")


@_attrs_define
class MergeAListIntoThisOneBody:
    """
    Attributes:
        source_list_id (int): The list to merge in.
        delete_source (bool | Unset): Delete the source list after merging. Defaults to false.
    """

    source_list_id: int
    delete_source: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_list_id = self.source_list_id

        delete_source = self.delete_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_list_id": source_list_id,
            }
        )
        if delete_source is not UNSET:
            field_dict["delete_source"] = delete_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_list_id = d.pop("source_list_id")

        delete_source = d.pop("delete_source", UNSET)

        merge_a_list_into_this_one_body = cls(
            source_list_id=source_list_id,
            delete_source=delete_source,
        )

        merge_a_list_into_this_one_body.additional_properties = d
        return merge_a_list_into_this_one_body

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
