from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_characters_item import (
        ViewYearlyReadingStatisticsResponse200DataBreakdownsCharactersItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_creators_item import (
        ViewYearlyReadingStatisticsResponse200DataBreakdownsCreatorsItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_genres_item import (
        ViewYearlyReadingStatisticsResponse200DataBreakdownsGenresItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_publishers_item import (
        ViewYearlyReadingStatisticsResponse200DataBreakdownsPublishersItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_series_item import (
        ViewYearlyReadingStatisticsResponse200DataBreakdownsSeriesItem,
    )


T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200DataBreakdowns")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200DataBreakdowns:
    """
    Attributes:
        series (list[ViewYearlyReadingStatisticsResponse200DataBreakdownsSeriesItem]):
        publishers (list[ViewYearlyReadingStatisticsResponse200DataBreakdownsPublishersItem]):
        creators (list[ViewYearlyReadingStatisticsResponse200DataBreakdownsCreatorsItem]):
        genres (list[ViewYearlyReadingStatisticsResponse200DataBreakdownsGenresItem]):
        characters (list[ViewYearlyReadingStatisticsResponse200DataBreakdownsCharactersItem]):
    """

    series: list[ViewYearlyReadingStatisticsResponse200DataBreakdownsSeriesItem]
    publishers: list[ViewYearlyReadingStatisticsResponse200DataBreakdownsPublishersItem]
    creators: list[ViewYearlyReadingStatisticsResponse200DataBreakdownsCreatorsItem]
    genres: list[ViewYearlyReadingStatisticsResponse200DataBreakdownsGenresItem]
    characters: list[ViewYearlyReadingStatisticsResponse200DataBreakdownsCharactersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        publishers = []
        for publishers_item_data in self.publishers:
            publishers_item = publishers_item_data.to_dict()
            publishers.append(publishers_item)

        creators = []
        for creators_item_data in self.creators:
            creators_item = creators_item_data.to_dict()
            creators.append(creators_item)

        genres = []
        for genres_item_data in self.genres:
            genres_item = genres_item_data.to_dict()
            genres.append(genres_item)

        characters = []
        for characters_item_data in self.characters:
            characters_item = characters_item_data.to_dict()
            characters.append(characters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series": series,
                "publishers": publishers,
                "creators": creators,
                "genres": genres,
                "characters": characters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_characters_item import (
            ViewYearlyReadingStatisticsResponse200DataBreakdownsCharactersItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_creators_item import (
            ViewYearlyReadingStatisticsResponse200DataBreakdownsCreatorsItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_genres_item import (
            ViewYearlyReadingStatisticsResponse200DataBreakdownsGenresItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_publishers_item import (
            ViewYearlyReadingStatisticsResponse200DataBreakdownsPublishersItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns_series_item import (
            ViewYearlyReadingStatisticsResponse200DataBreakdownsSeriesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ViewYearlyReadingStatisticsResponse200DataBreakdownsSeriesItem.from_dict(series_item_data)

            series.append(series_item)

        publishers = []
        _publishers = d.pop("publishers")
        for publishers_item_data in _publishers:
            publishers_item = ViewYearlyReadingStatisticsResponse200DataBreakdownsPublishersItem.from_dict(
                publishers_item_data
            )

            publishers.append(publishers_item)

        creators = []
        _creators = d.pop("creators")
        for creators_item_data in _creators:
            creators_item = ViewYearlyReadingStatisticsResponse200DataBreakdownsCreatorsItem.from_dict(
                creators_item_data
            )

            creators.append(creators_item)

        genres = []
        _genres = d.pop("genres")
        for genres_item_data in _genres:
            genres_item = ViewYearlyReadingStatisticsResponse200DataBreakdownsGenresItem.from_dict(genres_item_data)

            genres.append(genres_item)

        characters = []
        _characters = d.pop("characters")
        for characters_item_data in _characters:
            characters_item = ViewYearlyReadingStatisticsResponse200DataBreakdownsCharactersItem.from_dict(
                characters_item_data
            )

            characters.append(characters_item)

        view_yearly_reading_statistics_response_200_data_breakdowns = cls(
            series=series,
            publishers=publishers,
            creators=creators,
            genres=genres,
            characters=characters,
        )

        view_yearly_reading_statistics_response_200_data_breakdowns.additional_properties = d
        return view_yearly_reading_statistics_response_200_data_breakdowns

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
