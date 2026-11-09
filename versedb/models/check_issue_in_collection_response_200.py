from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.check_issue_in_collection_response_200_copies_item import CheckIssueInCollectionResponse200CopiesItem
    from ..models.check_issue_in_collection_response_200_data_type_0 import CheckIssueInCollectionResponse200DataType0


T = TypeVar("T", bound="CheckIssueInCollectionResponse200")


@_attrs_define
class CheckIssueInCollectionResponse200:
    """
    Attributes:
        in_collection (bool):
        is_unreleased (bool): The issue is more than a day from its release, so it cannot be added yet.
        copies_count (int):
        copies (list[CheckIssueInCollectionResponse200CopiesItem]):
        data (CheckIssueInCollectionResponse200DataType0 | None): The first copy, or null when there is none.
    """

    in_collection: bool
    is_unreleased: bool
    copies_count: int
    copies: list[CheckIssueInCollectionResponse200CopiesItem]
    data: CheckIssueInCollectionResponse200DataType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.check_issue_in_collection_response_200_data_type_0 import (
            CheckIssueInCollectionResponse200DataType0,  # noqa: PLC0415
        )

        in_collection = self.in_collection

        is_unreleased = self.is_unreleased

        copies_count = self.copies_count

        copies = []
        for copies_item_data in self.copies:
            copies_item = copies_item_data.to_dict()
            copies.append(copies_item)

        data: dict[str, Any] | None
        if isinstance(self.data, CheckIssueInCollectionResponse200DataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in_collection": in_collection,
                "is_unreleased": is_unreleased,
                "copies_count": copies_count,
                "copies": copies,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_issue_in_collection_response_200_copies_item import (
            CheckIssueInCollectionResponse200CopiesItem,  # noqa: PLC0415
        )
        from ..models.check_issue_in_collection_response_200_data_type_0 import (
            CheckIssueInCollectionResponse200DataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        in_collection = d.pop("in_collection")

        is_unreleased = d.pop("is_unreleased")

        copies_count = d.pop("copies_count")

        copies = []
        _copies = d.pop("copies")
        for copies_item_data in _copies:
            copies_item = CheckIssueInCollectionResponse200CopiesItem.from_dict(copies_item_data)

            copies.append(copies_item)

        def _parse_data(data: object) -> CheckIssueInCollectionResponse200DataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CheckIssueInCollectionResponse200DataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckIssueInCollectionResponse200DataType0 | None, data)

        data = _parse_data(d.pop("data"))

        check_issue_in_collection_response_200 = cls(
            in_collection=in_collection,
            is_unreleased=is_unreleased,
            copies_count=copies_count,
            copies=copies,
            data=data,
        )

        check_issue_in_collection_response_200.additional_properties = d
        return check_issue_in_collection_response_200

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
