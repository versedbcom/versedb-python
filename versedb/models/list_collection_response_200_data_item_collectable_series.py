from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_collection_response_200_data_item_collectable_series_images import (
        ListCollectionResponse200DataItemCollectableSeriesImages,
    )


T = TypeVar("T", bound="ListCollectionResponse200DataItemCollectableSeries")


@_attrs_define
class ListCollectionResponse200DataItemCollectableSeries:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        start_year (int | Unset):
        end_year (None | str | Unset):
        volume_number (int | Unset):
        publication_type (str | Unset):
        format_ (str | Unset):
        cached_issues_count (int | Unset):
        cover_url (str | Unset):
        images (ListCollectionResponse200DataItemCollectableSeriesImages | Unset):
        publisher_name (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: None | str | Unset = UNSET
    volume_number: int | Unset = UNSET
    publication_type: str | Unset = UNSET
    format_: str | Unset = UNSET
    cached_issues_count: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    images: ListCollectionResponse200DataItemCollectableSeriesImages | Unset = UNSET
    publisher_name: str | Unset = UNSET
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

        volume_number = self.volume_number

        publication_type = self.publication_type

        format_ = self.format_

        cached_issues_count = self.cached_issues_count

        cover_url = self.cover_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        publisher_name = self.publisher_name

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
        if volume_number is not UNSET:
            field_dict["volume_number"] = volume_number
        if publication_type is not UNSET:
            field_dict["publication_type"] = publication_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if cached_issues_count is not UNSET:
            field_dict["cached_issues_count"] = cached_issues_count
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if images is not UNSET:
            field_dict["images"] = images
        if publisher_name is not UNSET:
            field_dict["publisher_name"] = publisher_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collection_response_200_data_item_collectable_series_images import (
            ListCollectionResponse200DataItemCollectableSeriesImages,  # noqa: PLC0415
        )

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

        volume_number = d.pop("volume_number", UNSET)

        publication_type = d.pop("publication_type", UNSET)

        format_ = d.pop("format", UNSET)

        cached_issues_count = d.pop("cached_issues_count", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListCollectionResponse200DataItemCollectableSeriesImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListCollectionResponse200DataItemCollectableSeriesImages.from_dict(_images)

        publisher_name = d.pop("publisher_name", UNSET)

        list_collection_response_200_data_item_collectable_series = cls(
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

        list_collection_response_200_data_item_collectable_series.additional_properties = d
        return list_collection_response_200_data_item_collectable_series

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
