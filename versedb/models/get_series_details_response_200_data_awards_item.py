from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSeriesDetailsResponse200DataAwardsItem")


@_attrs_define
class GetSeriesDetailsResponse200DataAwardsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        category (None | str):
        year (int | None):
    """

    id: int
    name: None | str
    category: None | str
    year: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        category: None | str
        category = self.category

        year: int | None
        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "category": category,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        year = _parse_year(d.pop("year"))

        get_series_details_response_200_data_awards_item = cls(
            id=id,
            name=name,
            category=category,
            year=year,
        )

        get_series_details_response_200_data_awards_item.additional_properties = d
        return get_series_details_response_200_data_awards_item

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
