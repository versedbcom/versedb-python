from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListSeriesResponse200DataItem")


@_attrs_define
class ListSeriesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        title_id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        number (int | Unset):
        start_year (int | Unset):
        end_year (int | Unset):
        cover_url (str | Unset):
        publication_type (str | Unset):
        format_ (str | Unset):
        status (str | Unset):
        original_language (str | Unset):
        cached_issues_count (int | Unset):
        average_rating (float | Unset):
        total_reviews (int | Unset):
        issues_average_rating (float | Unset):
        issues_rated_count (int | Unset):
        content_rating_label (str | Unset):
        min_age (int | Unset):
        is_nsfw (bool | Unset):
    """

    id: int | Unset = UNSET
    title_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    number: int | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    publication_type: str | Unset = UNSET
    format_: str | Unset = UNSET
    status: str | Unset = UNSET
    original_language: str | Unset = UNSET
    cached_issues_count: int | Unset = UNSET
    average_rating: float | Unset = UNSET
    total_reviews: int | Unset = UNSET
    issues_average_rating: float | Unset = UNSET
    issues_rated_count: int | Unset = UNSET
    content_rating_label: str | Unset = UNSET
    min_age: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title_id = self.title_id

        name = self.name

        slug = self.slug

        number = self.number

        start_year = self.start_year

        end_year = self.end_year

        cover_url = self.cover_url

        publication_type = self.publication_type

        format_ = self.format_

        status = self.status

        original_language = self.original_language

        cached_issues_count = self.cached_issues_count

        average_rating = self.average_rating

        total_reviews = self.total_reviews

        issues_average_rating = self.issues_average_rating

        issues_rated_count = self.issues_rated_count

        content_rating_label = self.content_rating_label

        min_age = self.min_age

        is_nsfw = self.is_nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title_id is not UNSET:
            field_dict["title_id"] = title_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if number is not UNSET:
            field_dict["number"] = number
        if start_year is not UNSET:
            field_dict["start_year"] = start_year
        if end_year is not UNSET:
            field_dict["end_year"] = end_year
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if publication_type is not UNSET:
            field_dict["publication_type"] = publication_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if status is not UNSET:
            field_dict["status"] = status
        if original_language is not UNSET:
            field_dict["original_language"] = original_language
        if cached_issues_count is not UNSET:
            field_dict["cached_issues_count"] = cached_issues_count
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if total_reviews is not UNSET:
            field_dict["total_reviews"] = total_reviews
        if issues_average_rating is not UNSET:
            field_dict["issues_average_rating"] = issues_average_rating
        if issues_rated_count is not UNSET:
            field_dict["issues_rated_count"] = issues_rated_count
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

        title_id = d.pop("title_id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        number = d.pop("number", UNSET)

        start_year = d.pop("start_year", UNSET)

        end_year = d.pop("end_year", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        publication_type = d.pop("publication_type", UNSET)

        format_ = d.pop("format", UNSET)

        status = d.pop("status", UNSET)

        original_language = d.pop("original_language", UNSET)

        cached_issues_count = d.pop("cached_issues_count", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        total_reviews = d.pop("total_reviews", UNSET)

        issues_average_rating = d.pop("issues_average_rating", UNSET)

        issues_rated_count = d.pop("issues_rated_count", UNSET)

        content_rating_label = d.pop("content_rating_label", UNSET)

        min_age = d.pop("min_age", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        list_series_response_200_data_item = cls(
            id=id,
            title_id=title_id,
            name=name,
            slug=slug,
            number=number,
            start_year=start_year,
            end_year=end_year,
            cover_url=cover_url,
            publication_type=publication_type,
            format_=format_,
            status=status,
            original_language=original_language,
            cached_issues_count=cached_issues_count,
            average_rating=average_rating,
            total_reviews=total_reviews,
            issues_average_rating=issues_average_rating,
            issues_rated_count=issues_rated_count,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
        )

        list_series_response_200_data_item.additional_properties = d
        return list_series_response_200_data_item

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
