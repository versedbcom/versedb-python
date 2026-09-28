from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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


T = TypeVar("T", bound="GetCreatorsBlogPostsResponse200DataItem")


@_attrs_define
class GetCreatorsBlogPostsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        title (str | Unset):
        featured_image_url (str | Unset):
        category (GetCreatorsBlogPostsResponse200DataItemCategory | Unset):
        author (GetCreatorsBlogPostsResponse200DataItemAuthor | Unset):
        published_at (str | Unset):
        reading_time (int | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    title: str | Unset = UNSET
    featured_image_url: str | Unset = UNSET
    category: GetCreatorsBlogPostsResponse200DataItemCategory | Unset = UNSET
    author: GetCreatorsBlogPostsResponse200DataItemAuthor | Unset = UNSET
    published_at: str | Unset = UNSET
    reading_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        title = self.title

        featured_image_url = self.featured_image_url

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        published_at = self.published_at

        reading_time = self.reading_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if title is not UNSET:
            field_dict["title"] = title
        if featured_image_url is not UNSET:
            field_dict["featured_image_url"] = featured_image_url
        if category is not UNSET:
            field_dict["category"] = category
        if author is not UNSET:
            field_dict["author"] = author
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if reading_time is not UNSET:
            field_dict["reading_time"] = reading_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creators_blog_posts_response_200_data_item_author import (
            GetCreatorsBlogPostsResponse200DataItemAuthor,  # noqa: PLC0415
        )
        from ..models.get_creators_blog_posts_response_200_data_item_category import (
            GetCreatorsBlogPostsResponse200DataItemCategory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        title = d.pop("title", UNSET)

        featured_image_url = d.pop("featured_image_url", UNSET)

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

        published_at = d.pop("published_at", UNSET)

        reading_time = d.pop("reading_time", UNSET)

        get_creators_blog_posts_response_200_data_item = cls(
            id=id,
            slug=slug,
            title=title,
            featured_image_url=featured_image_url,
            category=category,
            author=author,
            published_at=published_at,
            reading_time=reading_time,
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
