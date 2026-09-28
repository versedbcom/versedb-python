from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddToPullListResponse422Errors")


@_attrs_define
class AddToPullListResponse422Errors:
    """
    Attributes:
        series_id (list[str] | Unset):
    """

    series_id: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_id: list[str] | Unset = UNSET
        if not isinstance(self.series_id, Unset):
            series_id = self.series_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series_id is not UNSET:
            field_dict["series_id"] = series_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_id = cast(list[str], d.pop("series_id", UNSET))

        add_to_pull_list_response_422_errors = cls(
            series_id=series_id,
        )

        add_to_pull_list_response_422_errors.additional_properties = d
        return add_to_pull_list_response_422_errors

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
