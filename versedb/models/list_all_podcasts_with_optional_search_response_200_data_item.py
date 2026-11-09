from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_all_podcasts_with_optional_search_response_200_data_item_images_type_0 import (
        ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0,
    )


T = TypeVar("T", bound="ListAllPodcastsWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllPodcastsWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        type_ (str):
        language (None | str):
        logo_url (None | str):
        images (ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0 | None):
        follower_count (int):
        subscriber_count (int | None):
        categories (list[str]): The category names.
    """

    id: int
    name: None | str
    slug: None | str
    type_: str
    language: None | str
    logo_url: None | str
    images: ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0 | None
    follower_count: int
    subscriber_count: int | None
    categories: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_all_podcasts_with_optional_search_response_200_data_item_images_type_0 import (
            ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        type_ = self.type_

        language: None | str
        language = self.language

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        follower_count = self.follower_count

        subscriber_count: int | None
        subscriber_count = self.subscriber_count

        categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "language": language,
                "logo_url": logo_url,
                "images": images,
                "follower_count": follower_count,
                "subscriber_count": subscriber_count,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_podcasts_with_optional_search_response_200_data_item_images_type_0 import (
            ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0,  # noqa: PLC0415
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

        type_ = d.pop("type")

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAllPodcastsWithOptionalSearchResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        follower_count = d.pop("follower_count")

        def _parse_subscriber_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        subscriber_count = _parse_subscriber_count(d.pop("subscriber_count"))

        categories = cast(list[str], d.pop("categories"))

        list_all_podcasts_with_optional_search_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            language=language,
            logo_url=logo_url,
            images=images,
            follower_count=follower_count,
            subscriber_count=subscriber_count,
            categories=categories,
        )

        list_all_podcasts_with_optional_search_response_200_data_item.additional_properties = d
        return list_all_podcasts_with_optional_search_response_200_data_item

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
