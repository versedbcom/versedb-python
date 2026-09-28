from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewYourMonthlyReadingCalendarResponse200")


@_attrs_define
class ViewYourMonthlyReadingCalendarResponse200:
    """
    Attributes:
        data (list[Any] | Unset):
        current_page (int | Unset):
        last_page (int | Unset):
        total (int | Unset):
    """

    data: list[Any] | Unset = UNSET
    current_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        current_page = self.current_page

        last_page = self.last_page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = cast(list[Any], d.pop("data", UNSET))

        current_page = d.pop("current_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        total = d.pop("total", UNSET)

        view_your_monthly_reading_calendar_response_200 = cls(
            data=data,
            current_page=current_page,
            last_page=last_page,
            total=total,
        )

        view_your_monthly_reading_calendar_response_200.additional_properties = d
        return view_your_monthly_reading_calendar_response_200

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
