from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LendACopyOutResponse200DataLoanType0")


@_attrs_define
class LendACopyOutResponse200DataLoanType0:
    """Left out for a `read:showcase` token.

    Attributes:
        id (int):
        loaned_to (None | str):
        loaned_at (None | str):
        due_at (None | str):
        is_overdue (bool):
        days_until_due (int | None):
    """

    id: int
    loaned_to: None | str
    loaned_at: None | str
    due_at: None | str
    is_overdue: bool
    days_until_due: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        loaned_to: None | str
        loaned_to = self.loaned_to

        loaned_at: None | str
        loaned_at = self.loaned_at

        due_at: None | str
        due_at = self.due_at

        is_overdue = self.is_overdue

        days_until_due: int | None
        days_until_due = self.days_until_due

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "loaned_to": loaned_to,
                "loaned_at": loaned_at,
                "due_at": due_at,
                "is_overdue": is_overdue,
                "days_until_due": days_until_due,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_loaned_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        loaned_to = _parse_loaned_to(d.pop("loaned_to"))

        def _parse_loaned_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        loaned_at = _parse_loaned_at(d.pop("loaned_at"))

        def _parse_due_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        due_at = _parse_due_at(d.pop("due_at"))

        is_overdue = d.pop("is_overdue")

        def _parse_days_until_due(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_until_due = _parse_days_until_due(d.pop("days_until_due"))

        lend_a_copy_out_response_200_data_loan_type_0 = cls(
            id=id,
            loaned_to=loaned_to,
            loaned_at=loaned_at,
            due_at=due_at,
            is_overdue=is_overdue,
            days_until_due=days_until_due,
        )

        lend_a_copy_out_response_200_data_loan_type_0.additional_properties = d
        return lend_a_copy_out_response_200_data_loan_type_0

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
