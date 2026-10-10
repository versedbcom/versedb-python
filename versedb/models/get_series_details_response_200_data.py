from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_series_details_response_200_data_characters_item import (
        GetSeriesDetailsResponse200DataCharactersItem,
    )
    from ..models.get_series_details_response_200_data_creators_item import GetSeriesDetailsResponse200DataCreatorsItem
    from ..models.get_series_details_response_200_data_foc_issues_item import (
        GetSeriesDetailsResponse200DataFocIssuesItem,
    )
    from ..models.get_series_details_response_200_data_genres_item import GetSeriesDetailsResponse200DataGenresItem
    from ..models.get_series_details_response_200_data_last_edited_by import GetSeriesDetailsResponse200DataLastEditedBy
    from ..models.get_series_details_response_200_data_publisher import GetSeriesDetailsResponse200DataPublisher
    from ..models.get_series_details_response_200_data_publishers_item import (
        GetSeriesDetailsResponse200DataPublishersItem,
    )
    from ..models.get_series_details_response_200_data_teams_item import GetSeriesDetailsResponse200DataTeamsItem
    from ..models.get_series_details_response_200_data_title import GetSeriesDetailsResponse200DataTitle
    from ..models.get_series_details_response_200_data_upcoming_issues_item import (
        GetSeriesDetailsResponse200DataUpcomingIssuesItem,
    )


T = TypeVar("T", bound="GetSeriesDetailsResponse200Data")


@_attrs_define
class GetSeriesDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        title_id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        number (int | Unset):
        start_year (int | Unset):
        end_year (int | Unset):
        cover_url (str | Unset):
        publisher_description (str | Unset):
        publication_type (str | Unset):
        format_ (str | Unset):
        status (str | Unset):
        original_language (str | Unset):
        cached_issues_count (int | Unset):
        average_rating (float | Unset):
        total_reviews (int | Unset):
        issues_average_rating (float | Unset):
        issues_rated_count (int | Unset):
        content_rating_label (str | Unset):
        min_age (int | Unset):
        is_nsfw (bool | Unset):
        cached_creators_count (int | Unset):
        cached_characters_count (int | Unset):
        cached_teams_count (int | Unset):
        lists_count (int | Unset):
        title (GetSeriesDetailsResponse200DataTitle | Unset):
        publisher (GetSeriesDetailsResponse200DataPublisher | Unset):
        publishers (list[GetSeriesDetailsResponse200DataPublishersItem] | Unset):
        genres (list[GetSeriesDetailsResponse200DataGenresItem] | Unset):
        imprint (None | str | Unset):
        effective_imprint (None | str | Unset):
        last_edited_by (GetSeriesDetailsResponse200DataLastEditedBy | Unset):
        creators (list[GetSeriesDetailsResponse200DataCreatorsItem] | Unset):
        characters (list[GetSeriesDetailsResponse200DataCharactersItem] | Unset):
        teams (list[GetSeriesDetailsResponse200DataTeamsItem] | Unset):
        foc_issues (list[GetSeriesDetailsResponse200DataFocIssuesItem] | Unset):
        upcoming_issues (list[GetSeriesDetailsResponse200DataUpcomingIssuesItem] | Unset):
    """

    id: int | Unset = UNSET
    title_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    number: int | Unset = UNSET
    start_year: int | Unset = UNSET
    end_year: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    publisher_description: str | Unset = UNSET
    publication_type: str | Unset = UNSET
    format_: str | Unset = UNSET
    status: str | Unset = UNSET
    original_language: str | Unset = UNSET
    cached_issues_count: int | Unset = UNSET
    average_rating: float | Unset = UNSET
    total_reviews: int | Unset = UNSET
    issues_average_rating: float | Unset = UNSET
    issues_rated_count: int | Unset = UNSET
    content_rating_label: str | Unset = UNSET
    min_age: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    cached_creators_count: int | Unset = UNSET
    cached_characters_count: int | Unset = UNSET
    cached_teams_count: int | Unset = UNSET
    lists_count: int | Unset = UNSET
    title: GetSeriesDetailsResponse200DataTitle | Unset = UNSET
    publisher: GetSeriesDetailsResponse200DataPublisher | Unset = UNSET
    publishers: list[GetSeriesDetailsResponse200DataPublishersItem] | Unset = UNSET
    genres: list[GetSeriesDetailsResponse200DataGenresItem] | Unset = UNSET
    imprint: None | str | Unset = UNSET
    effective_imprint: None | str | Unset = UNSET
    last_edited_by: GetSeriesDetailsResponse200DataLastEditedBy | Unset = UNSET
    creators: list[GetSeriesDetailsResponse200DataCreatorsItem] | Unset = UNSET
    characters: list[GetSeriesDetailsResponse200DataCharactersItem] | Unset = UNSET
    teams: list[GetSeriesDetailsResponse200DataTeamsItem] | Unset = UNSET
    foc_issues: list[GetSeriesDetailsResponse200DataFocIssuesItem] | Unset = UNSET
    upcoming_issues: list[GetSeriesDetailsResponse200DataUpcomingIssuesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title_id = self.title_id

        name = self.name

        slug = self.slug

        number = self.number

        start_year = self.start_year

        end_year = self.end_year

        cover_url = self.cover_url

        publisher_description = self.publisher_description

        publication_type = self.publication_type

        format_ = self.format_

        status = self.status

        original_language = self.original_language

        cached_issues_count = self.cached_issues_count

        average_rating = self.average_rating

        total_reviews = self.total_reviews

        issues_average_rating = self.issues_average_rating

        issues_rated_count = self.issues_rated_count

        content_rating_label = self.content_rating_label

        min_age = self.min_age

        is_nsfw = self.is_nsfw

        cached_creators_count = self.cached_creators_count

        cached_characters_count = self.cached_characters_count

        cached_teams_count = self.cached_teams_count

        lists_count = self.lists_count

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        publishers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publishers, Unset):
            publishers = []
            for publishers_item_data in self.publishers:
                publishers_item = publishers_item_data.to_dict()
                publishers.append(publishers_item)

        genres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = []
            for genres_item_data in self.genres:
                genres_item = genres_item_data.to_dict()
                genres.append(genres_item)

        imprint: None | str | Unset
        if isinstance(self.imprint, Unset):
            imprint = UNSET
        else:
            imprint = self.imprint

        effective_imprint: None | str | Unset
        if isinstance(self.effective_imprint, Unset):
            effective_imprint = UNSET
        else:
            effective_imprint = self.effective_imprint

        last_edited_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_edited_by, Unset):
            last_edited_by = self.last_edited_by.to_dict()

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

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

        foc_issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.foc_issues, Unset):
            foc_issues = []
            for foc_issues_item_data in self.foc_issues:
                foc_issues_item = foc_issues_item_data.to_dict()
                foc_issues.append(foc_issues_item)

        upcoming_issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.upcoming_issues, Unset):
            upcoming_issues = []
            for upcoming_issues_item_data in self.upcoming_issues:
                upcoming_issues_item = upcoming_issues_item_data.to_dict()
                upcoming_issues.append(upcoming_issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title_id is not UNSET:
            field_dict["title_id"] = title_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if number is not UNSET:
            field_dict["number"] = number
        if start_year is not UNSET:
            field_dict["start_year"] = start_year
        if end_year is not UNSET:
            field_dict["end_year"] = end_year
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if publisher_description is not UNSET:
            field_dict["publisher_description"] = publisher_description
        if publication_type is not UNSET:
            field_dict["publication_type"] = publication_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if status is not UNSET:
            field_dict["status"] = status
        if original_language is not UNSET:
            field_dict["original_language"] = original_language
        if cached_issues_count is not UNSET:
            field_dict["cached_issues_count"] = cached_issues_count
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if total_reviews is not UNSET:
            field_dict["total_reviews"] = total_reviews
        if issues_average_rating is not UNSET:
            field_dict["issues_average_rating"] = issues_average_rating
        if issues_rated_count is not UNSET:
            field_dict["issues_rated_count"] = issues_rated_count
        if content_rating_label is not UNSET:
            field_dict["content_rating_label"] = content_rating_label
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if cached_creators_count is not UNSET:
            field_dict["cached_creators_count"] = cached_creators_count
        if cached_characters_count is not UNSET:
            field_dict["cached_characters_count"] = cached_characters_count
        if cached_teams_count is not UNSET:
            field_dict["cached_teams_count"] = cached_teams_count
        if lists_count is not UNSET:
            field_dict["lists_count"] = lists_count
        if title is not UNSET:
            field_dict["title"] = title
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if publishers is not UNSET:
            field_dict["publishers"] = publishers
        if genres is not UNSET:
            field_dict["genres"] = genres
        if imprint is not UNSET:
            field_dict["imprint"] = imprint
        if effective_imprint is not UNSET:
            field_dict["effective_imprint"] = effective_imprint
        if last_edited_by is not UNSET:
            field_dict["last_edited_by"] = last_edited_by
        if creators is not UNSET:
            field_dict["creators"] = creators
        if characters is not UNSET:
            field_dict["characters"] = characters
        if teams is not UNSET:
            field_dict["teams"] = teams
        if foc_issues is not UNSET:
            field_dict["foc_issues"] = foc_issues
        if upcoming_issues is not UNSET:
            field_dict["upcoming_issues"] = upcoming_issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_details_response_200_data_characters_item import (
            GetSeriesDetailsResponse200DataCharactersItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_creators_item import (
            GetSeriesDetailsResponse200DataCreatorsItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_foc_issues_item import (
            GetSeriesDetailsResponse200DataFocIssuesItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_genres_item import GetSeriesDetailsResponse200DataGenresItem  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_last_edited_by import (
            GetSeriesDetailsResponse200DataLastEditedBy,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_publisher import GetSeriesDetailsResponse200DataPublisher  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_publishers_item import (
            GetSeriesDetailsResponse200DataPublishersItem,  # noqa: PLC0415
        )
        from ..models.get_series_details_response_200_data_teams_item import GetSeriesDetailsResponse200DataTeamsItem  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_title import GetSeriesDetailsResponse200DataTitle  # noqa: PLC0415
        from ..models.get_series_details_response_200_data_upcoming_issues_item import (
            GetSeriesDetailsResponse200DataUpcomingIssuesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title_id = d.pop("title_id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        number = d.pop("number", UNSET)

        start_year = d.pop("start_year", UNSET)

        end_year = d.pop("end_year", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        publisher_description = d.pop("publisher_description", UNSET)

        publication_type = d.pop("publication_type", UNSET)

        format_ = d.pop("format", UNSET)

        status = d.pop("status", UNSET)

        original_language = d.pop("original_language", UNSET)

        cached_issues_count = d.pop("cached_issues_count", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        total_reviews = d.pop("total_reviews", UNSET)

        issues_average_rating = d.pop("issues_average_rating", UNSET)

        issues_rated_count = d.pop("issues_rated_count", UNSET)

        content_rating_label = d.pop("content_rating_label", UNSET)

        min_age = d.pop("min_age", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        cached_creators_count = d.pop("cached_creators_count", UNSET)

        cached_characters_count = d.pop("cached_characters_count", UNSET)

        cached_teams_count = d.pop("cached_teams_count", UNSET)

        lists_count = d.pop("lists_count", UNSET)

        _title = d.pop("title", UNSET)
        title: GetSeriesDetailsResponse200DataTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = GetSeriesDetailsResponse200DataTitle.from_dict(_title)

        _publisher = d.pop("publisher", UNSET)
        publisher: GetSeriesDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetSeriesDetailsResponse200DataPublisher.from_dict(_publisher)

        _publishers = d.pop("publishers", UNSET)
        publishers: list[GetSeriesDetailsResponse200DataPublishersItem] | Unset = UNSET
        if _publishers is not UNSET:
            publishers = []
            for publishers_item_data in _publishers:
                publishers_item = GetSeriesDetailsResponse200DataPublishersItem.from_dict(publishers_item_data)

                publishers.append(publishers_item)

        _genres = d.pop("genres", UNSET)
        genres: list[GetSeriesDetailsResponse200DataGenresItem] | Unset = UNSET
        if _genres is not UNSET:
            genres = []
            for genres_item_data in _genres:
                genres_item = GetSeriesDetailsResponse200DataGenresItem.from_dict(genres_item_data)

                genres.append(genres_item)

        def _parse_imprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imprint = _parse_imprint(d.pop("imprint", UNSET))

        def _parse_effective_imprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_imprint = _parse_effective_imprint(d.pop("effective_imprint", UNSET))

        _last_edited_by = d.pop("last_edited_by", UNSET)
        last_edited_by: GetSeriesDetailsResponse200DataLastEditedBy | Unset
        if isinstance(_last_edited_by, Unset):
            last_edited_by = UNSET
        else:
            last_edited_by = GetSeriesDetailsResponse200DataLastEditedBy.from_dict(_last_edited_by)

        _creators = d.pop("creators", UNSET)
        creators: list[GetSeriesDetailsResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetSeriesDetailsResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

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

        _foc_issues = d.pop("foc_issues", UNSET)
        foc_issues: list[GetSeriesDetailsResponse200DataFocIssuesItem] | Unset = UNSET
        if _foc_issues is not UNSET:
            foc_issues = []
            for foc_issues_item_data in _foc_issues:
                foc_issues_item = GetSeriesDetailsResponse200DataFocIssuesItem.from_dict(foc_issues_item_data)

                foc_issues.append(foc_issues_item)

        _upcoming_issues = d.pop("upcoming_issues", UNSET)
        upcoming_issues: list[GetSeriesDetailsResponse200DataUpcomingIssuesItem] | Unset = UNSET
        if _upcoming_issues is not UNSET:
            upcoming_issues = []
            for upcoming_issues_item_data in _upcoming_issues:
                upcoming_issues_item = GetSeriesDetailsResponse200DataUpcomingIssuesItem.from_dict(
                    upcoming_issues_item_data
                )

                upcoming_issues.append(upcoming_issues_item)

        get_series_details_response_200_data = cls(
            id=id,
            title_id=title_id,
            name=name,
            slug=slug,
            number=number,
            start_year=start_year,
            end_year=end_year,
            cover_url=cover_url,
            publisher_description=publisher_description,
            publication_type=publication_type,
            format_=format_,
            status=status,
            original_language=original_language,
            cached_issues_count=cached_issues_count,
            average_rating=average_rating,
            total_reviews=total_reviews,
            issues_average_rating=issues_average_rating,
            issues_rated_count=issues_rated_count,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            cached_creators_count=cached_creators_count,
            cached_characters_count=cached_characters_count,
            cached_teams_count=cached_teams_count,
            lists_count=lists_count,
            title=title,
            publisher=publisher,
            publishers=publishers,
            genres=genres,
            imprint=imprint,
            effective_imprint=effective_imprint,
            last_edited_by=last_edited_by,
            creators=creators,
            characters=characters,
            teams=teams,
            foc_issues=foc_issues,
            upcoming_issues=upcoming_issues,
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
