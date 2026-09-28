from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lend_a_copy_out_response_200_data_loan import LendACopyOutResponse200DataLoan


T = TypeVar("T", bound="LendACopyOutResponse200Data")


@_attrs_define
class LendACopyOutResponse200Data:
    """
    Attributes:
        id (int | Unset):
        loan (LendACopyOutResponse200DataLoan | Unset):
    """

    id: int | Unset = UNSET
    loan: LendACopyOutResponse200DataLoan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        loan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loan, Unset):
            loan = self.loan.to_dict()

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
        from ..models.lend_a_copy_out_response_200_data_loan import LendACopyOutResponse200DataLoan  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _loan = d.pop("loan", UNSET)
        loan: LendACopyOutResponse200DataLoan | Unset
        if isinstance(_loan, Unset):
            loan = UNSET
        else:
            loan = LendACopyOutResponse200DataLoan.from_dict(_loan)

        lend_a_copy_out_response_200_data = cls(
            id=id,
            loan=loan,
        )

        lend_a_copy_out_response_200_data.additional_properties = d
        return lend_a_copy_out_response_200_data

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
