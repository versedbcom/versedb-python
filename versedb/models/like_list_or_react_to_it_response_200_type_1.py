from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LikeListOrReactToItResponse200Type1")


@_attrs_define
class LikeListOrReactToItResponse200Type1:
    """Already Liked

    Attributes:
        message (str | Unset):
        liked (bool | Unset):
    """

    message: str | Unset = UNSET
    liked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        liked = self.liked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if liked is not UNSET:
            field_dict["liked"] = liked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        liked = d.pop("liked", UNSET)

        like_list_or_react_to_it_response_200_type_1 = cls(
            message=message,
            liked=liked,
        )

        like_list_or_react_to_it_response_200_type_1.additional_properties = d
        return like_list_or_react_to_it_response_200_type_1

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
