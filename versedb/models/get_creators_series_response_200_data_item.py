from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorsSeriesResponse200DataItem")


@_attrs_define
class GetCreatorsSeriesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        start_year (int | Unset):
        end_year (int | Unset):
        cover_url (str | Unset):
        cached_issues_count (int | Unset):
        creator_issues_count (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    cached_issues_count: int | Unset = UNSET
    creator_issues_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        start_year = self.start_year

        end_year = self.end_year

        cover_url = self.cover_url

        cached_issues_count = self.cached_issues_count

        creator_issues_count = self.creator_issues_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if start_year is not UNSET:
            field_dict["start_year"] = start_year
        if end_year is not UNSET:
            field_dict["end_year"] = end_year
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if cached_issues_count is not UNSET:
            field_dict["cached_issues_count"] = cached_issues_count
        if creator_issues_count is not UNSET:
            field_dict["creator_issues_count"] = creator_issues_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        start_year = d.pop("start_year", UNSET)

        end_year = d.pop("end_year", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        cached_issues_count = d.pop("cached_issues_count", UNSET)

        creator_issues_count = d.pop("creator_issues_count", UNSET)

        get_creators_series_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            cover_url=cover_url,
            cached_issues_count=cached_issues_count,
            creator_issues_count=creator_issues_count,
        )

        get_creators_series_response_200_data_item.additional_properties = d
        return get_creators_series_response_200_data_item

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
