from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200DataProgress")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200DataProgress:
    """
    Attributes:
        year (int):
        target (int | None):
        read_count (int):
        percent (float | None):
        completed (bool):
        expected_reads (int | None):
        pace_difference (int | None):
        remaining (int | None):
        reads_per_week (int | None):
        editable (bool):
        last_year_reads (int | None):
        suggested_target (int | None):
        timezone (str):
        is_public (bool):
        share_url (None | str):
        notify_milestones (bool | Unset): Left out for a `read:showcase` token.
        notify_lapses (bool | Unset): Left out for a `read:showcase` token.
        email_updates (bool | Unset): Left out for a `read:showcase` token.
    """

    year: int
    target: int | None
    read_count: int
    percent: float | None
    completed: bool
    expected_reads: int | None
    pace_difference: int | None
    remaining: int | None
    reads_per_week: int | None
    editable: bool
    last_year_reads: int | None
    suggested_target: int | None
    timezone: str
    is_public: bool
    share_url: None | str
    notify_milestones: bool | Unset = UNSET
    notify_lapses: bool | Unset = UNSET
    email_updates: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        target: int | None
        target = self.target

        read_count = self.read_count

        percent: float | None
        percent = self.percent

        completed = self.completed

        expected_reads: int | None
        expected_reads = self.expected_reads

        pace_difference: int | None
        pace_difference = self.pace_difference

        remaining: int | None
        remaining = self.remaining

        reads_per_week: int | None
        reads_per_week = self.reads_per_week

        editable = self.editable

        last_year_reads: int | None
        last_year_reads = self.last_year_reads

        suggested_target: int | None
        suggested_target = self.suggested_target

        timezone = self.timezone

        is_public = self.is_public

        share_url: None | str
        share_url = self.share_url

        notify_milestones = self.notify_milestones

        notify_lapses = self.notify_lapses

        email_updates = self.email_updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "target": target,
                "read_count": read_count,
                "percent": percent,
                "completed": completed,
                "expected_reads": expected_reads,
                "pace_difference": pace_difference,
                "remaining": remaining,
                "reads_per_week": reads_per_week,
                "editable": editable,
                "last_year_reads": last_year_reads,
                "suggested_target": suggested_target,
                "timezone": timezone,
                "is_public": is_public,
                "share_url": share_url,
            }
        )
        if notify_milestones is not UNSET:
            field_dict["notify_milestones"] = notify_milestones
        if notify_lapses is not UNSET:
            field_dict["notify_lapses"] = notify_lapses
        if email_updates is not UNSET:
            field_dict["email_updates"] = email_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        def _parse_target(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        target = _parse_target(d.pop("target"))

        read_count = d.pop("read_count")

        def _parse_percent(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percent = _parse_percent(d.pop("percent"))

        completed = d.pop("completed")

        def _parse_expected_reads(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        expected_reads = _parse_expected_reads(d.pop("expected_reads"))

        def _parse_pace_difference(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pace_difference = _parse_pace_difference(d.pop("pace_difference"))

        def _parse_remaining(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining = _parse_remaining(d.pop("remaining"))

        def _parse_reads_per_week(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        reads_per_week = _parse_reads_per_week(d.pop("reads_per_week"))

        editable = d.pop("editable")

        def _parse_last_year_reads(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_year_reads = _parse_last_year_reads(d.pop("last_year_reads"))

        def _parse_suggested_target(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        suggested_target = _parse_suggested_target(d.pop("suggested_target"))

        timezone = d.pop("timezone")

        is_public = d.pop("is_public")

        def _parse_share_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        share_url = _parse_share_url(d.pop("share_url"))

        notify_milestones = d.pop("notify_milestones", UNSET)

        notify_lapses = d.pop("notify_lapses", UNSET)

        email_updates = d.pop("email_updates", UNSET)

        view_yearly_reading_statistics_response_200_data_progress = cls(
            year=year,
            target=target,
            read_count=read_count,
            percent=percent,
            completed=completed,
            expected_reads=expected_reads,
            pace_difference=pace_difference,
            remaining=remaining,
            reads_per_week=reads_per_week,
            editable=editable,
            last_year_reads=last_year_reads,
            suggested_target=suggested_target,
            timezone=timezone,
            is_public=is_public,
            share_url=share_url,
            notify_milestones=notify_milestones,
            notify_lapses=notify_lapses,
            email_updates=email_updates,
        )

        view_yearly_reading_statistics_response_200_data_progress.additional_properties = d
        return view_yearly_reading_statistics_response_200_data_progress

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
