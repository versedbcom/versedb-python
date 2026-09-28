from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeriesForASpecificTeamResponse200DataItem")


@_attrs_define
class GetSeriesForASpecificTeamResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        title_id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        start_year (int | Unset):
        end_year (int | Unset):
        medium (str | Unset):
        publication_type (str | Unset):
        status (str | Unset):
        average_rating (float | Unset):
        total_reviews (int | Unset):
        is_nsfw (bool | Unset):
    """

    id: int | Unset = UNSET
    title_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: int | Unset = UNSET
    medium: str | Unset = UNSET
    publication_type: str | Unset = UNSET
    status: str | Unset = UNSET
    average_rating: float | Unset = UNSET
    total_reviews: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title_id = self.title_id

        name = self.name

        slug = self.slug

        start_year = self.start_year

        end_year = self.end_year

        medium = self.medium

        publication_type = self.publication_type

        status = self.status

        average_rating = self.average_rating

        total_reviews = self.total_reviews

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
        if start_year is not UNSET:
            field_dict["start_year"] = start_year
        if end_year is not UNSET:
            field_dict["end_year"] = end_year
        if medium is not UNSET:
            field_dict["medium"] = medium
        if publication_type is not UNSET:
            field_dict["publication_type"] = publication_type
        if status is not UNSET:
            field_dict["status"] = status
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if total_reviews is not UNSET:
            field_dict["total_reviews"] = total_reviews
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

        start_year = d.pop("start_year", UNSET)

        end_year = d.pop("end_year", UNSET)

        medium = d.pop("medium", UNSET)

        publication_type = d.pop("publication_type", UNSET)

        status = d.pop("status", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        total_reviews = d.pop("total_reviews", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        get_series_for_a_specific_team_response_200_data_item = cls(
            id=id,
            title_id=title_id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            medium=medium,
            publication_type=publication_type,
            status=status,
            average_rating=average_rating,
            total_reviews=total_reviews,
            is_nsfw=is_nsfw,
        )

        get_series_for_a_specific_team_response_200_data_item.additional_properties = d
        return get_series_for_a_specific_team_response_200_data_item

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
