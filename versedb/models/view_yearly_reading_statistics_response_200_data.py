from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_yearly_reading_statistics_response_200_data_breakdowns import (
        ViewYearlyReadingStatisticsResponse200DataBreakdowns,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_days_item import (
        ViewYearlyReadingStatisticsResponse200DataDaysItem,
    )
    from ..models.view_yearly_reading_statistics_response_200_data_finished_series_item import (
        ViewYearlyReadingStatisticsResponse200DataFinishedSeriesItem,
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
        progress (ViewYearlyReadingStatisticsResponse200DataProgress):
        days (list[ViewYearlyReadingStatisticsResponse200DataDaysItem]):
        months (ViewYearlyReadingStatisticsResponse200DataMonths): Reads in each month, keyed 1 to 12.
        breakdowns (ViewYearlyReadingStatisticsResponse200DataBreakdowns):
        active_days (int):
        longest_streak (int):
        current_streak (int):
        projected_reads (int):
        projected_finish (None | str):
        this_week (int):
        this_month (int):
        monthly_target (int | None):
        busiest_month (int | None):
        finished_series (list[ViewYearlyReadingStatisticsResponse200DataFinishedSeriesItem]):
    """

    progress: ViewYearlyReadingStatisticsResponse200DataProgress
    days: list[ViewYearlyReadingStatisticsResponse200DataDaysItem]
    months: ViewYearlyReadingStatisticsResponse200DataMonths
    breakdowns: ViewYearlyReadingStatisticsResponse200DataBreakdowns
    active_days: int
    longest_streak: int
    current_streak: int
    projected_reads: int
    projected_finish: None | str
    this_week: int
    this_month: int
    monthly_target: int | None
    busiest_month: int | None
    finished_series: list[ViewYearlyReadingStatisticsResponse200DataFinishedSeriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress = self.progress.to_dict()

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        months = self.months.to_dict()

        breakdowns = self.breakdowns.to_dict()

        active_days = self.active_days

        longest_streak = self.longest_streak

        current_streak = self.current_streak

        projected_reads = self.projected_reads

        projected_finish: None | str
        projected_finish = self.projected_finish

        this_week = self.this_week

        this_month = self.this_month

        monthly_target: int | None
        monthly_target = self.monthly_target

        busiest_month: int | None
        busiest_month = self.busiest_month

        finished_series = []
        for finished_series_item_data in self.finished_series:
            finished_series_item = finished_series_item_data.to_dict()
            finished_series.append(finished_series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "progress": progress,
                "days": days,
                "months": months,
                "breakdowns": breakdowns,
                "active_days": active_days,
                "longest_streak": longest_streak,
                "current_streak": current_streak,
                "projected_reads": projected_reads,
                "projected_finish": projected_finish,
                "this_week": this_week,
                "this_month": this_month,
                "monthly_target": monthly_target,
                "busiest_month": busiest_month,
                "finished_series": finished_series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_yearly_reading_statistics_response_200_data_breakdowns import (
            ViewYearlyReadingStatisticsResponse200DataBreakdowns,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_days_item import (
            ViewYearlyReadingStatisticsResponse200DataDaysItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_finished_series_item import (
            ViewYearlyReadingStatisticsResponse200DataFinishedSeriesItem,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_months import (
            ViewYearlyReadingStatisticsResponse200DataMonths,  # noqa: PLC0415
        )
        from ..models.view_yearly_reading_statistics_response_200_data_progress import (
            ViewYearlyReadingStatisticsResponse200DataProgress,  # noqa: PLC0415
        )

        d = dict(src_dict)
        progress = ViewYearlyReadingStatisticsResponse200DataProgress.from_dict(d.pop("progress"))

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = ViewYearlyReadingStatisticsResponse200DataDaysItem.from_dict(days_item_data)

            days.append(days_item)

        months = ViewYearlyReadingStatisticsResponse200DataMonths.from_dict(d.pop("months"))

        breakdowns = ViewYearlyReadingStatisticsResponse200DataBreakdowns.from_dict(d.pop("breakdowns"))

        active_days = d.pop("active_days")

        longest_streak = d.pop("longest_streak")

        current_streak = d.pop("current_streak")

        projected_reads = d.pop("projected_reads")

        def _parse_projected_finish(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        projected_finish = _parse_projected_finish(d.pop("projected_finish"))

        this_week = d.pop("this_week")

        this_month = d.pop("this_month")

        def _parse_monthly_target(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monthly_target = _parse_monthly_target(d.pop("monthly_target"))

        def _parse_busiest_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        busiest_month = _parse_busiest_month(d.pop("busiest_month"))

        finished_series = []
        _finished_series = d.pop("finished_series")
        for finished_series_item_data in _finished_series:
            finished_series_item = ViewYearlyReadingStatisticsResponse200DataFinishedSeriesItem.from_dict(
                finished_series_item_data
            )

            finished_series.append(finished_series_item)

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
