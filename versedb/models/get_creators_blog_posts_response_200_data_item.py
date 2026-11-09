from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creators_blog_posts_response_200_data_item_author import (
        GetCreatorsBlogPostsResponse200DataItemAuthor,
    )
    from ..models.get_creators_blog_posts_response_200_data_item_category import (
        GetCreatorsBlogPostsResponse200DataItemCategory,
    )
    from ..models.get_creators_blog_posts_response_200_data_item_images_type_0 import (
        GetCreatorsBlogPostsResponse200DataItemImagesType0,
    )


T = TypeVar("T", bound="GetCreatorsBlogPostsResponse200DataItem")


@_attrs_define
class GetCreatorsBlogPostsResponse200DataItem:
    """
    Attributes:
        id (int):
        slug (None | str):
        title (None | str):
        featured_image_url (None | str):
        images (GetCreatorsBlogPostsResponse200DataItemImagesType0 | None):
        published_at (None | str):
        reading_time (int):
        category (GetCreatorsBlogPostsResponse200DataItemCategory | Unset):
        author (GetCreatorsBlogPostsResponse200DataItemAuthor | Unset):
    """

    id: int
    slug: None | str
    title: None | str
    featured_image_url: None | str
    images: GetCreatorsBlogPostsResponse200DataItemImagesType0 | None
    published_at: None | str
    reading_time: int
    category: GetCreatorsBlogPostsResponse200DataItemCategory | Unset = UNSET
    author: GetCreatorsBlogPostsResponse200DataItemAuthor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_creators_blog_posts_response_200_data_item_images_type_0 import (
            GetCreatorsBlogPostsResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        slug: None | str
        slug = self.slug

        title: None | str
        title = self.title

        featured_image_url: None | str
        featured_image_url = self.featured_image_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetCreatorsBlogPostsResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        published_at: None | str
        published_at = self.published_at

        reading_time = self.reading_time

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "title": title,
                "featured_image_url": featured_image_url,
                "images": images,
                "published_at": published_at,
                "reading_time": reading_time,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creators_blog_posts_response_200_data_item_author import (
            GetCreatorsBlogPostsResponse200DataItemAuthor,  # noqa: PLC0415
        )
        from ..models.get_creators_blog_posts_response_200_data_item_category import (
            GetCreatorsBlogPostsResponse200DataItemCategory,  # noqa: PLC0415
        )
        from ..models.get_creators_blog_posts_response_200_data_item_images_type_0 import (
            GetCreatorsBlogPostsResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_featured_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        featured_image_url = _parse_featured_image_url(d.pop("featured_image_url"))

        def _parse_images(data: object) -> GetCreatorsBlogPostsResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetCreatorsBlogPostsResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCreatorsBlogPostsResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        reading_time = d.pop("reading_time")

        _category = d.pop("category", UNSET)
        category: GetCreatorsBlogPostsResponse200DataItemCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetCreatorsBlogPostsResponse200DataItemCategory.from_dict(_category)

        _author = d.pop("author", UNSET)
        author: GetCreatorsBlogPostsResponse200DataItemAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = GetCreatorsBlogPostsResponse200DataItemAuthor.from_dict(_author)

        get_creators_blog_posts_response_200_data_item = cls(
            id=id,
            slug=slug,
            title=title,
            featured_image_url=featured_image_url,
            images=images,
            published_at=published_at,
            reading_time=reading_time,
            category=category,
            author=author,
        )

        get_creators_blog_posts_response_200_data_item.additional_properties = d
        return get_creators_blog_posts_response_200_data_item

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
