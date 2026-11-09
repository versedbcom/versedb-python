from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_a_specific_podcast_response_200_data_images_type_0 import (
        GetASpecificPodcastResponse200DataImagesType0,
    )
    from ..models.get_a_specific_podcast_response_200_data_platform_links_type_0 import (
        GetASpecificPodcastResponse200DataPlatformLinksType0,
    )
    from ..models.get_a_specific_podcast_response_200_data_platform_links_type_5 import (
        GetASpecificPodcastResponse200DataPlatformLinksType5,
    )
    from ..models.get_a_specific_podcast_response_200_data_social_links_type_0 import (
        GetASpecificPodcastResponse200DataSocialLinksType0,
    )
    from ..models.get_a_specific_podcast_response_200_data_website_url_type_4 import (
        GetASpecificPodcastResponse200DataWebsiteUrlType4,
    )


T = TypeVar("T", bound="GetASpecificPodcastResponse200Data")


@_attrs_define
class GetASpecificPodcastResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        type_ (str):
        language (None | str):
        logo_url (None | str):
        images (GetASpecificPodcastResponse200DataImagesType0 | None):
        website_url (bool | float | GetASpecificPodcastResponse200DataWebsiteUrlType4 | list[Any] | None | str):
            social_links.website as stored (a URL in production), or null; always printed.
        rss_feed_url (None | str):
        youtube_channel_id (None | str):
        social_links (GetASpecificPodcastResponse200DataSocialLinksType0 | list[Any] | None): Links by name, or null; an
            empty map prints as `[]`.
        platform_links (bool | float | GetASpecificPodcastResponse200DataPlatformLinksType0 |
            GetASpecificPodcastResponse200DataPlatformLinksType5 | list[Any] | None | str): Links by name, or null; an empty
            map prints as `[]`.
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
    images: GetASpecificPodcastResponse200DataImagesType0 | None
    website_url: bool | float | GetASpecificPodcastResponse200DataWebsiteUrlType4 | list[Any] | None | str
    rss_feed_url: None | str
    youtube_channel_id: None | str
    social_links: GetASpecificPodcastResponse200DataSocialLinksType0 | list[Any] | None
    platform_links: (
        bool
        | float
        | GetASpecificPodcastResponse200DataPlatformLinksType0
        | GetASpecificPodcastResponse200DataPlatformLinksType5
        | list[Any]
        | None
        | str
    )
    follower_count: int
    subscriber_count: int | None
    categories: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_a_specific_podcast_response_200_data_images_type_0 import (
            GetASpecificPodcastResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_platform_links_type_0 import (
            GetASpecificPodcastResponse200DataPlatformLinksType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_platform_links_type_5 import (
            GetASpecificPodcastResponse200DataPlatformLinksType5,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_social_links_type_0 import (
            GetASpecificPodcastResponse200DataSocialLinksType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_website_url_type_4 import (
            GetASpecificPodcastResponse200DataWebsiteUrlType4,  # noqa: PLC0415
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
        if isinstance(self.images, GetASpecificPodcastResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        website_url: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.website_url, list):
            website_url = self.website_url

        elif isinstance(self.website_url, GetASpecificPodcastResponse200DataWebsiteUrlType4):
            website_url = self.website_url.to_dict()
        else:
            website_url = self.website_url

        rss_feed_url: None | str
        rss_feed_url = self.rss_feed_url

        youtube_channel_id: None | str
        youtube_channel_id = self.youtube_channel_id

        social_links: dict[str, Any] | list[Any] | None
        if isinstance(self.social_links, GetASpecificPodcastResponse200DataSocialLinksType0):
            social_links = self.social_links.to_dict()
        elif isinstance(self.social_links, list):
            social_links = self.social_links

        else:
            social_links = self.social_links

        platform_links: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.platform_links, GetASpecificPodcastResponse200DataPlatformLinksType0):
            platform_links = self.platform_links.to_dict()
        elif isinstance(self.platform_links, list):
            platform_links = self.platform_links

        elif isinstance(self.platform_links, GetASpecificPodcastResponse200DataPlatformLinksType5):
            platform_links = self.platform_links.to_dict()
        else:
            platform_links = self.platform_links

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
                "website_url": website_url,
                "rss_feed_url": rss_feed_url,
                "youtube_channel_id": youtube_channel_id,
                "social_links": social_links,
                "platform_links": platform_links,
                "follower_count": follower_count,
                "subscriber_count": subscriber_count,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_podcast_response_200_data_images_type_0 import (
            GetASpecificPodcastResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_platform_links_type_0 import (
            GetASpecificPodcastResponse200DataPlatformLinksType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_platform_links_type_5 import (
            GetASpecificPodcastResponse200DataPlatformLinksType5,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_social_links_type_0 import (
            GetASpecificPodcastResponse200DataSocialLinksType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_podcast_response_200_data_website_url_type_4 import (
            GetASpecificPodcastResponse200DataWebsiteUrlType4,  # noqa: PLC0415
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

        def _parse_images(data: object) -> GetASpecificPodcastResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetASpecificPodcastResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetASpecificPodcastResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_website_url(
            data: object,
        ) -> bool | float | GetASpecificPodcastResponse200DataWebsiteUrlType4 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                website_url_type_3 = cast(list[Any], data)

                return website_url_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                website_url_type_4 = GetASpecificPodcastResponse200DataWebsiteUrlType4.from_dict(data)

                return website_url_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetASpecificPodcastResponse200DataWebsiteUrlType4 | list[Any] | None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_rss_feed_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rss_feed_url = _parse_rss_feed_url(d.pop("rss_feed_url"))

        def _parse_youtube_channel_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        youtube_channel_id = _parse_youtube_channel_id(d.pop("youtube_channel_id"))

        def _parse_social_links(data: object) -> GetASpecificPodcastResponse200DataSocialLinksType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_links_type_0 = GetASpecificPodcastResponse200DataSocialLinksType0.from_dict(data)

                return social_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                social_links_type_1 = cast(list[Any], data)

                return social_links_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetASpecificPodcastResponse200DataSocialLinksType0 | list[Any] | None, data)

        social_links = _parse_social_links(d.pop("social_links"))

        def _parse_platform_links(
            data: object,
        ) -> (
            bool
            | float
            | GetASpecificPodcastResponse200DataPlatformLinksType0
            | GetASpecificPodcastResponse200DataPlatformLinksType5
            | list[Any]
            | None
            | str
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_links_type_0 = GetASpecificPodcastResponse200DataPlatformLinksType0.from_dict(data)

                return platform_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platform_links_type_4 = cast(list[Any], data)

                return platform_links_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_links_type_5 = GetASpecificPodcastResponse200DataPlatformLinksType5.from_dict(data)

                return platform_links_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | GetASpecificPodcastResponse200DataPlatformLinksType0
                | GetASpecificPodcastResponse200DataPlatformLinksType5
                | list[Any]
                | None
                | str,
                data,
            )

        platform_links = _parse_platform_links(d.pop("platform_links"))

        follower_count = d.pop("follower_count")

        def _parse_subscriber_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        subscriber_count = _parse_subscriber_count(d.pop("subscriber_count"))

        categories = cast(list[str], d.pop("categories"))

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
