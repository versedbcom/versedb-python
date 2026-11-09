from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ViewYourMonthlyReadingCalendarResponse200DataItem")


@_attrs_define
class ViewYourMonthlyReadingCalendarResponse200DataItem:
    """
    Attributes:
        id (int):
        date (None | str):
        name (None | str):
        url (None | str):
        cover (None | str):
    """

    id: int
    date: None | str
    name: None | str
    url: None | str
    cover: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date: None | str
        date = self.date

        name: None | str
        name = self.name

        url: None | str
        url = self.url

        cover: None | str
        cover = self.cover

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "name": name,
                "url": url,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_cover(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover = _parse_cover(d.pop("cover"))

        view_your_monthly_reading_calendar_response_200_data_item = cls(
            id=id,
            date=date,
            name=name,
            url=url,
            cover=cover,
        )

        view_your_monthly_reading_calendar_response_200_data_item.additional_properties = d
        return view_your_monthly_reading_calendar_response_200_data_item

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
