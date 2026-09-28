from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_issue_in_collection_response_200_type_0_copies_item import (
        CheckIssueInCollectionResponse200Type0CopiesItem,
    )
    from ..models.check_issue_in_collection_response_200_type_0_data import CheckIssueInCollectionResponse200Type0Data


T = TypeVar("T", bound="CheckIssueInCollectionResponse200Type0")


@_attrs_define
class CheckIssueInCollectionResponse200Type0:
    """In Collection

    Attributes:
        in_collection (bool | Unset):
        is_unreleased (bool | Unset):
        copies_count (int | Unset):
        copies (list[CheckIssueInCollectionResponse200Type0CopiesItem] | Unset):
        data (CheckIssueInCollectionResponse200Type0Data | Unset):
    """

    in_collection: bool | Unset = UNSET
    is_unreleased: bool | Unset = UNSET
    copies_count: int | Unset = UNSET
    copies: list[CheckIssueInCollectionResponse200Type0CopiesItem] | Unset = UNSET
    data: CheckIssueInCollectionResponse200Type0Data | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_collection = self.in_collection

        is_unreleased = self.is_unreleased

        copies_count = self.copies_count

        copies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.copies, Unset):
            copies = []
            for copies_item_data in self.copies:
                copies_item = copies_item_data.to_dict()
                copies.append(copies_item)

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.check_issue_in_collection_response_200_type_0_copies_item import (
            CheckIssueInCollectionResponse200Type0CopiesItem,  # noqa: PLC0415
        )
        from ..models.check_issue_in_collection_response_200_type_0_data import (
            CheckIssueInCollectionResponse200Type0Data,  # noqa: PLC0415
        )

        d = dict(src_dict)
        in_collection = d.pop("in_collection", UNSET)

        is_unreleased = d.pop("is_unreleased", UNSET)

        copies_count = d.pop("copies_count", UNSET)

        _copies = d.pop("copies", UNSET)
        copies: list[CheckIssueInCollectionResponse200Type0CopiesItem] | Unset = UNSET
        if _copies is not UNSET:
            copies = []
            for copies_item_data in _copies:
                copies_item = CheckIssueInCollectionResponse200Type0CopiesItem.from_dict(copies_item_data)

                copies.append(copies_item)

        _data = d.pop("data", UNSET)
        data: CheckIssueInCollectionResponse200Type0Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CheckIssueInCollectionResponse200Type0Data.from_dict(_data)

        check_issue_in_collection_response_200_type_0 = cls(
            in_collection=in_collection,
            is_unreleased=is_unreleased,
            copies_count=copies_count,
            copies=copies,
            data=data,
        )

        check_issue_in_collection_response_200_type_0.additional_properties = d
        return check_issue_in_collection_response_200_type_0

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
