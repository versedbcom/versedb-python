from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_issue_in_collection_response_200_type_0_data_issue import (
        CheckIssueInCollectionResponse200Type0DataIssue,
    )


T = TypeVar("T", bound="CheckIssueInCollectionResponse200Type0Data")


@_attrs_define
class CheckIssueInCollectionResponse200Type0Data:
    """
    Attributes:
        id (int | Unset):
        condition (str | Unset):
        price_paid (float | Unset):
        issue (CheckIssueInCollectionResponse200Type0DataIssue | Unset):
    """

    id: int | Unset = UNSET
    condition: str | Unset = UNSET
    price_paid: float | Unset = UNSET
    issue: CheckIssueInCollectionResponse200Type0DataIssue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        condition = self.condition

        price_paid = self.price_paid

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
        if issue is not UNSET:
            field_dict["issue"] = issue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_issue_in_collection_response_200_type_0_data_issue import (
            CheckIssueInCollectionResponse200Type0DataIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        condition = d.pop("condition", UNSET)

        price_paid = d.pop("price_paid", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: CheckIssueInCollectionResponse200Type0DataIssue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = CheckIssueInCollectionResponse200Type0DataIssue.from_dict(_issue)

        check_issue_in_collection_response_200_type_0_data = cls(
            id=id,
            condition=condition,
            price_paid=price_paid,
            issue=issue,
        )

        check_issue_in_collection_response_200_type_0_data.additional_properties = d
        return check_issue_in_collection_response_200_type_0_data

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
