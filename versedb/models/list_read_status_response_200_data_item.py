from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_read_status_response_200_data_item_issue import ListReadStatusResponse200DataItemIssue
    from ..models.list_read_status_response_200_data_item_series import ListReadStatusResponse200DataItemSeries


T = TypeVar("T", bound="ListReadStatusResponse200DataItem")


@_attrs_define
class ListReadStatusResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        issue (ListReadStatusResponse200DataItemIssue | Unset):
        series (ListReadStatusResponse200DataItemSeries | Unset):
        variant_id (None | str | Unset):
        read_at (str | Unset):
    """

    id: int | Unset = UNSET
    issue: ListReadStatusResponse200DataItemIssue | Unset = UNSET
    series: ListReadStatusResponse200DataItemSeries | Unset = UNSET
    variant_id: None | str | Unset = UNSET
    read_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        read_at = self.read_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issue is not UNSET:
            field_dict["issue"] = issue
        if series is not UNSET:
            field_dict["series"] = series
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if read_at is not UNSET:
            field_dict["read_at"] = read_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_read_status_response_200_data_item_issue import ListReadStatusResponse200DataItemIssue  # noqa: PLC0415
        from ..models.list_read_status_response_200_data_item_series import ListReadStatusResponse200DataItemSeries  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: ListReadStatusResponse200DataItemIssue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = ListReadStatusResponse200DataItemIssue.from_dict(_issue)

        _series = d.pop("series", UNSET)
        series: ListReadStatusResponse200DataItemSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = ListReadStatusResponse200DataItemSeries.from_dict(_series)

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        read_at = d.pop("read_at", UNSET)

        list_read_status_response_200_data_item = cls(
            id=id,
            issue=issue,
            series=series,
            variant_id=variant_id,
            read_at=read_at,
        )

        list_read_status_response_200_data_item.additional_properties = d
        return list_read_status_response_200_data_item

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
