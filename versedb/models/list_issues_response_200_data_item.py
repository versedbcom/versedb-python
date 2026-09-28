from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListIssuesResponse200DataItem")


@_attrs_define
class ListIssuesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        series_id (int | Unset):
        issue_number (str | Unset):
        name (str | Unset):
        release_date (str | Unset):
        cover_url (str | Unset):
        is_reprint (bool | Unset):
        content_rating_label (str | Unset):
        min_age (int | Unset):
        is_nsfw (bool | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    series_id: int | Unset = UNSET
    issue_number: str | Unset = UNSET
    name: str | Unset = UNSET
    release_date: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    is_reprint: bool | Unset = UNSET
    content_rating_label: str | Unset = UNSET
    min_age: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        series_id = self.series_id

        issue_number = self.issue_number

        name = self.name

        release_date = self.release_date

        cover_url = self.cover_url

        is_reprint = self.is_reprint

        content_rating_label = self.content_rating_label

        min_age = self.min_age

        is_nsfw = self.is_nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if name is not UNSET:
            field_dict["name"] = name
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if is_reprint is not UNSET:
            field_dict["is_reprint"] = is_reprint
        if content_rating_label is not UNSET:
            field_dict["content_rating_label"] = content_rating_label
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        series_id = d.pop("series_id", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        name = d.pop("name", UNSET)

        release_date = d.pop("release_date", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        is_reprint = d.pop("is_reprint", UNSET)

        content_rating_label = d.pop("content_rating_label", UNSET)

        min_age = d.pop("min_age", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        list_issues_response_200_data_item = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            issue_number=issue_number,
            name=name,
            release_date=release_date,
            cover_url=cover_url,
            is_reprint=is_reprint,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
        )

        list_issues_response_200_data_item.additional_properties = d
        return list_issues_response_200_data_item

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
