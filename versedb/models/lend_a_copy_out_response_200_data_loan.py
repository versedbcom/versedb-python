from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LendACopyOutResponse200DataLoan")


@_attrs_define
class LendACopyOutResponse200DataLoan:
    """
    Attributes:
        id (int | Unset):
        loaned_to (str | Unset):
        loaned_at (str | Unset):
        due_at (str | Unset):
        is_overdue (bool | Unset):
        days_until_due (int | Unset):
    """

    id: int | Unset = UNSET
    loaned_to: str | Unset = UNSET
    loaned_at: str | Unset = UNSET
    due_at: str | Unset = UNSET
    is_overdue: bool | Unset = UNSET
    days_until_due: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        loaned_to = self.loaned_to

        loaned_at = self.loaned_at

        due_at = self.due_at

        is_overdue = self.is_overdue

        days_until_due = self.days_until_due

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if loaned_to is not UNSET:
            field_dict["loaned_to"] = loaned_to
        if loaned_at is not UNSET:
            field_dict["loaned_at"] = loaned_at
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if is_overdue is not UNSET:
            field_dict["is_overdue"] = is_overdue
        if days_until_due is not UNSET:
            field_dict["days_until_due"] = days_until_due

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        loaned_to = d.pop("loaned_to", UNSET)

        loaned_at = d.pop("loaned_at", UNSET)

        due_at = d.pop("due_at", UNSET)

        is_overdue = d.pop("is_overdue", UNSET)

        days_until_due = d.pop("days_until_due", UNSET)

        lend_a_copy_out_response_200_data_loan = cls(
            id=id,
            loaned_to=loaned_to,
            loaned_at=loaned_at,
            due_at=due_at,
            is_overdue=is_overdue,
            days_until_due=days_until_due,
        )

        lend_a_copy_out_response_200_data_loan.additional_properties = d
        return lend_a_copy_out_response_200_data_loan

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
