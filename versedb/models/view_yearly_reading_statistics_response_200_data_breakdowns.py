from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200DataBreakdowns")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200DataBreakdowns:
    """
    Attributes:
        series (list[Any] | Unset):
        publishers (list[Any] | Unset):
        creators (list[Any] | Unset):
        characters (list[Any] | Unset):
    """

    series: list[Any] | Unset = UNSET
    publishers: list[Any] | Unset = UNSET
    creators: list[Any] | Unset = UNSET
    characters: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series: list[Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series

        publishers: list[Any] | Unset = UNSET
        if not isinstance(self.publishers, Unset):
            publishers = self.publishers

        creators: list[Any] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = self.creators

        characters: list[Any] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = self.characters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series
        if publishers is not UNSET:
            field_dict["publishers"] = publishers
        if creators is not UNSET:
            field_dict["creators"] = creators
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series = cast(list[Any], d.pop("series", UNSET))

        publishers = cast(list[Any], d.pop("publishers", UNSET))

        creators = cast(list[Any], d.pop("creators", UNSET))

        characters = cast(list[Any], d.pop("characters", UNSET))

        view_yearly_reading_statistics_response_200_data_breakdowns = cls(
            series=series,
            publishers=publishers,
            creators=creators,
            characters=characters,
        )

        view_yearly_reading_statistics_response_200_data_breakdowns.additional_properties = d
        return view_yearly_reading_statistics_response_200_data_breakdowns

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
