from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_a_specific_title_response_200_data_images import GetASpecificTitleResponse200DataImages


T = TypeVar("T", bound="GetASpecificTitleResponse200Data")


@_attrs_define
class GetASpecificTitleResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        start_year (int | Unset):
        end_year (None | str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        image_url (str | Unset):
        images (GetASpecificTitleResponse200DataImages | Unset):
        content_rating_label (str | Unset):
        min_age (int | Unset):
        is_nsfw (bool | Unset):
        imprint_id (None | str | Unset):
        series_count (int | Unset):
        issues_count (int | Unset):
        average_rating (float | Unset):
        aliases (list[str] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: None | str | Unset = UNSET
    status: str | Unset = UNSET
    type_: str | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetASpecificTitleResponse200DataImages | Unset = UNSET
    content_rating_label: str | Unset = UNSET
    min_age: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    imprint_id: None | str | Unset = UNSET
    series_count: int | Unset = UNSET
    issues_count: int | Unset = UNSET
    average_rating: float | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        start_year = self.start_year

        end_year: None | str | Unset
        if isinstance(self.end_year, Unset):
            end_year = UNSET
        else:
            end_year = self.end_year

        status = self.status

        type_ = self.type_

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        content_rating_label = self.content_rating_label

        min_age = self.min_age

        is_nsfw = self.is_nsfw

        imprint_id: None | str | Unset
        if isinstance(self.imprint_id, Unset):
            imprint_id = UNSET
        else:
            imprint_id = self.imprint_id

        series_count = self.series_count

        issues_count = self.issues_count

        average_rating = self.average_rating

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

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
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images
        if content_rating_label is not UNSET:
            field_dict["content_rating_label"] = content_rating_label
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if imprint_id is not UNSET:
            field_dict["imprint_id"] = imprint_id
        if series_count is not UNSET:
            field_dict["series_count"] = series_count
        if issues_count is not UNSET:
            field_dict["issues_count"] = issues_count
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_title_response_200_data_images import GetASpecificTitleResponse200DataImages  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        start_year = d.pop("start_year", UNSET)

        def _parse_end_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_year = _parse_end_year(d.pop("end_year", UNSET))

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetASpecificTitleResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetASpecificTitleResponse200DataImages.from_dict(_images)

        content_rating_label = d.pop("content_rating_label", UNSET)

        min_age = d.pop("min_age", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        def _parse_imprint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imprint_id = _parse_imprint_id(d.pop("imprint_id", UNSET))

        series_count = d.pop("series_count", UNSET)

        issues_count = d.pop("issues_count", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        get_a_specific_title_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            status=status,
            type_=type_,
            image_url=image_url,
            images=images,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            imprint_id=imprint_id,
            series_count=series_count,
            issues_count=issues_count,
            average_rating=average_rating,
            aliases=aliases,
        )

        get_a_specific_title_response_200_data.additional_properties = d
        return get_a_specific_title_response_200_data

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
