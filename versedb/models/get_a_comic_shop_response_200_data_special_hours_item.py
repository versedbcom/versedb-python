from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAComicShopResponse200DataSpecialHoursItem")


@_attrs_define
class GetAComicShopResponse200DataSpecialHoursItem:
    """
    Attributes:
        from_ (str | Unset):
        to (str | Unset):
        hours (str | Unset):
        note (str | Unset):
    """

    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    hours: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        hours = self.hours

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if hours is not UNSET:
            field_dict["hours"] = hours
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        hours = d.pop("hours", UNSET)

        note = d.pop("note", UNSET)

        get_a_comic_shop_response_200_data_special_hours_item = cls(
            from_=from_,
            to=to,
            hours=hours,
            note=note,
        )

        get_a_comic_shop_response_200_data_special_hours_item.additional_properties = d
        return get_a_comic_shop_response_200_data_special_hours_item

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
