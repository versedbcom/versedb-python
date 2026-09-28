from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewYourReadingGoalResponse200Data")


@_attrs_define
class ViewYourReadingGoalResponse200Data:
    """
    Attributes:
        year (int | Unset):
        target (int | Unset):
        read_count (int | Unset):
        percent (int | Unset):
        completed (bool | Unset):
        expected_reads (int | Unset):
        pace_difference (int | Unset):
        remaining (int | Unset):
        reads_per_week (int | Unset):
        editable (bool | Unset):
        last_year_reads (int | Unset):
        suggested_target (int | Unset):
        timezone (str | Unset):
        is_public (bool | Unset):
        notify_milestones (bool | Unset):
        notify_lapses (bool | Unset):
        email_updates (bool | Unset):
        share_url (None | str | Unset):
    """

    year: int | Unset = UNSET
    target: int | Unset = UNSET
    read_count: int | Unset = UNSET
    percent: int | Unset = UNSET
    completed: bool | Unset = UNSET
    expected_reads: int | Unset = UNSET
    pace_difference: int | Unset = UNSET
    remaining: int | Unset = UNSET
    reads_per_week: int | Unset = UNSET
    editable: bool | Unset = UNSET
    last_year_reads: int | Unset = UNSET
    suggested_target: int | Unset = UNSET
    timezone: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    notify_milestones: bool | Unset = UNSET
    notify_lapses: bool | Unset = UNSET
    email_updates: bool | Unset = UNSET
    share_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        target = self.target

        read_count = self.read_count

        percent = self.percent

        completed = self.completed

        expected_reads = self.expected_reads

        pace_difference = self.pace_difference

        remaining = self.remaining

        reads_per_week = self.reads_per_week

        editable = self.editable

        last_year_reads = self.last_year_reads

        suggested_target = self.suggested_target

        timezone = self.timezone

        is_public = self.is_public

        notify_milestones = self.notify_milestones

        notify_lapses = self.notify_lapses

        email_updates = self.email_updates

        share_url: None | str | Unset
        if isinstance(self.share_url, Unset):
            share_url = UNSET
        else:
            share_url = self.share_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if target is not UNSET:
            field_dict["target"] = target
        if read_count is not UNSET:
            field_dict["read_count"] = read_count
        if percent is not UNSET:
            field_dict["percent"] = percent
        if completed is not UNSET:
            field_dict["completed"] = completed
        if expected_reads is not UNSET:
            field_dict["expected_reads"] = expected_reads
        if pace_difference is not UNSET:
            field_dict["pace_difference"] = pace_difference
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if reads_per_week is not UNSET:
            field_dict["reads_per_week"] = reads_per_week
        if editable is not UNSET:
            field_dict["editable"] = editable
        if last_year_reads is not UNSET:
            field_dict["last_year_reads"] = last_year_reads
        if suggested_target is not UNSET:
            field_dict["suggested_target"] = suggested_target
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if notify_milestones is not UNSET:
            field_dict["notify_milestones"] = notify_milestones
        if notify_lapses is not UNSET:
            field_dict["notify_lapses"] = notify_lapses
        if email_updates is not UNSET:
            field_dict["email_updates"] = email_updates
        if share_url is not UNSET:
            field_dict["share_url"] = share_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year", UNSET)

        target = d.pop("target", UNSET)

        read_count = d.pop("read_count", UNSET)

        percent = d.pop("percent", UNSET)

        completed = d.pop("completed", UNSET)

        expected_reads = d.pop("expected_reads", UNSET)

        pace_difference = d.pop("pace_difference", UNSET)

        remaining = d.pop("remaining", UNSET)

        reads_per_week = d.pop("reads_per_week", UNSET)

        editable = d.pop("editable", UNSET)

        last_year_reads = d.pop("last_year_reads", UNSET)

        suggested_target = d.pop("suggested_target", UNSET)

        timezone = d.pop("timezone", UNSET)

        is_public = d.pop("is_public", UNSET)

        notify_milestones = d.pop("notify_milestones", UNSET)

        notify_lapses = d.pop("notify_lapses", UNSET)

        email_updates = d.pop("email_updates", UNSET)

        def _parse_share_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_url = _parse_share_url(d.pop("share_url", UNSET))

        view_your_reading_goal_response_200_data = cls(
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
            notify_milestones=notify_milestones,
            notify_lapses=notify_lapses,
            email_updates=email_updates,
            share_url=share_url,
        )

        view_your_reading_goal_response_200_data.additional_properties = d
        return view_your_reading_goal_response_200_data

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
