from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAComicShopResponse200DataOperatingHoursType0")


@_attrs_define
class GetAComicShopResponse200DataOperatingHoursType0:
    """
    Attributes:
        monday (str | Unset):
        tuesday (str | Unset):
        wednesday (str | Unset):
        thursday (str | Unset):
        friday (str | Unset):
        saturday (str | Unset):
        sunday (str | Unset):
    """

    monday: str | Unset = UNSET
    tuesday: str | Unset = UNSET
    wednesday: str | Unset = UNSET
    thursday: str | Unset = UNSET
    friday: str | Unset = UNSET
    saturday: str | Unset = UNSET
    sunday: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday = self.monday

        tuesday = self.tuesday

        wednesday = self.wednesday

        thursday = self.thursday

        friday = self.friday

        saturday = self.saturday

        sunday = self.sunday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        get_a_comic_shop_response_200_data_operating_hours_type_0 = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        get_a_comic_shop_response_200_data_operating_hours_type_0.additional_properties = d
        return get_a_comic_shop_response_200_data_operating_hours_type_0

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
