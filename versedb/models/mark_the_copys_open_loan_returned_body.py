from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkTheCopysOpenLoanReturnedBody")


@_attrs_define
class MarkTheCopysOpenLoanReturnedBody:
    """
    Attributes:
        returned_at (None | str | Unset): The day it came back (YYYY-MM-DD). Defaults to today. Must be a valid date.
    """

    returned_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        returned_at: None | str | Unset
        if isinstance(self.returned_at, Unset):
            returned_at = UNSET
        else:
            returned_at = self.returned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if returned_at is not UNSET:
            field_dict["returned_at"] = returned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_returned_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        returned_at = _parse_returned_at(d.pop("returned_at", UNSET))

        mark_the_copys_open_loan_returned_body = cls(
            returned_at=returned_at,
        )

        mark_the_copys_open_loan_returned_body.additional_properties = d
        return mark_the_copys_open_loan_returned_body

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
