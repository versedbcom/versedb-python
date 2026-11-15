from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_character_series_response_200_data_item_aliases_i18n import (
        GetCharacterSeriesResponse200DataItemAliasesI18N,
    )
    from ..models.get_character_series_response_200_data_item_images_type_0 import (
        GetCharacterSeriesResponse200DataItemImagesType0,
    )
    from ..models.get_character_series_response_200_data_item_name_i18n import (
        GetCharacterSeriesResponse200DataItemNameI18N,
    )


T = TypeVar("T", bound="GetCharacterSeriesResponse200DataItem")


@_attrs_define
class GetCharacterSeriesResponse200DataItem:
    """
    Attributes:
        id (int):
        title_id (int | None):
        name (None | str):
        display_name (str):
        slug (None | str):
        number (int | None):
        start_year (int | None):
        end_year (int | None):
        cover_url (None | str):
        images (GetCharacterSeriesResponse200DataItemImagesType0 | None):
        medium (None | str):
        publication_type (None | str):
        format_ (None | str):
        status (None | str):
        original_name (None | str):
        original_language (None | str):
        language (None | str):
        cached_issues_count (int | None):
        average_rating (None | str):
        total_reviews (int | None):
        issues_average_rating (None | str):
        issues_rated_count (int | None):
        content_rating_label (None | str):
        min_age (int | None):
        is_nsfw (bool | None):
        publisher_name (None | str):
        name_i18n (GetCharacterSeriesResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetCharacterSeriesResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the series is from, a BCP 47 tag.
    """

    id: int
    title_id: int | None
    name: None | str
    display_name: str
    slug: None | str
    number: int | None
    start_year: int | None
    end_year: int | None
    cover_url: None | str
    images: GetCharacterSeriesResponse200DataItemImagesType0 | None
    medium: None | str
    publication_type: None | str
    format_: None | str
    status: None | str
    original_name: None | str
    original_language: None | str
    language: None | str
    cached_issues_count: int | None
    average_rating: None | str
    total_reviews: int | None
    issues_average_rating: None | str
    issues_rated_count: int | None
    content_rating_label: None | str
    min_age: int | None
    is_nsfw: bool | None
    publisher_name: None | str
    name_i18n: GetCharacterSeriesResponse200DataItemNameI18N
    aliases_i18n: GetCharacterSeriesResponse200DataItemAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_character_series_response_200_data_item_images_type_0 import (
            GetCharacterSeriesResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        title_id: int | None
        title_id = self.title_id

        name: None | str
        name = self.name

        display_name = self.display_name

        slug: None | str
        slug = self.slug

        number: int | None
        number = self.number

        start_year: int | None
        start_year = self.start_year

        end_year: int | None
        end_year = self.end_year

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetCharacterSeriesResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        medium: None | str
        medium = self.medium

        publication_type: None | str
        publication_type = self.publication_type

        format_: None | str
        format_ = self.format_

        status: None | str
        status = self.status

        original_name: None | str
        original_name = self.original_name

        original_language: None | str
        original_language = self.original_language

        language: None | str
        language = self.language

        cached_issues_count: int | None
        cached_issues_count = self.cached_issues_count

        average_rating: None | str
        average_rating = self.average_rating

        total_reviews: int | None
        total_reviews = self.total_reviews

        issues_average_rating: None | str
        issues_average_rating = self.issues_average_rating

        issues_rated_count: int | None
        issues_rated_count = self.issues_rated_count

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        publisher_name: None | str
        publisher_name = self.publisher_name

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title_id": title_id,
                "name": name,
                "display_name": display_name,
                "slug": slug,
                "number": number,
                "start_year": start_year,
                "end_year": end_year,
                "cover_url": cover_url,
                "images": images,
                "medium": medium,
                "publication_type": publication_type,
                "format": format_,
                "status": status,
                "original_name": original_name,
                "original_language": original_language,
                "language": language,
                "cached_issues_count": cached_issues_count,
                "average_rating": average_rating,
                "total_reviews": total_reviews,
                "issues_average_rating": issues_average_rating,
                "issues_rated_count": issues_rated_count,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "is_nsfw": is_nsfw,
                "publisher_name": publisher_name,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_character_series_response_200_data_item_aliases_i18n import (
            GetCharacterSeriesResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_character_series_response_200_data_item_images_type_0 import (
            GetCharacterSeriesResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.get_character_series_response_200_data_item_name_i18n import (
            GetCharacterSeriesResponse200DataItemNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_title_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        title_id = _parse_title_id(d.pop("title_id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        display_name = d.pop("display_name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        number = _parse_number(d.pop("number"))

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

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> GetCharacterSeriesResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetCharacterSeriesResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCharacterSeriesResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_medium(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        medium = _parse_medium(d.pop("medium"))

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

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_original_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_name = _parse_original_name(d.pop("original_name"))

        def _parse_original_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_language = _parse_original_language(d.pop("original_language"))

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        def _parse_cached_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cached_issues_count = _parse_cached_issues_count(d.pop("cached_issues_count"))

        def _parse_average_rating(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        average_rating = _parse_average_rating(d.pop("average_rating"))

        def _parse_total_reviews(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_reviews = _parse_total_reviews(d.pop("total_reviews"))

        def _parse_issues_average_rating(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issues_average_rating = _parse_issues_average_rating(d.pop("issues_average_rating"))

        def _parse_issues_rated_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issues_rated_count = _parse_issues_rated_count(d.pop("issues_rated_count"))

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

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name"))

        name_i18n = GetCharacterSeriesResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetCharacterSeriesResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        get_character_series_response_200_data_item = cls(
            id=id,
            title_id=title_id,
            name=name,
            display_name=display_name,
            slug=slug,
            number=number,
            start_year=start_year,
            end_year=end_year,
            cover_url=cover_url,
            images=images,
            medium=medium,
            publication_type=publication_type,
            format_=format_,
            status=status,
            original_name=original_name,
            original_language=original_language,
            language=language,
            cached_issues_count=cached_issues_count,
            average_rating=average_rating,
            total_reviews=total_reviews,
            issues_average_rating=issues_average_rating,
            issues_rated_count=issues_rated_count,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            publisher_name=publisher_name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        get_character_series_response_200_data_item.additional_properties = d
        return get_character_series_response_200_data_item

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
