from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarkAsReadResponse201SeriesCompleted")


@_attrs_define
class MarkAsReadResponse201SeriesCompleted:
    """Every live issue of the series is now read.

    Attributes:
        series_id (int):
        series_name (None | str):
    """

    series_id: int
    series_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_id = self.series_id

        series_name: None | str
        series_name = self.series_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series_id": series_id,
                "series_name": series_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_id = d.pop("series_id")

        def _parse_series_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_name = _parse_series_name(d.pop("series_name"))

        mark_as_read_response_201_series_completed = cls(
            series_id=series_id,
            series_name=series_name,
        )

        mark_as_read_response_201_series_completed.additional_properties = d
        return mark_as_read_response_201_series_completed

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
