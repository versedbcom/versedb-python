from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_list_response_200_data_items_item import GetListResponse200DataItemsItem
    from ..models.get_list_response_200_data_user import GetListResponse200DataUser


T = TypeVar("T", bound="GetListResponse200Data")


@_attrs_define
class GetListResponse200Data:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        description (str | Unset):
        entity_type (str | Unset):
        is_ranked (bool | Unset):
        is_private (bool | Unset):
        items_count (int | Unset):
        likes_count (int | Unset):
        saves_count (int | Unset):
        user (GetListResponse200DataUser | Unset):
        items (list[GetListResponse200DataItemsItem] | Unset):
        created_at (str | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    is_ranked: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    items_count: int | Unset = UNSET
    likes_count: int | Unset = UNSET
    saves_count: int | Unset = UNSET
    user: GetListResponse200DataUser | Unset = UNSET
    items: list[GetListResponse200DataItemsItem] | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        entity_type = self.entity_type

        is_ranked = self.is_ranked

        is_private = self.is_private

        items_count = self.items_count

        likes_count = self.likes_count

        saves_count = self.saves_count

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if is_ranked is not UNSET:
            field_dict["is_ranked"] = is_ranked
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if items_count is not UNSET:
            field_dict["items_count"] = items_count
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if saves_count is not UNSET:
            field_dict["saves_count"] = saves_count
        if user is not UNSET:
            field_dict["user"] = user
        if items is not UNSET:
            field_dict["items"] = items
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_list_response_200_data_items_item import GetListResponse200DataItemsItem  # noqa: PLC0415
        from ..models.get_list_response_200_data_user import GetListResponse200DataUser  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        is_ranked = d.pop("is_ranked", UNSET)

        is_private = d.pop("is_private", UNSET)

        items_count = d.pop("items_count", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        saves_count = d.pop("saves_count", UNSET)

        _user = d.pop("user", UNSET)
        user: GetListResponse200DataUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetListResponse200DataUser.from_dict(_user)

        _items = d.pop("items", UNSET)
        items: list[GetListResponse200DataItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetListResponse200DataItemsItem.from_dict(items_item_data)

                items.append(items_item)

        created_at = d.pop("created_at", UNSET)

        get_list_response_200_data = cls(
            id=id,
            title=title,
            description=description,
            entity_type=entity_type,
            is_ranked=is_ranked,
            is_private=is_private,
            items_count=items_count,
            likes_count=likes_count,
            saves_count=saves_count,
            user=user,
            items=items,
            created_at=created_at,
        )

        get_list_response_200_data.additional_properties = d
        return get_list_response_200_data

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
