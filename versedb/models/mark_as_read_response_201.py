from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_as_read_response_201_series_completed import MarkAsReadResponse201SeriesCompleted


T = TypeVar("T", bound="MarkAsReadResponse201")


@_attrs_define
class MarkAsReadResponse201:
    """
    Attributes:
        read_at (None | str): The read's date; null when it has none.
        series_completed (MarkAsReadResponse201SeriesCompleted | Unset): Every live issue of the series is now read.
    """

    read_at: None | str
    series_completed: MarkAsReadResponse201SeriesCompleted | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_at: None | str
        read_at = self.read_at

        series_completed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series_completed, Unset):
            series_completed = self.series_completed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read_at": read_at,
            }
        )
        if series_completed is not UNSET:
            field_dict["series_completed"] = series_completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mark_as_read_response_201_series_completed import MarkAsReadResponse201SeriesCompleted  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_read_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        read_at = _parse_read_at(d.pop("read_at"))

        _series_completed = d.pop("series_completed", UNSET)
        series_completed: MarkAsReadResponse201SeriesCompleted | Unset
        if isinstance(_series_completed, Unset):
            series_completed = UNSET
        else:
            series_completed = MarkAsReadResponse201SeriesCompleted.from_dict(_series_completed)

        mark_as_read_response_201 = cls(
            read_at=read_at,
            series_completed=series_completed,
        )

        mark_as_read_response_201.additional_properties = d
        return mark_as_read_response_201

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
