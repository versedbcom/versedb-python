from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckIssueInCollectionResponse200Type1")


@_attrs_define
class CheckIssueInCollectionResponse200Type1:
    """Not in Collection

    Attributes:
        in_collection (bool | Unset):
        is_unreleased (bool | Unset):
        copies_count (int | Unset):
        copies (list[Any] | Unset):
        data (None | str | Unset):
    """

    in_collection: bool | Unset = UNSET
    is_unreleased: bool | Unset = UNSET
    copies_count: int | Unset = UNSET
    copies: list[Any] | Unset = UNSET
    data: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_collection = self.in_collection

        is_unreleased = self.is_unreleased

        copies_count = self.copies_count

        copies: list[Any] | Unset = UNSET
        if not isinstance(self.copies, Unset):
            copies = self.copies

        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_collection is not UNSET:
            field_dict["in_collection"] = in_collection
        if is_unreleased is not UNSET:
            field_dict["is_unreleased"] = is_unreleased
        if copies_count is not UNSET:
            field_dict["copies_count"] = copies_count
        if copies is not UNSET:
            field_dict["copies"] = copies
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_collection = d.pop("in_collection", UNSET)

        is_unreleased = d.pop("is_unreleased", UNSET)

        copies_count = d.pop("copies_count", UNSET)

        copies = cast(list[Any], d.pop("copies", UNSET))

        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        check_issue_in_collection_response_200_type_1 = cls(
            in_collection=in_collection,
            is_unreleased=is_unreleased,
            copies_count=copies_count,
            copies=copies,
            data=data,
        )

        check_issue_in_collection_response_200_type_1.additional_properties = d
        return check_issue_in_collection_response_200_type_1

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
