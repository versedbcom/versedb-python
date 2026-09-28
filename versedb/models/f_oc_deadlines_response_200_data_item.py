from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.f_oc_deadlines_response_200_data_item_series import FOcDeadlinesResponse200DataItemSeries


T = TypeVar("T", bound="FOcDeadlinesResponse200DataItem")


@_attrs_define
class FOcDeadlinesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        number (str | Unset):
        title (str | Unset):
        cover_url (str | Unset):
        release_date (str | Unset):
        foc_date (str | Unset):
        series (FOcDeadlinesResponse200DataItemSeries | Unset):
    """

    id: int | Unset = UNSET
    number: str | Unset = UNSET
    title: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    release_date: str | Unset = UNSET
    foc_date: str | Unset = UNSET
    series: FOcDeadlinesResponse200DataItemSeries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        title = self.title

        cover_url = self.cover_url

        release_date = self.release_date

        foc_date = self.foc_date

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if foc_date is not UNSET:
            field_dict["foc_date"] = foc_date
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.f_oc_deadlines_response_200_data_item_series import (
            FOcDeadlinesResponse200DataItemSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        number = d.pop("number", UNSET)

        title = d.pop("title", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        release_date = d.pop("release_date", UNSET)

        foc_date = d.pop("foc_date", UNSET)

        _series = d.pop("series", UNSET)
        series: FOcDeadlinesResponse200DataItemSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = FOcDeadlinesResponse200DataItemSeries.from_dict(_series)

        f_oc_deadlines_response_200_data_item = cls(
            id=id,
            number=number,
            title=title,
            cover_url=cover_url,
            release_date=release_date,
            foc_date=foc_date,
            series=series,
        )

        f_oc_deadlines_response_200_data_item.additional_properties = d
        return f_oc_deadlines_response_200_data_item

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
