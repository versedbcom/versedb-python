from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_series_details_response_200_data_foc_issues_item_images_type_0 import (
        GetSeriesDetailsResponse200DataFocIssuesItemImagesType0,
    )
    from ..models.get_series_details_response_200_data_foc_issues_item_name_i18n import (
        GetSeriesDetailsResponse200DataFocIssuesItemNameI18N,
    )


T = TypeVar("T", bound="GetSeriesDetailsResponse200DataFocIssuesItem")


@_attrs_define
class GetSeriesDetailsResponse200DataFocIssuesItem:
    """
    Attributes:
        id (int):
        slug (None | str):
        series_id (int | None):
        issue_number (None | str):
        name (None | str):
        cover_date (None | str):
        release_date (None | str):
        foc_date (None | str):
        is_unreleased (bool):
        cover_url (None | str):
        images (GetSeriesDetailsResponse200DataFocIssuesItemImagesType0 | None):
        is_reprint (bool):
        content_rating_label (None | str):
        min_age (int | None):
        is_nsfw (bool):
        average_rating (float | None):
        name_i18n (GetSeriesDetailsResponse200DataFocIssuesItemNameI18N): One name per language, keyed by BCP 47 tag.
    """

    id: int
    slug: None | str
    series_id: int | None
    issue_number: None | str
    name: None | str
    cover_date: None | str
    release_date: None | str
    foc_date: None | str
    is_unreleased: bool
    cover_url: None | str
    images: GetSeriesDetailsResponse200DataFocIssuesItemImagesType0 | None
    is_reprint: bool
    content_rating_label: None | str
    min_age: int | None
    is_nsfw: bool
    average_rating: float | None
    name_i18n: GetSeriesDetailsResponse200DataFocIssuesItemNameI18N
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_details_response_200_data_foc_issues_item_images_type_0 import (
            GetSeriesDetailsResponse200DataFocIssuesItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        slug: None | str
        slug = self.slug

        series_id: int | None
        series_id = self.series_id

        issue_number: None | str
        issue_number = self.issue_number

        name: None | str
        name = self.name

        cover_date: None | str
        cover_date = self.cover_date

        release_date: None | str
        release_date = self.release_date

        foc_date: None | str
        foc_date = self.foc_date

        is_unreleased = self.is_unreleased

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetSeriesDetailsResponse200DataFocIssuesItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        is_reprint = self.is_reprint

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        is_nsfw = self.is_nsfw

        average_rating: float | None
        average_rating = self.average_rating

        name_i18n = self.name_i18n.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "series_id": series_id,
                "issue_number": issue_number,
                "name": name,
                "cover_date": cover_date,
                "release_date": release_date,
                "foc_date": foc_date,
                "is_unreleased": is_unreleased,
                "cover_url": cover_url,
                "images": images,
                "is_reprint": is_reprint,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "is_nsfw": is_nsfw,
                "average_rating": average_rating,
                "name_i18n": name_i18n,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_details_response_200_data_foc_issues_item_images_type_0 import (
            GetSeriesDetailsResponse200DataFocIssuesItemImagesType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_foc_issues_item_name_i18n import (
            GetSeriesDetailsResponse200DataFocIssuesItemNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_cover_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_date = _parse_cover_date(d.pop("cover_date"))

        def _parse_release_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        release_date = _parse_release_date(d.pop("release_date"))

        def _parse_foc_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        foc_date = _parse_foc_date(d.pop("foc_date"))

        is_unreleased = d.pop("is_unreleased")

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> GetSeriesDetailsResponse200DataFocIssuesItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetSeriesDetailsResponse200DataFocIssuesItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesDetailsResponse200DataFocIssuesItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        is_reprint = d.pop("is_reprint")

        def _parse_content_rating_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_rating_label = _parse_content_rating_label(d.pop("content_rating_label"))

        def _parse_min_age(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_age = _parse_min_age(d.pop("min_age"))

        is_nsfw = d.pop("is_nsfw")

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("average_rating"))

        name_i18n = GetSeriesDetailsResponse200DataFocIssuesItemNameI18N.from_dict(d.pop("name_i18n"))

        get_series_details_response_200_data_foc_issues_item = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            issue_number=issue_number,
            name=name,
            cover_date=cover_date,
            release_date=release_date,
            foc_date=foc_date,
            is_unreleased=is_unreleased,
            cover_url=cover_url,
            images=images,
            is_reprint=is_reprint,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            average_rating=average_rating,
            name_i18n=name_i18n,
        )

        get_series_details_response_200_data_foc_issues_item.additional_properties = d
        return get_series_details_response_200_data_foc_issues_item

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
