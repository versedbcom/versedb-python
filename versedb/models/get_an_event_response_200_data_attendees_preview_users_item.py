from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAnEventResponse200DataAttendeesPreviewUsersItem")


@_attrs_define
class GetAnEventResponse200DataAttendeesPreviewUsersItem:
    """
    Attributes:
        id (int):
        username (None | str):
        name (None | str):
        profile_image_url (None | str):
        is_private (bool):
    """

    id: int
    username: None | str
    name: None | str
    profile_image_url: None | str
    is_private: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username: None | str
        username = self.username

        name: None | str
        name = self.name

        profile_image_url: None | str
        profile_image_url = self.profile_image_url

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "name": name,
                "profile_image_url": profile_image_url,
                "is_private": is_private,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_profile_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_image_url = _parse_profile_image_url(d.pop("profile_image_url"))

        is_private = d.pop("is_private")

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
