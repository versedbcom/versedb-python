from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAComicShopResponse200DataSpecialHoursItem")


@_attrs_define
class GetAComicShopResponse200DataSpecialHoursItem:
    """
    Attributes:
        from_ (str):
        to (str):
        hours (str):
        note (None | str):
    """

    from_: str
    to: str
    hours: str
    note: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        hours = self.hours

        note: None | str
        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "hours": hours,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        hours = d.pop("hours")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

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
