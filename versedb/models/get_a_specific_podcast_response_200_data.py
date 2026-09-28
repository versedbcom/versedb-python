from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_a_specific_podcast_response_200_data_images import GetASpecificPodcastResponse200DataImages
    from ..models.get_a_specific_podcast_response_200_data_platform_links import (
        GetASpecificPodcastResponse200DataPlatformLinks,
    )
    from ..models.get_a_specific_podcast_response_200_data_social_links import (
        GetASpecificPodcastResponse200DataSocialLinks,
    )


T = TypeVar("T", bound="GetASpecificPodcastResponse200Data")


@_attrs_define
class GetASpecificPodcastResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        type_ (str | Unset):
        language (str | Unset):
        logo_url (str | Unset):
        images (GetASpecificPodcastResponse200DataImages | Unset):
        website_url (str | Unset):
        rss_feed_url (str | Unset):
        youtube_channel_id (None | str | Unset):
        social_links (GetASpecificPodcastResponse200DataSocialLinks | Unset):
        platform_links (GetASpecificPodcastResponse200DataPlatformLinks | Unset):
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
    images: GetASpecificPodcastResponse200DataImages | Unset = UNSET
    website_url: str | Unset = UNSET
    rss_feed_url: str | Unset = UNSET
    youtube_channel_id: None | str | Unset = UNSET
    social_links: GetASpecificPodcastResponse200DataSocialLinks | Unset = UNSET
    platform_links: GetASpecificPodcastResponse200DataPlatformLinks | Unset = UNSET
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

        website_url = self.website_url

        rss_feed_url = self.rss_feed_url

        youtube_channel_id: None | str | Unset
        if isinstance(self.youtube_channel_id, Unset):
            youtube_channel_id = UNSET
        else:
            youtube_channel_id = self.youtube_channel_id

        social_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.social_links, Unset):
            social_links = self.social_links.to_dict()

        platform_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_links, Unset):
            platform_links = self.platform_links.to_dict()

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
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if rss_feed_url is not UNSET:
            field_dict["rss_feed_url"] = rss_feed_url
        if youtube_channel_id is not UNSET:
            field_dict["youtube_channel_id"] = youtube_channel_id
        if social_links is not UNSET:
            field_dict["social_links"] = social_links
        if platform_links is not UNSET:
            field_dict["platform_links"] = platform_links
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if subscriber_count is not UNSET:
            field_dict["subscriber_count"] = subscriber_count
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_podcast_response_200_data_images import (
            GetASpecificPodcastResponse200DataImages,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_platform_links import (
            GetASpecificPodcastResponse200DataPlatformLinks,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_social_links import (
            GetASpecificPodcastResponse200DataSocialLinks,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        type_ = d.pop("type", UNSET)

        language = d.pop("language", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetASpecificPodcastResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetASpecificPodcastResponse200DataImages.from_dict(_images)

        website_url = d.pop("website_url", UNSET)

        rss_feed_url = d.pop("rss_feed_url", UNSET)

        def _parse_youtube_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        youtube_channel_id = _parse_youtube_channel_id(d.pop("youtube_channel_id", UNSET))

        _social_links = d.pop("social_links", UNSET)
        social_links: GetASpecificPodcastResponse200DataSocialLinks | Unset
        if isinstance(_social_links, Unset):
            social_links = UNSET
        else:
            social_links = GetASpecificPodcastResponse200DataSocialLinks.from_dict(_social_links)

        _platform_links = d.pop("platform_links", UNSET)
        platform_links: GetASpecificPodcastResponse200DataPlatformLinks | Unset
        if isinstance(_platform_links, Unset):
            platform_links = UNSET
        else:
            platform_links = GetASpecificPodcastResponse200DataPlatformLinks.from_dict(_platform_links)

        follower_count = d.pop("follower_count", UNSET)

        subscriber_count = d.pop("subscriber_count", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        get_a_specific_podcast_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            language=language,
            logo_url=logo_url,
            images=images,
            website_url=website_url,
            rss_feed_url=rss_feed_url,
            youtube_channel_id=youtube_channel_id,
            social_links=social_links,
            platform_links=platform_links,
            follower_count=follower_count,
            subscriber_count=subscriber_count,
            categories=categories,
        )

        get_a_specific_podcast_response_200_data.additional_properties = d
        return get_a_specific_podcast_response_200_data

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
