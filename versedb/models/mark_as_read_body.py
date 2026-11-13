from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkAsReadBody")


@_attrs_define
class MarkAsReadBody:
    """
    Attributes:
        read_at (str | Unset): The day it was read, YYYY-MM-DD, not in the future (optional). Leave it out when the date
            is unknown.
        variant_id (int | None | Unset): Specific variant ID (optional).
    """

    read_at: str | Unset = UNSET
    variant_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        read_at = d.pop("read_at", UNSET)

        def _parse_variant_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        mark_as_read_body = cls(
            read_at=read_at,
            variant_id=variant_id,
        )

        mark_as_read_body.additional_properties = d
        return mark_as_read_body

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
