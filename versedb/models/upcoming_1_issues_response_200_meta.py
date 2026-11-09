from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Upcoming1IssuesResponse200Meta")


@_attrs_define
class Upcoming1IssuesResponse200Meta:
    """
    Attributes:
        current_page (int):
        per_page (int):
        total (int):
        last_page (int):
        lookahead_days (int):
        window_start (str):
        window_end (str):
    """

    current_page: int
    per_page: int
    total: int
    last_page: int
    lookahead_days: int
    window_start: str
    window_end: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        per_page = self.per_page

        total = self.total

        last_page = self.last_page

        lookahead_days = self.lookahead_days

        window_start = self.window_start

        window_end = self.window_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "per_page": per_page,
                "total": total,
                "last_page": last_page,
                "lookahead_days": lookahead_days,
                "window_start": window_start,
                "window_end": window_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        last_page = d.pop("last_page")

        lookahead_days = d.pop("lookahead_days")

        window_start = d.pop("window_start")

        window_end = d.pop("window_end")

        upcoming_1_issues_response_200_meta = cls(
            current_page=current_page,
            per_page=per_page,
            total=total,
            last_page=last_page,
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
