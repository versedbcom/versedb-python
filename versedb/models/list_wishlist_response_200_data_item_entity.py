from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_wishlist_response_200_data_item_entity_series_type_0 import (
        ListWishlistResponse200DataItemEntitySeriesType0,
    )


T = TypeVar("T", bound="ListWishlistResponse200DataItemEntity")


@_attrs_define
class ListWishlistResponse200DataItemEntity:
    """Left out once the issue is gone.

    Attributes:
        id (int):
        slug (None | str):
        name (None | str):
        issue_number (None | str):
        release_date (None | str):
        foc_date (None | str):
        image_url (None | str):
        is_nsfw (bool | None):
        publisher (None | str):
        series (ListWishlistResponse200DataItemEntitySeriesType0 | None):
    """

    id: int
    slug: None | str
    name: None | str
    issue_number: None | str
    release_date: None | str
    foc_date: None | str
    image_url: None | str
    is_nsfw: bool | None
    publisher: None | str
    series: ListWishlistResponse200DataItemEntitySeriesType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_wishlist_response_200_data_item_entity_series_type_0 import (
            ListWishlistResponse200DataItemEntitySeriesType0,  # noqa: PLC0415
        )

        id = self.id

        slug: None | str
        slug = self.slug

        name: None | str
        name = self.name

        issue_number: None | str
        issue_number = self.issue_number

        release_date: None | str
        release_date = self.release_date

        foc_date: None | str
        foc_date = self.foc_date

        image_url: None | str
        image_url = self.image_url

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        publisher: None | str
        publisher = self.publisher

        series: dict[str, Any] | None
        if isinstance(self.series, ListWishlistResponse200DataItemEntitySeriesType0):
            series = self.series.to_dict()
        else:
            series = self.series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "issue_number": issue_number,
                "release_date": release_date,
                "foc_date": foc_date,
                "image_url": image_url,
                "is_nsfw": is_nsfw,
                "publisher": publisher,
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_wishlist_response_200_data_item_entity_series_type_0 import (
            ListWishlistResponse200DataItemEntitySeriesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

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

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_publisher(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher = _parse_publisher(d.pop("publisher"))

        def _parse_series(data: object) -> ListWishlistResponse200DataItemEntitySeriesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_type_0 = ListWishlistResponse200DataItemEntitySeriesType0.from_dict(data)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListWishlistResponse200DataItemEntitySeriesType0 | None, data)

        series = _parse_series(d.pop("series"))

        list_wishlist_response_200_data_item_entity = cls(
            id=id,
            slug=slug,
            name=name,
            issue_number=issue_number,
            release_date=release_date,
            foc_date=foc_date,
            image_url=image_url,
            is_nsfw=is_nsfw,
            publisher=publisher,
            series=series,
        )

        list_wishlist_response_200_data_item_entity.additional_properties = d
        return list_wishlist_response_200_data_item_entity

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
