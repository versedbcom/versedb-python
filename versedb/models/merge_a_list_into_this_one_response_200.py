from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merge_a_list_into_this_one_response_200_data import MergeAListIntoThisOneResponse200Data
    from ..models.merge_a_list_into_this_one_response_200_merge import MergeAListIntoThisOneResponse200Merge


T = TypeVar("T", bound="MergeAListIntoThisOneResponse200")


@_attrs_define
class MergeAListIntoThisOneResponse200:
    """
    Attributes:
        data (MergeAListIntoThisOneResponse200Data | Unset):
        merge (MergeAListIntoThisOneResponse200Merge | Unset):
    """

    data: MergeAListIntoThisOneResponse200Data | Unset = UNSET
    merge: MergeAListIntoThisOneResponse200Merge | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        merge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge, Unset):
            merge = self.merge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if merge is not UNSET:
            field_dict["merge"] = merge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merge_a_list_into_this_one_response_200_data import (
            MergeAListIntoThisOneResponse200Data,  # noqa: PLC0415
        )
        from ..models.merge_a_list_into_this_one_response_200_merge import (
            MergeAListIntoThisOneResponse200Merge,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: MergeAListIntoThisOneResponse200Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = MergeAListIntoThisOneResponse200Data.from_dict(_data)

        _merge = d.pop("merge", UNSET)
        merge: MergeAListIntoThisOneResponse200Merge | Unset
        if isinstance(_merge, Unset):
            merge = UNSET
        else:
            merge = MergeAListIntoThisOneResponse200Merge.from_dict(_merge)

        merge_a_list_into_this_one_response_200 = cls(
            data=data,
            merge=merge,
        )

        merge_a_list_into_this_one_response_200.additional_properties = d
        return merge_a_list_into_this_one_response_200

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
