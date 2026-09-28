from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_attendees_preview_users_item import (
        GetAnEventResponse200DataAttendeesPreviewUsersItem,
    )


T = TypeVar("T", bound="GetAnEventResponse200DataAttendeesPreview")


@_attrs_define
class GetAnEventResponse200DataAttendeesPreview:
    """
    Attributes:
        total (int | Unset):
        users (list[GetAnEventResponse200DataAttendeesPreviewUsersItem] | Unset):
    """

    total: int | Unset = UNSET
    users: list[GetAnEventResponse200DataAttendeesPreviewUsersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_attendees_preview_users_item import (
            GetAnEventResponse200DataAttendeesPreviewUsersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _users = d.pop("users", UNSET)
        users: list[GetAnEventResponse200DataAttendeesPreviewUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = GetAnEventResponse200DataAttendeesPreviewUsersItem.from_dict(users_item_data)

                users.append(users_item)

        get_an_event_response_200_data_attendees_preview = cls(
            total=total,
            users=users,
        )

        get_an_event_response_200_data_attendees_preview.additional_properties = d
        return get_an_event_response_200_data_attendees_preview

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
