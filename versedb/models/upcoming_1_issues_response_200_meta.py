from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Upcoming1IssuesResponse200Meta")


@_attrs_define
class Upcoming1IssuesResponse200Meta:
    """
    Attributes:
        lookahead_days (int | Unset):
        window_start (str | Unset):
        window_end (str | Unset):
    """

    lookahead_days: int | Unset = UNSET
    window_start: str | Unset = UNSET
    window_end: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookahead_days = self.lookahead_days

        window_start = self.window_start

        window_end = self.window_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookahead_days is not UNSET:
            field_dict["lookahead_days"] = lookahead_days
        if window_start is not UNSET:
            field_dict["window_start"] = window_start
        if window_end is not UNSET:
            field_dict["window_end"] = window_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lookahead_days = d.pop("lookahead_days", UNSET)

        window_start = d.pop("window_start", UNSET)

        window_end = d.pop("window_end", UNSET)

        upcoming_1_issues_response_200_meta = cls(
            lookahead_days=lookahead_days,
            window_start=window_start,
            window_end=window_end,
        )

        upcoming_1_issues_response_200_meta.additional_properties = d
        return upcoming_1_issues_response_200_meta

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
