from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorDetailsResponse200DataLinksType0Item")


@_attrs_define
class GetCreatorDetailsResponse200DataLinksType0Item:
    """
    Attributes:
        url (str):
        type_ (str | Unset):
        label (str | Unset):
    """

    url: str
    type_: str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        type_ = self.type_

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        get_creator_details_response_200_data_links_type_0_item = cls(
            url=url,
            type_=type_,
            label=label,
        )

        get_creator_details_response_200_data_links_type_0_item.additional_properties = d
        return get_creator_details_response_200_data_links_type_0_item

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
