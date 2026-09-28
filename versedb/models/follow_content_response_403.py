from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowContentResponse403")


@_attrs_define
class FollowContentResponse403:
    """
    Attributes:
        message (str | Unset):
        code (str | Unset):
        is_following (bool | Unset):
    """

    message: str | Unset = UNSET
    code: str | Unset = UNSET
    is_following: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        is_following = self.is_following

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if is_following is not UNSET:
            field_dict["is_following"] = is_following

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        is_following = d.pop("is_following", UNSET)

        follow_content_response_403 = cls(
            message=message,
            code=code,
            is_following=is_following,
        )

        follow_content_response_403.additional_properties = d
        return follow_content_response_403

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
