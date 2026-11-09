from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FOcDeadlinesResponse200Meta")


@_attrs_define
class FOcDeadlinesResponse200Meta:
    """
    Attributes:
        current_page (int):
        per_page (int):
        total (int):
        last_page (int):
        foc_window_days (int):
        foc_start (str):
        foc_end (str):
        sort (str):
        note (str):
    """

    current_page: int
    per_page: int
    total: int
    last_page: int
    foc_window_days: int
    foc_start: str
    foc_end: str
    sort: str
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        per_page = self.per_page

        total = self.total

        last_page = self.last_page

        foc_window_days = self.foc_window_days

        foc_start = self.foc_start

        foc_end = self.foc_end

        sort = self.sort

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "per_page": per_page,
                "total": total,
                "last_page": last_page,
                "foc_window_days": foc_window_days,
                "foc_start": foc_start,
                "foc_end": foc_end,
                "sort": sort,
                "note": note,
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

        foc_window_days = d.pop("foc_window_days")

        foc_start = d.pop("foc_start")

        foc_end = d.pop("foc_end")

        sort = d.pop("sort")

        note = d.pop("note")

        f_oc_deadlines_response_200_meta = cls(
            current_page=current_page,
            per_page=per_page,
            total=total,
            last_page=last_page,
            foc_window_days=foc_window_days,
            foc_start=foc_start,
            foc_end=foc_end,
            sort=sort,
            note=note,
        )

        f_oc_deadlines_response_200_meta.additional_properties = d
        return f_oc_deadlines_response_200_meta

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
