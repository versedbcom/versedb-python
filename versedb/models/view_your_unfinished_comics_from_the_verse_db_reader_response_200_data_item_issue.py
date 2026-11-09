from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue_series import (
        ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries,
    )


T = TypeVar("T", bound="ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue")


@_attrs_define
class ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (str):
        issue_number (None | str):
        cover_url (None | str):
        is_nsfw (bool):
        release_date (None | str):
        series (ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries):
    """

    id: int
    name: None | str
    slug: str
    issue_number: None | str
    cover_url: None | str
    is_nsfw: bool
    release_date: None | str
    series: ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug = self.slug

        issue_number: None | str
        issue_number = self.issue_number

        cover_url: None | str
        cover_url = self.cover_url

        is_nsfw = self.is_nsfw

        release_date: None | str
        release_date = self.release_date

        series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "issue_number": issue_number,
                "cover_url": cover_url,
                "is_nsfw": is_nsfw,
                "release_date": release_date,
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue_series import (
            ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        slug = d.pop("slug")

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        is_nsfw = d.pop("is_nsfw")

        def _parse_release_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        release_date = _parse_release_date(d.pop("release_date"))

        series = ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries.from_dict(d.pop("series"))

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue = cls(
            id=id,
            name=name,
            slug=slug,
            issue_number=issue_number,
            cover_url=cover_url,
            is_nsfw=is_nsfw,
            release_date=release_date,
            series=series,
        )

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue.additional_properties = d
        return view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue

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
