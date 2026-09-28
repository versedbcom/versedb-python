from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_all_podcasts_with_optional_search_response_200_data_item_images import (
        ListAllPodcastsWithOptionalSearchResponse200DataItemImages,
    )


T = TypeVar("T", bound="ListAllPodcastsWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllPodcastsWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        type_ (str | Unset):
        language (str | Unset):
        logo_url (str | Unset):
        images (ListAllPodcastsWithOptionalSearchResponse200DataItemImages | Unset):
        follower_count (int | Unset):
        subscriber_count (int | Unset):
        categories (list[str] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: str | Unset = UNSET
    language: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: ListAllPodcastsWithOptionalSearchResponse200DataItemImages | Unset = UNSET
    follower_count: int | Unset = UNSET
    subscriber_count: int | Unset = UNSET
    categories: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        type_ = self.type_

        language = self.language

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        follower_count = self.follower_count

        subscriber_count = self.subscriber_count

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_
        if language is not UNSET:
            field_dict["language"] = language
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if subscriber_count is not UNSET:
            field_dict["subscriber_count"] = subscriber_count
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_podcasts_with_optional_search_response_200_data_item_images import (
            ListAllPodcastsWithOptionalSearchResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        type_ = d.pop("type", UNSET)

        language = d.pop("language", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListAllPodcastsWithOptionalSearchResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListAllPodcastsWithOptionalSearchResponse200DataItemImages.from_dict(_images)

        follower_count = d.pop("follower_count", UNSET)

        subscriber_count = d.pop("subscriber_count", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

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
