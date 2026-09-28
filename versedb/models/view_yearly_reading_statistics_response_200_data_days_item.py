from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200DataDaysItem")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200DataDaysItem:
    """
    Attributes:
        date (str | Unset):
        count (int | Unset):
        total (int | Unset):
        expected (float | Unset):
    """

    date: str | Unset = UNSET
    count: int | Unset = UNSET
    total: int | Unset = UNSET
    expected: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        count = self.count

        total = self.total

        expected = self.expected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if count is not UNSET:
            field_dict["count"] = count
        if total is not UNSET:
            field_dict["total"] = total
        if expected is not UNSET:
            field_dict["expected"] = expected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        count = d.pop("count", UNSET)

        total = d.pop("total", UNSET)

        expected = d.pop("expected", UNSET)

        view_yearly_reading_statistics_response_200_data_days_item = cls(
            date=date,
            count=count,
            total=total,
            expected=expected,
        )

        view_yearly_reading_statistics_response_200_data_days_item.additional_properties = d
        return view_yearly_reading_statistics_response_200_data_days_item

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
