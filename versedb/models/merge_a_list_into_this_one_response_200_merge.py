from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeAListIntoThisOneResponse200Merge")


@_attrs_define
class MergeAListIntoThisOneResponse200Merge:
    """
    Attributes:
        moved (int | Unset):
        skipped_duplicates (int | Unset):
        converted_to_mixed (bool | Unset):
        source_deleted (bool | Unset):
    """

    moved: int | Unset = UNSET
    skipped_duplicates: int | Unset = UNSET
    converted_to_mixed: bool | Unset = UNSET
    source_deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        moved = self.moved

        skipped_duplicates = self.skipped_duplicates

        converted_to_mixed = self.converted_to_mixed

        source_deleted = self.source_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moved is not UNSET:
            field_dict["moved"] = moved
        if skipped_duplicates is not UNSET:
            field_dict["skipped_duplicates"] = skipped_duplicates
        if converted_to_mixed is not UNSET:
            field_dict["converted_to_mixed"] = converted_to_mixed
        if source_deleted is not UNSET:
            field_dict["source_deleted"] = source_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        moved = d.pop("moved", UNSET)

        skipped_duplicates = d.pop("skipped_duplicates", UNSET)

        converted_to_mixed = d.pop("converted_to_mixed", UNSET)

        source_deleted = d.pop("source_deleted", UNSET)

        merge_a_list_into_this_one_response_200_merge = cls(
            moved=moved,
            skipped_duplicates=skipped_duplicates,
            converted_to_mixed=converted_to_mixed,
            source_deleted=source_deleted,
        )

        merge_a_list_into_this_one_response_200_merge.additional_properties = d
        return merge_a_list_into_this_one_response_200_merge

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
