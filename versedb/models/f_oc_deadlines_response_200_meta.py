from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FOcDeadlinesResponse200Meta")


@_attrs_define
class FOcDeadlinesResponse200Meta:
    """
    Attributes:
        current_page (int | Unset):
        last_page (int | Unset):
        per_page (int | Unset):
        total (int | Unset):
        foc_window_days (int | Unset):
        foc_start (str | Unset):
        foc_end (str | Unset):
        note (str | Unset):
    """

    current_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    per_page: int | Unset = UNSET
    total: int | Unset = UNSET
    foc_window_days: int | Unset = UNSET
    foc_start: str | Unset = UNSET
    foc_end: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        total = self.total

        foc_window_days = self.foc_window_days

        foc_start = self.foc_start

        foc_end = self.foc_end

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if total is not UNSET:
            field_dict["total"] = total
        if foc_window_days is not UNSET:
            field_dict["foc_window_days"] = foc_window_days
        if foc_start is not UNSET:
            field_dict["foc_start"] = foc_start
        if foc_end is not UNSET:
            field_dict["foc_end"] = foc_end
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        per_page = d.pop("per_page", UNSET)

        total = d.pop("total", UNSET)

        foc_window_days = d.pop("foc_window_days", UNSET)

        foc_start = d.pop("foc_start", UNSET)

        foc_end = d.pop("foc_end", UNSET)

        note = d.pop("note", UNSET)

        f_oc_deadlines_response_200_meta = cls(
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            total=total,
            foc_window_days=foc_window_days,
            foc_start=foc_start,
            foc_end=foc_end,
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
