from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_pull_list_response_200_data_item_series import ListPullListResponse200DataItemSeries


T = TypeVar("T", bound="ListPullListResponse200DataItem")


@_attrs_define
class ListPullListResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        series (ListPullListResponse200DataItemSeries | Unset):
        added_at (str | Unset):
    """

    id: int | Unset = UNSET
    series: ListPullListResponse200DataItemSeries | Unset = UNSET
    added_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if series is not UNSET:
            field_dict["series"] = series
        if added_at is not UNSET:
            field_dict["added_at"] = added_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_pull_list_response_200_data_item_series import (
            ListPullListResponse200DataItemSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _series = d.pop("series", UNSET)
        series: ListPullListResponse200DataItemSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = ListPullListResponse200DataItemSeries.from_dict(_series)

        added_at = d.pop("added_at", UNSET)

        list_pull_list_response_200_data_item = cls(
            id=id,
            series=series,
            added_at=added_at,
        )

        list_pull_list_response_200_data_item.additional_properties = d
        return list_pull_list_response_200_data_item

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
