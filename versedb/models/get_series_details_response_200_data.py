from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_series_details_response_200_data_aliases_i18n import GetSeriesDetailsResponse200DataAliasesI18N
    from ..models.get_series_details_response_200_data_availabilities_item import (
        GetSeriesDetailsResponse200DataAvailabilitiesItem,
    )
    from ..models.get_series_details_response_200_data_awards_item import GetSeriesDetailsResponse200DataAwardsItem
    from ..models.get_series_details_response_200_data_characters_item import (
        GetSeriesDetailsResponse200DataCharactersItem,
    )
    from ..models.get_series_details_response_200_data_creators_item import GetSeriesDetailsResponse200DataCreatorsItem
    from ..models.get_series_details_response_200_data_effective_imprint_type_0 import (
        GetSeriesDetailsResponse200DataEffectiveImprintType0,
    )
    from ..models.get_series_details_response_200_data_foc_issues_item import (
        GetSeriesDetailsResponse200DataFocIssuesItem,
    )
    from ..models.get_series_details_response_200_data_foreign_edition_of_item import (
        GetSeriesDetailsResponse200DataForeignEditionOfItem,
    )
    from ..models.get_series_details_response_200_data_foreign_editions_item import (
        GetSeriesDetailsResponse200DataForeignEditionsItem,
    )
    from ..models.get_series_details_response_200_data_genres_item import GetSeriesDetailsResponse200DataGenresItem
    from ..models.get_series_details_response_200_data_images_type_0 import GetSeriesDetailsResponse200DataImagesType0
    from ..models.get_series_details_response_200_data_imprint_type_0 import GetSeriesDetailsResponse200DataImprintType0
    from ..models.get_series_details_response_200_data_name_i18n import GetSeriesDetailsResponse200DataNameI18N
    from ..models.get_series_details_response_200_data_publisher import GetSeriesDetailsResponse200DataPublisher
    from ..models.get_series_details_response_200_data_publishers_item import (
        GetSeriesDetailsResponse200DataPublishersItem,
    )
    from ..models.get_series_details_response_200_data_teams_item import GetSeriesDetailsResponse200DataTeamsItem
    from ..models.get_series_details_response_200_data_title_type_0 import GetSeriesDetailsResponse200DataTitleType0
    from ..models.get_series_details_response_200_data_upcoming_issues_item import (
        GetSeriesDetailsResponse200DataUpcomingIssuesItem,
    )


T = TypeVar("T", bound="GetSeriesDetailsResponse200Data")


@_attrs_define
class GetSeriesDetailsResponse200Data:
    """
    Attributes:
        id (int):
        title_id (int | None):
        name (None | str):
        original_name (None | str):
        display_name (str):
        slug (None | str):
        number (int | None):
        start_year (int | None):
        end_year (int | None):
        cover_url (None | str):
        images (GetSeriesDetailsResponse200DataImagesType0 | None):
        publisher_description (None | str):
        medium (None | str):
        adapted_from (None | str):
        publication_type (None | str):
        format_ (None | str):
        status (None | str):
        original_language (None | str):
        cached_issues_count (int | None):
        cached_creators_count (int):
        cached_characters_count (int):
        cached_teams_count (int):
        lists_count (int):
        average_rating (None | str):
        total_reviews (int | None):
        issues_average_rating (None | str):
        issues_rated_count (int | None):
        imprint_id (int | None):
        content_rating_label (None | str):
        min_age (int | None):
        language (None | str):
        aliases (list[str] | None):
        is_nsfw (bool | None):
        title (GetSeriesDetailsResponse200DataTitleType0 | None):
        publishers (list[GetSeriesDetailsResponse200DataPublishersItem]):
        imprint (GetSeriesDetailsResponse200DataImprintType0 | None):
        effective_imprint (GetSeriesDetailsResponse200DataEffectiveImprintType0 | None):
        genres (list[GetSeriesDetailsResponse200DataGenresItem]):
        awards (list[GetSeriesDetailsResponse200DataAwardsItem]):
        foreign_edition_of (list[GetSeriesDetailsResponse200DataForeignEditionOfItem]):
        foreign_editions (list[GetSeriesDetailsResponse200DataForeignEditionsItem]):
        availabilities (list[GetSeriesDetailsResponse200DataAvailabilitiesItem]):
        creators (list[GetSeriesDetailsResponse200DataCreatorsItem]):
        foc_issues (list[GetSeriesDetailsResponse200DataFocIssuesItem]):
        upcoming_issues (list[GetSeriesDetailsResponse200DataUpcomingIssuesItem]):
        name_i18n (GetSeriesDetailsResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetSeriesDetailsResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the series is from, a BCP 47 tag.
        publisher (GetSeriesDetailsResponse200DataPublisher | Unset):
        characters (list[GetSeriesDetailsResponse200DataCharactersItem] | Unset):
        teams (list[GetSeriesDetailsResponse200DataTeamsItem] | Unset):
    """

    id: int
    title_id: int | None
    name: None | str
    original_name: None | str
    display_name: str
    slug: None | str
    number: int | None
    start_year: int | None
    end_year: int | None
    cover_url: None | str
    images: GetSeriesDetailsResponse200DataImagesType0 | None
    publisher_description: None | str
    medium: None | str
    adapted_from: None | str
    publication_type: None | str
    format_: None | str
    status: None | str
    original_language: None | str
    cached_issues_count: int | None
    cached_creators_count: int
    cached_characters_count: int
    cached_teams_count: int
    lists_count: int
    average_rating: None | str
    total_reviews: int | None
    issues_average_rating: None | str
    issues_rated_count: int | None
    imprint_id: int | None
    content_rating_label: None | str
    min_age: int | None
    language: None | str
    aliases: list[str] | None
    is_nsfw: bool | None
    title: GetSeriesDetailsResponse200DataTitleType0 | None
    publishers: list[GetSeriesDetailsResponse200DataPublishersItem]
    imprint: GetSeriesDetailsResponse200DataImprintType0 | None
    effective_imprint: GetSeriesDetailsResponse200DataEffectiveImprintType0 | None
    genres: list[GetSeriesDetailsResponse200DataGenresItem]
    awards: list[GetSeriesDetailsResponse200DataAwardsItem]
    foreign_edition_of: list[GetSeriesDetailsResponse200DataForeignEditionOfItem]
    foreign_editions: list[GetSeriesDetailsResponse200DataForeignEditionsItem]
    availabilities: list[GetSeriesDetailsResponse200DataAvailabilitiesItem]
    creators: list[GetSeriesDetailsResponse200DataCreatorsItem]
    foc_issues: list[GetSeriesDetailsResponse200DataFocIssuesItem]
    upcoming_issues: list[GetSeriesDetailsResponse200DataUpcomingIssuesItem]
    name_i18n: GetSeriesDetailsResponse200DataNameI18N
    aliases_i18n: GetSeriesDetailsResponse200DataAliasesI18N
    original_locale: None | str
    publisher: GetSeriesDetailsResponse200DataPublisher | Unset = UNSET
    characters: list[GetSeriesDetailsResponse200DataCharactersItem] | Unset = UNSET
    teams: list[GetSeriesDetailsResponse200DataTeamsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_details_response_200_data_effective_imprint_type_0 import (
            GetSeriesDetailsResponse200DataEffectiveImprintType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_images_type_0 import (
            GetSeriesDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_imprint_type_0 import (
            GetSeriesDetailsResponse200DataImprintType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_title_type_0 import GetSeriesDetailsResponse200DataTitleType0  # noqa: PLC0415

        id = self.id

        title_id: int | None
        title_id = self.title_id

        name: None | str
        name = self.name

        original_name: None | str
        original_name = self.original_name

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
        if isinstance(self.images, GetSeriesDetailsResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        publisher_description: None | str
        publisher_description = self.publisher_description

        medium: None | str
        medium = self.medium

        adapted_from: None | str
        adapted_from = self.adapted_from

        publication_type: None | str
        publication_type = self.publication_type

        format_: None | str
        format_ = self.format_

        status: None | str
        status = self.status

        original_language: None | str
        original_language = self.original_language

        cached_issues_count: int | None
        cached_issues_count = self.cached_issues_count

        cached_creators_count = self.cached_creators_count

        cached_characters_count = self.cached_characters_count

        cached_teams_count = self.cached_teams_count

        lists_count = self.lists_count

        average_rating: None | str
        average_rating = self.average_rating

        total_reviews: int | None
        total_reviews = self.total_reviews

        issues_average_rating: None | str
        issues_average_rating = self.issues_average_rating

        issues_rated_count: int | None
        issues_rated_count = self.issues_rated_count

        imprint_id: int | None
        imprint_id = self.imprint_id

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        language: None | str
        language = self.language

        aliases: list[str] | None
        if isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        title: dict[str, Any] | None
        if isinstance(self.title, GetSeriesDetailsResponse200DataTitleType0):
            title = self.title.to_dict()
        else:
            title = self.title

        publishers = []
        for publishers_item_data in self.publishers:
            publishers_item = publishers_item_data.to_dict()
            publishers.append(publishers_item)

        imprint: dict[str, Any] | None
        if isinstance(self.imprint, GetSeriesDetailsResponse200DataImprintType0):
            imprint = self.imprint.to_dict()
        else:
            imprint = self.imprint

        effective_imprint: dict[str, Any] | None
        if isinstance(self.effective_imprint, GetSeriesDetailsResponse200DataEffectiveImprintType0):
            effective_imprint = self.effective_imprint.to_dict()
        else:
            effective_imprint = self.effective_imprint

        genres = []
        for genres_item_data in self.genres:
            genres_item = genres_item_data.to_dict()
            genres.append(genres_item)

        awards = []
        for awards_item_data in self.awards:
            awards_item = awards_item_data.to_dict()
            awards.append(awards_item)

        foreign_edition_of = []
        for foreign_edition_of_item_data in self.foreign_edition_of:
            foreign_edition_of_item = foreign_edition_of_item_data.to_dict()
            foreign_edition_of.append(foreign_edition_of_item)

        foreign_editions = []
        for foreign_editions_item_data in self.foreign_editions:
            foreign_editions_item = foreign_editions_item_data.to_dict()
            foreign_editions.append(foreign_editions_item)

        availabilities = []
        for availabilities_item_data in self.availabilities:
            availabilities_item = availabilities_item_data.to_dict()
            availabilities.append(availabilities_item)

        creators = []
        for creators_item_data in self.creators:
            creators_item = creators_item_data.to_dict()
            creators.append(creators_item)

        foc_issues = []
        for foc_issues_item_data in self.foc_issues:
            foc_issues_item = foc_issues_item_data.to_dict()
            foc_issues.append(foc_issues_item)

        upcoming_issues = []
        for upcoming_issues_item_data in self.upcoming_issues:
            upcoming_issues_item = upcoming_issues_item_data.to_dict()
            upcoming_issues.append(upcoming_issues_item)

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title_id": title_id,
                "name": name,
                "original_name": original_name,
                "display_name": display_name,
                "slug": slug,
                "number": number,
                "start_year": start_year,
                "end_year": end_year,
                "cover_url": cover_url,
                "images": images,
                "publisher_description": publisher_description,
                "medium": medium,
                "adapted_from": adapted_from,
                "publication_type": publication_type,
                "format": format_,
                "status": status,
                "original_language": original_language,
                "cached_issues_count": cached_issues_count,
                "cached_creators_count": cached_creators_count,
                "cached_characters_count": cached_characters_count,
                "cached_teams_count": cached_teams_count,
                "lists_count": lists_count,
                "average_rating": average_rating,
                "total_reviews": total_reviews,
                "issues_average_rating": issues_average_rating,
                "issues_rated_count": issues_rated_count,
                "imprint_id": imprint_id,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "language": language,
                "aliases": aliases,
                "is_nsfw": is_nsfw,
                "title": title,
                "publishers": publishers,
                "imprint": imprint,
                "effective_imprint": effective_imprint,
                "genres": genres,
                "awards": awards,
                "foreign_edition_of": foreign_edition_of,
                "foreign_editions": foreign_editions,
                "availabilities": availabilities,
                "creators": creators,
                "foc_issues": foc_issues,
                "upcoming_issues": upcoming_issues,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if characters is not UNSET:
            field_dict["characters"] = characters
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_details_response_200_data_aliases_i18n import (
            GetSeriesDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_availabilities_item import (
            GetSeriesDetailsResponse200DataAvailabilitiesItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_awards_item import GetSeriesDetailsResponse200DataAwardsItem  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_characters_item import (
            GetSeriesDetailsResponse200DataCharactersItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_creators_item import (
            GetSeriesDetailsResponse200DataCreatorsItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_effective_imprint_type_0 import (
            GetSeriesDetailsResponse200DataEffectiveImprintType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_foc_issues_item import (
            GetSeriesDetailsResponse200DataFocIssuesItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_foreign_edition_of_item import (
            GetSeriesDetailsResponse200DataForeignEditionOfItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_foreign_editions_item import (
            GetSeriesDetailsResponse200DataForeignEditionsItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_genres_item import GetSeriesDetailsResponse200DataGenresItem  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_images_type_0 import (
            GetSeriesDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_imprint_type_0 import (
            GetSeriesDetailsResponse200DataImprintType0,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_name_i18n import GetSeriesDetailsResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_publisher import GetSeriesDetailsResponse200DataPublisher  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_publishers_item import (
            GetSeriesDetailsResponse200DataPublishersItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_teams_item import GetSeriesDetailsResponse200DataTeamsItem  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_title_type_0 import GetSeriesDetailsResponse200DataTitleType0  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_upcoming_issues_item import (
            GetSeriesDetailsResponse200DataUpcomingIssuesItem,  # noqa: PLC0415
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

        def _parse_original_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_name = _parse_original_name(d.pop("original_name"))

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

        def _parse_images(data: object) -> GetSeriesDetailsResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetSeriesDetailsResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesDetailsResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_publisher_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_description = _parse_publisher_description(d.pop("publisher_description"))

        def _parse_medium(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        medium = _parse_medium(d.pop("medium"))

        def _parse_adapted_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        adapted_from = _parse_adapted_from(d.pop("adapted_from"))

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

        def _parse_original_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_language = _parse_original_language(d.pop("original_language"))

        def _parse_cached_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cached_issues_count = _parse_cached_issues_count(d.pop("cached_issues_count"))

        cached_creators_count = d.pop("cached_creators_count")

        cached_characters_count = d.pop("cached_characters_count")

        cached_teams_count = d.pop("cached_teams_count")

        lists_count = d.pop("lists_count")

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

        def _parse_imprint_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        imprint_id = _parse_imprint_id(d.pop("imprint_id"))

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

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        def _parse_aliases(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        aliases = _parse_aliases(d.pop("aliases"))

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_title(data: object) -> GetSeriesDetailsResponse200DataTitleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                title_type_0 = GetSeriesDetailsResponse200DataTitleType0.from_dict(data)

                return title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesDetailsResponse200DataTitleType0 | None, data)

        title = _parse_title(d.pop("title"))

        publishers = []
        _publishers = d.pop("publishers")
        for publishers_item_data in _publishers:
            publishers_item = GetSeriesDetailsResponse200DataPublishersItem.from_dict(publishers_item_data)

            publishers.append(publishers_item)

        def _parse_imprint(data: object) -> GetSeriesDetailsResponse200DataImprintType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                imprint_type_0 = GetSeriesDetailsResponse200DataImprintType0.from_dict(data)

                return imprint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesDetailsResponse200DataImprintType0 | None, data)

        imprint = _parse_imprint(d.pop("imprint"))

        def _parse_effective_imprint(data: object) -> GetSeriesDetailsResponse200DataEffectiveImprintType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_imprint_type_0 = GetSeriesDetailsResponse200DataEffectiveImprintType0.from_dict(data)

                return effective_imprint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesDetailsResponse200DataEffectiveImprintType0 | None, data)

        effective_imprint = _parse_effective_imprint(d.pop("effective_imprint"))

        genres = []
        _genres = d.pop("genres")
        for genres_item_data in _genres:
            genres_item = GetSeriesDetailsResponse200DataGenresItem.from_dict(genres_item_data)

            genres.append(genres_item)

        awards = []
        _awards = d.pop("awards")
        for awards_item_data in _awards:
            awards_item = GetSeriesDetailsResponse200DataAwardsItem.from_dict(awards_item_data)

            awards.append(awards_item)

        foreign_edition_of = []
        _foreign_edition_of = d.pop("foreign_edition_of")
        for foreign_edition_of_item_data in _foreign_edition_of:
            foreign_edition_of_item = GetSeriesDetailsResponse200DataForeignEditionOfItem.from_dict(
                foreign_edition_of_item_data
            )

            foreign_edition_of.append(foreign_edition_of_item)

        foreign_editions = []
        _foreign_editions = d.pop("foreign_editions")
        for foreign_editions_item_data in _foreign_editions:
            foreign_editions_item = GetSeriesDetailsResponse200DataForeignEditionsItem.from_dict(
                foreign_editions_item_data
            )

            foreign_editions.append(foreign_editions_item)

        availabilities = []
        _availabilities = d.pop("availabilities")
        for availabilities_item_data in _availabilities:
            availabilities_item = GetSeriesDetailsResponse200DataAvailabilitiesItem.from_dict(availabilities_item_data)

            availabilities.append(availabilities_item)

        creators = []
        _creators = d.pop("creators")
        for creators_item_data in _creators:
            creators_item = GetSeriesDetailsResponse200DataCreatorsItem.from_dict(creators_item_data)

            creators.append(creators_item)

        foc_issues = []
        _foc_issues = d.pop("foc_issues")
        for foc_issues_item_data in _foc_issues:
            foc_issues_item = GetSeriesDetailsResponse200DataFocIssuesItem.from_dict(foc_issues_item_data)

            foc_issues.append(foc_issues_item)

        upcoming_issues = []
        _upcoming_issues = d.pop("upcoming_issues")
        for upcoming_issues_item_data in _upcoming_issues:
            upcoming_issues_item = GetSeriesDetailsResponse200DataUpcomingIssuesItem.from_dict(
                upcoming_issues_item_data
            )

            upcoming_issues.append(upcoming_issues_item)

        name_i18n = GetSeriesDetailsResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetSeriesDetailsResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        _publisher = d.pop("publisher", UNSET)
        publisher: GetSeriesDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetSeriesDetailsResponse200DataPublisher.from_dict(_publisher)

        _characters = d.pop("characters", UNSET)
        characters: list[GetSeriesDetailsResponse200DataCharactersItem] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = GetSeriesDetailsResponse200DataCharactersItem.from_dict(characters_item_data)

                characters.append(characters_item)

        _teams = d.pop("teams", UNSET)
        teams: list[GetSeriesDetailsResponse200DataTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = GetSeriesDetailsResponse200DataTeamsItem.from_dict(teams_item_data)

                teams.append(teams_item)

        get_series_details_response_200_data = cls(
            id=id,
            title_id=title_id,
            name=name,
            original_name=original_name,
            display_name=display_name,
            slug=slug,
            number=number,
            start_year=start_year,
            end_year=end_year,
            cover_url=cover_url,
            images=images,
            publisher_description=publisher_description,
            medium=medium,
            adapted_from=adapted_from,
            publication_type=publication_type,
            format_=format_,
            status=status,
            original_language=original_language,
            cached_issues_count=cached_issues_count,
            cached_creators_count=cached_creators_count,
            cached_characters_count=cached_characters_count,
            cached_teams_count=cached_teams_count,
            lists_count=lists_count,
            average_rating=average_rating,
            total_reviews=total_reviews,
            issues_average_rating=issues_average_rating,
            issues_rated_count=issues_rated_count,
            imprint_id=imprint_id,
            content_rating_label=content_rating_label,
            min_age=min_age,
            language=language,
            aliases=aliases,
            is_nsfw=is_nsfw,
            title=title,
            publishers=publishers,
            imprint=imprint,
            effective_imprint=effective_imprint,
            genres=genres,
            awards=awards,
            foreign_edition_of=foreign_edition_of,
            foreign_editions=foreign_editions,
            availabilities=availabilities,
            creators=creators,
            foc_issues=foc_issues,
            upcoming_issues=upcoming_issues,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            publisher=publisher,
            characters=characters,
            teams=teams,
        )

        get_series_details_response_200_data.additional_properties = d
        return get_series_details_response_200_data

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
