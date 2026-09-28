from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityFeedResponse200DataItemData")


@_attrs_define
class GetActivityFeedResponse200DataItemData:
    """
    Attributes:
        issue_id (int | Unset):
        issue_name (str | Unset):
        series_name (str | Unset):
        series_start_year (int | Unset):
        cover_url (str | Unset):
    """

    issue_id: int | Unset = UNSET
    issue_name: str | Unset = UNSET
    series_name: str | Unset = UNSET
    series_start_year: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        issue_name = self.issue_name

        series_name = self.series_name

        series_start_year = self.series_start_year

        cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if issue_name is not UNSET:
            field_dict["issue_name"] = issue_name
        if series_name is not UNSET:
            field_dict["series_name"] = series_name
        if series_start_year is not UNSET:
            field_dict["series_start_year"] = series_start_year
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_id = d.pop("issue_id", UNSET)

        issue_name = d.pop("issue_name", UNSET)

        series_name = d.pop("series_name", UNSET)

        series_start_year = d.pop("series_start_year", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        get_activity_feed_response_200_data_item_data = cls(
            issue_id=issue_id,
            issue_name=issue_name,
            series_name=series_name,
            series_start_year=series_start_year,
            cover_url=cover_url,
        )

        get_activity_feed_response_200_data_item_data.additional_properties = d
        return get_activity_feed_response_200_data_item_data

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
