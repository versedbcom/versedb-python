from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAnEventResponse200DataAttendeesPreviewUsersItem")


@_attrs_define
class GetAnEventResponse200DataAttendeesPreviewUsersItem:
    """
    Attributes:
        id (int | Unset):
        username (str | Unset):
        name (str | Unset):
        profile_image_url (str | Unset):
        is_private (bool | Unset):
    """

    id: int | Unset = UNSET
    username: str | Unset = UNSET
    name: str | Unset = UNSET
    profile_image_url: str | Unset = UNSET
    is_private: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        name = self.name

        profile_image_url = self.profile_image_url

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if name is not UNSET:
            field_dict["name"] = name
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if is_private is not UNSET:
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        name = d.pop("name", UNSET)

        profile_image_url = d.pop("profile_image_url", UNSET)

        is_private = d.pop("is_private", UNSET)

        get_an_event_response_200_data_attendees_preview_users_item = cls(
            id=id,
            username=username,
            name=name,
            profile_image_url=profile_image_url,
            is_private=is_private,
        )

        get_an_event_response_200_data_attendees_preview_users_item.additional_properties = d
        return get_an_event_response_200_data_attendees_preview_users_item

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
