from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_yearly_reading_statistics_response_200_data import ViewYearlyReadingStatisticsResponse200Data


T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200:
    """
    Attributes:
        data (ViewYearlyReadingStatisticsResponse200Data):
        years (list[int]):
    """

    data: ViewYearlyReadingStatisticsResponse200Data
    years: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "years": years,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_yearly_reading_statistics_response_200_data import ViewYearlyReadingStatisticsResponse200Data  # noqa: PLC0415

        d = dict(src_dict)
        data = ViewYearlyReadingStatisticsResponse200Data.from_dict(d.pop("data"))

        years = cast(list[int], d.pop("years"))

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
