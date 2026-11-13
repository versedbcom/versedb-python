from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetActivityFeedResponse200DataItemDataType0")


@_attrs_define
class GetActivityFeedResponse200DataItemDataType0:
    """
    Attributes:
        issue_id (int):
        issue_name (None | str): The issue as its series names it, or null when the issue is gone.
        series_name (None | str):
        series_start_year (int | None):
        cover_url (None | str):
    """

    issue_id: int
    issue_name: None | str
    series_name: None | str
    series_start_year: int | None
    cover_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        issue_name: None | str
        issue_name = self.issue_name

        series_name: None | str
        series_name = self.series_name

        series_start_year: int | None
        series_start_year = self.series_start_year

        cover_url: None | str
        cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "issue_name": issue_name,
                "series_name": series_name,
                "series_start_year": series_start_year,
                "cover_url": cover_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        def _parse_issue_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_name = _parse_issue_name(d.pop("issue_name"))

        def _parse_series_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_name = _parse_series_name(d.pop("series_name"))

        def _parse_series_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_start_year = _parse_series_start_year(d.pop("series_start_year"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        get_activity_feed_response_200_data_item_data_type_0 = cls(
            issue_id=issue_id,
            issue_name=issue_name,
            series_name=series_name,
            series_start_year=series_start_year,
            cover_url=cover_url,
        )

        get_activity_feed_response_200_data_item_data_type_0.additional_properties = d
        return get_activity_feed_response_200_data_item_data_type_0

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
