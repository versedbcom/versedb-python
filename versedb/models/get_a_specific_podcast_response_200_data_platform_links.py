from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetASpecificPodcastResponse200DataPlatformLinks")


@_attrs_define
class GetASpecificPodcastResponse200DataPlatformLinks:
    """
    Attributes:
        apple (str | Unset):
        spotify (str | Unset):
    """

    apple: str | Unset = UNSET
    spotify: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apple = self.apple

        spotify = self.spotify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple is not UNSET:
            field_dict["apple"] = apple
        if spotify is not UNSET:
            field_dict["spotify"] = spotify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apple = d.pop("apple", UNSET)

        spotify = d.pop("spotify", UNSET)

        get_a_specific_podcast_response_200_data_platform_links = cls(
            apple=apple,
            spotify=spotify,
        )

        get_a_specific_podcast_response_200_data_platform_links.additional_properties = d
        return get_a_specific_podcast_response_200_data_platform_links

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
