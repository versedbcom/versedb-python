from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_issues_response_200_data_item_series_type_0_images_type_0 import (
        ListIssuesResponse200DataItemSeriesType0ImagesType0,
    )


T = TypeVar("T", bound="ListIssuesResponse200DataItemSeriesType0")


@_attrs_define
class ListIssuesResponse200DataItemSeriesType0:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        start_year (int | None):
        end_year (int | None):
        volume_number (int | None):
        publication_type (None | str):
        format_ (None | str):
        cached_issues_count (int | None):
        cover_url (None | str):
        images (ListIssuesResponse200DataItemSeriesType0ImagesType0 | None):
        publisher_name (None | str):
    """

    id: int
    name: None | str
    slug: None | str
    start_year: int | None
    end_year: int | None
    volume_number: int | None
    publication_type: None | str
    format_: None | str
    cached_issues_count: int | None
    cover_url: None | str
    images: ListIssuesResponse200DataItemSeriesType0ImagesType0 | None
    publisher_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_issues_response_200_data_item_series_type_0_images_type_0 import (
            ListIssuesResponse200DataItemSeriesType0ImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        start_year: int | None
        start_year = self.start_year

        end_year: int | None
        end_year = self.end_year

        volume_number: int | None
        volume_number = self.volume_number

        publication_type: None | str
        publication_type = self.publication_type

        format_: None | str
        format_ = self.format_

        cached_issues_count: int | None
        cached_issues_count = self.cached_issues_count

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListIssuesResponse200DataItemSeriesType0ImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        publisher_name: None | str
        publisher_name = self.publisher_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "start_year": start_year,
                "end_year": end_year,
                "volume_number": volume_number,
                "publication_type": publication_type,
                "format": format_,
                "cached_issues_count": cached_issues_count,
                "cover_url": cover_url,
                "images": images,
                "publisher_name": publisher_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_issues_response_200_data_item_series_type_0_images_type_0 import (
            ListIssuesResponse200DataItemSeriesType0ImagesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        start_year = _parse_start_year(d.pop("start_year"))

        def _parse_end_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        end_year = _parse_end_year(d.pop("end_year"))

        def _parse_volume_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        volume_number = _parse_volume_number(d.pop("volume_number"))

        def _parse_publication_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publication_type = _parse_publication_type(d.pop("publication_type"))

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

        def _parse_cached_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cached_issues_count = _parse_cached_issues_count(d.pop("cached_issues_count"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> ListIssuesResponse200DataItemSeriesType0ImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListIssuesResponse200DataItemSeriesType0ImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListIssuesResponse200DataItemSeriesType0ImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name"))

        list_issues_response_200_data_item_series_type_0 = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            volume_number=volume_number,
            publication_type=publication_type,
            format_=format_,
            cached_issues_count=cached_issues_count,
            cover_url=cover_url,
            images=images,
            publisher_name=publisher_name,
        )

        list_issues_response_200_data_item_series_type_0.additional_properties = d
        return list_issues_response_200_data_item_series_type_0

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
