from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetASpecificPodcastResponse200DataSocialLinksType0")


@_attrs_define
class GetASpecificPodcastResponse200DataSocialLinksType0:
    """
    Attributes:
        website (Any | Unset):
        twitter (Any | Unset):
    """

    website: Any | Unset = UNSET
    twitter: Any | Unset = UNSET
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

        get_a_specific_podcast_response_200_data_social_links_type_0 = cls(
            website=website,
            twitter=twitter,
        )

        get_a_specific_podcast_response_200_data_social_links_type_0.additional_properties = d
        return get_a_specific_podcast_response_200_data_social_links_type_0

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
