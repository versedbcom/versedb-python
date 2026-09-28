from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditReadingDateBody")


@_attrs_define
class EditReadingDateBody:
    """
    Attributes:
        read_at (None | str | Unset): Date in YYYY-MM-DD format, must not be in the future. Pass null to mark as unread.
        variant_id (int | None | Unset): Specific variant ID (optional).
    """

    read_at: None | str | Unset = UNSET
    variant_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        else:
            read_at = self.read_at

        variant_id: int | None | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_read_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))

        def _parse_variant_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        edit_reading_date_body = cls(
            read_at=read_at,
            variant_id=variant_id,
        )

        edit_reading_date_body.additional_properties = d
        return edit_reading_date_body

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
