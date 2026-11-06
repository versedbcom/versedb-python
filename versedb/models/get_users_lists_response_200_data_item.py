from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_users_lists_response_200_data_item_user import GetUsersListsResponse200DataItemUser


T = TypeVar("T", bound="GetUsersListsResponse200DataItem")


@_attrs_define
class GetUsersListsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        entity_type (str | Unset):
        items_count (int | Unset):
        is_private (bool | Unset):
        user (GetUsersListsResponse200DataItemUser | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    items_count: int | Unset = UNSET
    is_private: bool | Unset = UNSET
    user: GetUsersListsResponse200DataItemUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        entity_type = self.entity_type

        items_count = self.items_count

        is_private = self.is_private

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if items_count is not UNSET:
            field_dict["items_count"] = items_count
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_users_lists_response_200_data_item_user import GetUsersListsResponse200DataItemUser  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        items_count = d.pop("items_count", UNSET)

        is_private = d.pop("is_private", UNSET)

        _user = d.pop("user", UNSET)
        user: GetUsersListsResponse200DataItemUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetUsersListsResponse200DataItemUser.from_dict(_user)

        get_users_lists_response_200_data_item = cls(
            id=id,
            title=title,
            entity_type=entity_type,
            items_count=items_count,
            is_private=is_private,
            user=user,
        )

        get_users_lists_response_200_data_item.additional_properties = d
        return get_users_lists_response_200_data_item

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
