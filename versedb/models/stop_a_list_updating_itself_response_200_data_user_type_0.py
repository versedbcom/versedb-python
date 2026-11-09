from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StopAListUpdatingItselfResponse200DataUserType0")


@_attrs_define
class StopAListUpdatingItselfResponse200DataUserType0:
    """The owner; null once the account is gone.

    Attributes:
        id (int):
        username (None | str):
        name (None | str):
        avatar (None | str):
    """

    id: int
    username: None | str
    name: None | str
    avatar: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username: None | str
        username = self.username

        name: None | str
        name = self.name

        avatar: None | str
        avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "name": name,
                "avatar": avatar,
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

        def _parse_avatar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        stop_a_list_updating_itself_response_200_data_user_type_0 = cls(
            id=id,
            username=username,
            name=name,
            avatar=avatar,
        )

        stop_a_list_updating_itself_response_200_data_user_type_0.additional_properties = d
        return stop_a_list_updating_itself_response_200_data_user_type_0

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
