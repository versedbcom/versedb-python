from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorDetailsResponse200DataLinks")


@_attrs_define
class GetCreatorDetailsResponse200DataLinks:
    """
    Attributes:
        website (str | Unset):
        twitter (str | Unset):
    """

    website: str | Unset = UNSET
    twitter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website = self.website

        twitter = self.twitter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if website is not UNSET:
            field_dict["website"] = website
        if twitter is not UNSET:
            field_dict["twitter"] = twitter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = d.pop("website", UNSET)

        twitter = d.pop("twitter", UNSET)

        get_creator_details_response_200_data_links = cls(
            website=website,
            twitter=twitter,
        )

        get_creator_details_response_200_data_links.additional_properties = d
        return get_creator_details_response_200_data_links

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
