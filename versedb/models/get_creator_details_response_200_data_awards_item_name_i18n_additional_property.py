from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorDetailsResponse200DataAwardsItemNameI18NAdditionalProperty")


@_attrs_define
class GetCreatorDetailsResponse200DataAwardsItemNameI18NAdditionalProperty:
    """
    Attributes:
        value (str):
        source (str):
        reading (str | Unset):
        sort (str | Unset):
    """

    value: str
    source: str
    reading: str | Unset = UNSET
    sort: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        source = self.source

        reading = self.reading

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "source": source,
            }
        )
        if reading is not UNSET:
            field_dict["reading"] = reading
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        source = d.pop("source")

        reading = d.pop("reading", UNSET)

        sort = d.pop("sort", UNSET)

        get_creator_details_response_200_data_awards_item_name_i18n_additional_property = cls(
            value=value,
            source=source,
            reading=reading,
            sort=sort,
        )

        get_creator_details_response_200_data_awards_item_name_i18n_additional_property.additional_properties = d
        return get_creator_details_response_200_data_awards_item_name_i18n_additional_property

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
