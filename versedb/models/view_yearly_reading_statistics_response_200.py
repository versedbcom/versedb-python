from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_yearly_reading_statistics_response_200_data import ViewYearlyReadingStatisticsResponse200Data


T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200:
    """
    Attributes:
        data (ViewYearlyReadingStatisticsResponse200Data | Unset):
        years (list[int] | Unset):
    """

    data: ViewYearlyReadingStatisticsResponse200Data | Unset = UNSET
    years: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        years: list[int] | Unset = UNSET
        if not isinstance(self.years, Unset):
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_yearly_reading_statistics_response_200_data import (
            ViewYearlyReadingStatisticsResponse200Data,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ViewYearlyReadingStatisticsResponse200Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ViewYearlyReadingStatisticsResponse200Data.from_dict(_data)

        years = cast(list[int], d.pop("years", UNSET))

        view_yearly_reading_statistics_response_200 = cls(
            data=data,
            years=years,
        )

        view_yearly_reading_statistics_response_200.additional_properties = d
        return view_yearly_reading_statistics_response_200

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
