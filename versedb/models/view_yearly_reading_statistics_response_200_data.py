from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns import (
        ViewYearlyReadingStatisticsResponse200DataBreakdowns,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_days_item import (
        ViewYearlyReadingStatisticsResponse200DataDaysItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_months import (
        ViewYearlyReadingStatisticsResponse200DataMonths,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_progress import (
        ViewYearlyReadingStatisticsResponse200DataProgress,
    )


T = TypeVar("T", bound="ViewYearlyReadingStatisticsResponse200Data")


@_attrs_define
class ViewYearlyReadingStatisticsResponse200Data:
    """
    Attributes:
        progress (ViewYearlyReadingStatisticsResponse200DataProgress | Unset):
        days (list[ViewYearlyReadingStatisticsResponse200DataDaysItem] | Unset):
        months (ViewYearlyReadingStatisticsResponse200DataMonths | Unset):
        breakdowns (ViewYearlyReadingStatisticsResponse200DataBreakdowns | Unset):
        active_days (int | Unset):
        longest_streak (int | Unset):
        current_streak (int | Unset):
        projected_reads (int | Unset):
        projected_finish (None | str | Unset):
        this_week (int | Unset):
        this_month (int | Unset):
        monthly_target (int | Unset):
        busiest_month (None | str | Unset):
        finished_series (list[Any] | Unset):
    """

    progress: ViewYearlyReadingStatisticsResponse200DataProgress | Unset = UNSET
    days: list[ViewYearlyReadingStatisticsResponse200DataDaysItem] | Unset = UNSET
    months: ViewYearlyReadingStatisticsResponse200DataMonths | Unset = UNSET
    breakdowns: ViewYearlyReadingStatisticsResponse200DataBreakdowns | Unset = UNSET
    active_days: int | Unset = UNSET
    longest_streak: int | Unset = UNSET
    current_streak: int | Unset = UNSET
    projected_reads: int | Unset = UNSET
    projected_finish: None | str | Unset = UNSET
    this_week: int | Unset = UNSET
    this_month: int | Unset = UNSET
    monthly_target: int | Unset = UNSET
    busiest_month: None | str | Unset = UNSET
    finished_series: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        months: dict[str, Any] | Unset = UNSET
        if not isinstance(self.months, Unset):
            months = self.months.to_dict()

        breakdowns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = self.breakdowns.to_dict()

        active_days = self.active_days

        longest_streak = self.longest_streak

        current_streak = self.current_streak

        projected_reads = self.projected_reads

        projected_finish: None | str | Unset
        if isinstance(self.projected_finish, Unset):
            projected_finish = UNSET
        else:
            projected_finish = self.projected_finish

        this_week = self.this_week

        this_month = self.this_month

        monthly_target = self.monthly_target

        busiest_month: None | str | Unset
        if isinstance(self.busiest_month, Unset):
            busiest_month = UNSET
        else:
            busiest_month = self.busiest_month

        finished_series: list[Any] | Unset = UNSET
        if not isinstance(self.finished_series, Unset):
            finished_series = self.finished_series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if days is not UNSET:
            field_dict["days"] = days
        if months is not UNSET:
            field_dict["months"] = months
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns
        if active_days is not UNSET:
            field_dict["active_days"] = active_days
        if longest_streak is not UNSET:
            field_dict["longest_streak"] = longest_streak
        if current_streak is not UNSET:
            field_dict["current_streak"] = current_streak
        if projected_reads is not UNSET:
            field_dict["projected_reads"] = projected_reads
        if projected_finish is not UNSET:
            field_dict["projected_finish"] = projected_finish
        if this_week is not UNSET:
            field_dict["this_week"] = this_week
        if this_month is not UNSET:
            field_dict["this_month"] = this_month
        if monthly_target is not UNSET:
            field_dict["monthly_target"] = monthly_target
        if busiest_month is not UNSET:
            field_dict["busiest_month"] = busiest_month
        if finished_series is not UNSET:
            field_dict["finished_series"] = finished_series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns import (
            ViewYearlyReadingStatisticsResponse200DataBreakdowns,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_days_item import (
            ViewYearlyReadingStatisticsResponse200DataDaysItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_months import (
            ViewYearlyReadingStatisticsResponse200DataMonths,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_progress import (
            ViewYearlyReadingStatisticsResponse200DataProgress,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _progress = d.pop("progress", UNSET)
        progress: ViewYearlyReadingStatisticsResponse200DataProgress | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ViewYearlyReadingStatisticsResponse200DataProgress.from_dict(_progress)

        _days = d.pop("days", UNSET)
        days: list[ViewYearlyReadingStatisticsResponse200DataDaysItem] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = ViewYearlyReadingStatisticsResponse200DataDaysItem.from_dict(days_item_data)

                days.append(days_item)

        _months = d.pop("months", UNSET)
        months: ViewYearlyReadingStatisticsResponse200DataMonths | Unset
        if isinstance(_months, Unset):
            months = UNSET
        else:
            months = ViewYearlyReadingStatisticsResponse200DataMonths.from_dict(_months)

        _breakdowns = d.pop("breakdowns", UNSET)
        breakdowns: ViewYearlyReadingStatisticsResponse200DataBreakdowns | Unset
        if isinstance(_breakdowns, Unset):
            breakdowns = UNSET
        else:
            breakdowns = ViewYearlyReadingStatisticsResponse200DataBreakdowns.from_dict(_breakdowns)

        active_days = d.pop("active_days", UNSET)

        longest_streak = d.pop("longest_streak", UNSET)

        current_streak = d.pop("current_streak", UNSET)

        projected_reads = d.pop("projected_reads", UNSET)

        def _parse_projected_finish(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        projected_finish = _parse_projected_finish(d.pop("projected_finish", UNSET))

        this_week = d.pop("this_week", UNSET)

        this_month = d.pop("this_month", UNSET)

        monthly_target = d.pop("monthly_target", UNSET)

        def _parse_busiest_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        busiest_month = _parse_busiest_month(d.pop("busiest_month", UNSET))

        finished_series = cast(list[Any], d.pop("finished_series", UNSET))

        view_yearly_reading_statistics_response_200_data = cls(
            progress=progress,
            days=days,
            months=months,
            breakdowns=breakdowns,
            active_days=active_days,
            longest_streak=longest_streak,
            current_streak=current_streak,
            projected_reads=projected_reads,
            projected_finish=projected_finish,
            this_week=this_week,
            this_month=this_month,
            monthly_target=monthly_target,
            busiest_month=busiest_month,
            finished_series=finished_series,
        )

        view_yearly_reading_statistics_response_200_data.additional_properties = d
        return view_yearly_reading_statistics_response_200_data

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
