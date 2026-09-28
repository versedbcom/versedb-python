from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkTheCopysOpenLoanReturnedResponse200Data")


@_attrs_define
class MarkTheCopysOpenLoanReturnedResponse200Data:
    """
    Attributes:
        id (int | Unset):
        loan (None | str | Unset):
    """

    id: int | Unset = UNSET
    loan: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        loan: None | str | Unset
        if isinstance(self.loan, Unset):
            loan = UNSET
        else:
            loan = self.loan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if loan is not UNSET:
            field_dict["loan"] = loan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_loan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loan = _parse_loan(d.pop("loan", UNSET))

        mark_the_copys_open_loan_returned_response_200_data = cls(
            id=id,
            loan=loan,
        )

        mark_the_copys_open_loan_returned_response_200_data.additional_properties = d
        return mark_the_copys_open_loan_returned_response_200_data

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
