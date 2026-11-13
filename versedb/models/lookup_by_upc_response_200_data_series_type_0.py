from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_by_upc_response_200_data_series_type_0_foreign_edition_of_item import (
        LookupByUpcResponse200DataSeriesType0ForeignEditionOfItem,
    )
    from ..models.lookup_by_upc_response_200_data_series_type_0_foreign_editions_item import (
        LookupByUpcResponse200DataSeriesType0ForeignEditionsItem,
    )
    from ..models.lookup_by_upc_response_200_data_series_type_0_genres_item import (
        LookupByUpcResponse200DataSeriesType0GenresItem,
    )
    from ..models.lookup_by_upc_response_200_data_series_type_0_imprint_type_0 import (
        LookupByUpcResponse200DataSeriesType0ImprintType0,
    )


T = TypeVar("T", bound="LookupByUpcResponse200DataSeriesType0")


@_attrs_define
class LookupByUpcResponse200DataSeriesType0:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        start_year (int | None):
        end_year (int | None):
        volume_number (int | None):
        status (None | str):
        publication_type (None | str):
        cached_issues_count (int | None):
        medium (str):
        format_ (None | str):
        content_rating_label (None | str):
        min_age (int | None):
        is_nsfw (bool):
        original_language (None | str):
        language (None | str):
        genres (list[LookupByUpcResponse200DataSeriesType0GenresItem]):
        aliases (list[str]):
        imprint (LookupByUpcResponse200DataSeriesType0ImprintType0 | None):
        foreign_edition_of (list[LookupByUpcResponse200DataSeriesType0ForeignEditionOfItem]):
        foreign_editions (list[LookupByUpcResponse200DataSeriesType0ForeignEditionsItem]):
    """

    id: int
    name: None | str
    slug: None | str
    start_year: int | None
    end_year: int | None
    volume_number: int | None
    status: None | str
    publication_type: None | str
    cached_issues_count: int | None
    medium: str
    format_: None | str
    content_rating_label: None | str
    min_age: int | None
    is_nsfw: bool
    original_language: None | str
    language: None | str
    genres: list[LookupByUpcResponse200DataSeriesType0GenresItem]
    aliases: list[str]
    imprint: LookupByUpcResponse200DataSeriesType0ImprintType0 | None
    foreign_edition_of: list[LookupByUpcResponse200DataSeriesType0ForeignEditionOfItem]
    foreign_editions: list[LookupByUpcResponse200DataSeriesType0ForeignEditionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookup_by_upc_response_200_data_series_type_0_imprint_type_0 import (
            LookupByUpcResponse200DataSeriesType0ImprintType0,  # noqa: PLC0415
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

        status: None | str
        status = self.status

        publication_type: None | str
        publication_type = self.publication_type

        cached_issues_count: int | None
        cached_issues_count = self.cached_issues_count

        medium = self.medium

        format_: None | str
        format_ = self.format_

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        is_nsfw = self.is_nsfw

        original_language: None | str
        original_language = self.original_language

        language: None | str
        language = self.language

        genres = []
        for genres_item_data in self.genres:
            genres_item = genres_item_data.to_dict()
            genres.append(genres_item)

        aliases = self.aliases

        imprint: dict[str, Any] | None
        if isinstance(self.imprint, LookupByUpcResponse200DataSeriesType0ImprintType0):
            imprint = self.imprint.to_dict()
        else:
            imprint = self.imprint

        foreign_edition_of = []
        for foreign_edition_of_item_data in self.foreign_edition_of:
            foreign_edition_of_item = foreign_edition_of_item_data.to_dict()
            foreign_edition_of.append(foreign_edition_of_item)

        foreign_editions = []
        for foreign_editions_item_data in self.foreign_editions:
            foreign_editions_item = foreign_editions_item_data.to_dict()
            foreign_editions.append(foreign_editions_item)

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
                "status": status,
                "publication_type": publication_type,
                "cached_issues_count": cached_issues_count,
                "medium": medium,
                "format": format_,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "is_nsfw": is_nsfw,
                "original_language": original_language,
                "language": language,
                "genres": genres,
                "aliases": aliases,
                "imprint": imprint,
                "foreign_edition_of": foreign_edition_of,
                "foreign_editions": foreign_editions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_upc_response_200_data_series_type_0_foreign_edition_of_item import (
            LookupByUpcResponse200DataSeriesType0ForeignEditionOfItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_upc_response_200_data_series_type_0_foreign_editions_item import (
            LookupByUpcResponse200DataSeriesType0ForeignEditionsItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_upc_response_200_data_series_type_0_genres_item import (
            LookupByUpcResponse200DataSeriesType0GenresItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_upc_response_200_data_series_type_0_imprint_type_0 import (
            LookupByUpcResponse200DataSeriesType0ImprintType0,  # noqa: PLC0415
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

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_publication_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publication_type = _parse_publication_type(d.pop("publication_type"))

        def _parse_cached_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cached_issues_count = _parse_cached_issues_count(d.pop("cached_issues_count"))

        medium = d.pop("medium")

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

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

        is_nsfw = d.pop("is_nsfw")

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

        genres = []
        _genres = d.pop("genres")
        for genres_item_data in _genres:
            genres_item = LookupByUpcResponse200DataSeriesType0GenresItem.from_dict(genres_item_data)

            genres.append(genres_item)

        aliases = cast(list[str], d.pop("aliases"))

        def _parse_imprint(data: object) -> LookupByUpcResponse200DataSeriesType0ImprintType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                imprint_type_0 = LookupByUpcResponse200DataSeriesType0ImprintType0.from_dict(data)

                return imprint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookupByUpcResponse200DataSeriesType0ImprintType0 | None, data)

        imprint = _parse_imprint(d.pop("imprint"))

        foreign_edition_of = []
        _foreign_edition_of = d.pop("foreign_edition_of")
        for foreign_edition_of_item_data in _foreign_edition_of:
            foreign_edition_of_item = LookupByUpcResponse200DataSeriesType0ForeignEditionOfItem.from_dict(
                foreign_edition_of_item_data
            )

            foreign_edition_of.append(foreign_edition_of_item)

        foreign_editions = []
        _foreign_editions = d.pop("foreign_editions")
        for foreign_editions_item_data in _foreign_editions:
            foreign_editions_item = LookupByUpcResponse200DataSeriesType0ForeignEditionsItem.from_dict(
                foreign_editions_item_data
            )

            foreign_editions.append(foreign_editions_item)

        lookup_by_upc_response_200_data_series_type_0 = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            volume_number=volume_number,
            status=status,
            publication_type=publication_type,
            cached_issues_count=cached_issues_count,
            medium=medium,
            format_=format_,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            original_language=original_language,
            language=language,
            genres=genres,
            aliases=aliases,
            imprint=imprint,
            foreign_edition_of=foreign_edition_of,
            foreign_editions=foreign_editions,
        )

        lookup_by_upc_response_200_data_series_type_0.additional_properties = d
        return lookup_by_upc_response_200_data_series_type_0

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
