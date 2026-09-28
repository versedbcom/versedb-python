from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAComicShopResponse200DataOperatingHours")


@_attrs_define
class GetAComicShopResponse200DataOperatingHours:
    """
    Attributes:
        monday (str | Unset):
        saturday (str | Unset):
        sunday (str | Unset):
    """

    monday: str | Unset = UNSET
    saturday: str | Unset = UNSET
    sunday: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday = self.monday

        saturday = self.saturday

        sunday = self.sunday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monday = d.pop("monday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        get_a_comic_shop_response_200_data_operating_hours = cls(
            monday=monday,
            saturday=saturday,
            sunday=sunday,
        )

        get_a_comic_shop_response_200_data_operating_hours.additional_properties = d
        return get_a_comic_shop_response_200_data_operating_hours

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
