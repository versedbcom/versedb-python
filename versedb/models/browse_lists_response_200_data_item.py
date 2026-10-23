from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browse_lists_response_200_data_item_preview_items_item import (
        BrowseListsResponse200DataItemPreviewItemsItem,
    )
    from ..models.browse_lists_response_200_data_item_user import BrowseListsResponse200DataItemUser


T = TypeVar("T", bound="BrowseListsResponse200DataItem")


@_attrs_define
class BrowseListsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        entity_type (str | Unset):
        is_ranked (bool | Unset):
        items_count (int | Unset):
        likes_count (int | Unset):
        saves_count (int | Unset):
        user (BrowseListsResponse200DataItemUser | Unset):
        preview_items (list[BrowseListsResponse200DataItemPreviewItemsItem] | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    is_ranked: bool | Unset = UNSET
    items_count: int | Unset = UNSET
    likes_count: int | Unset = UNSET
    saves_count: int | Unset = UNSET
    user: BrowseListsResponse200DataItemUser | Unset = UNSET
    preview_items: list[BrowseListsResponse200DataItemPreviewItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        entity_type = self.entity_type

        is_ranked = self.is_ranked

        items_count = self.items_count

        likes_count = self.likes_count

        saves_count = self.saves_count

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        preview_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preview_items, Unset):
            preview_items = []
            for preview_items_item_data in self.preview_items:
                preview_items_item = preview_items_item_data.to_dict()
                preview_items.append(preview_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if is_ranked is not UNSET:
            field_dict["is_ranked"] = is_ranked
        if items_count is not UNSET:
            field_dict["items_count"] = items_count
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if saves_count is not UNSET:
            field_dict["saves_count"] = saves_count
        if user is not UNSET:
            field_dict["user"] = user
        if preview_items is not UNSET:
            field_dict["preview_items"] = preview_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browse_lists_response_200_data_item_preview_items_item import (
            BrowseListsResponse200DataItemPreviewItemsItem,  # noqa: PLC0415
        )
        from ..models.browse_lists_response_200_data_item_user import BrowseListsResponse200DataItemUser  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        is_ranked = d.pop("is_ranked", UNSET)

        items_count = d.pop("items_count", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        saves_count = d.pop("saves_count", UNSET)

        _user = d.pop("user", UNSET)
        user: BrowseListsResponse200DataItemUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = BrowseListsResponse200DataItemUser.from_dict(_user)

        _preview_items = d.pop("preview_items", UNSET)
        preview_items: list[BrowseListsResponse200DataItemPreviewItemsItem] | Unset = UNSET
        if _preview_items is not UNSET:
            preview_items = []
            for preview_items_item_data in _preview_items:
                preview_items_item = BrowseListsResponse200DataItemPreviewItemsItem.from_dict(preview_items_item_data)

                preview_items.append(preview_items_item)

        browse_lists_response_200_data_item = cls(
            id=id,
            title=title,
            entity_type=entity_type,
            is_ranked=is_ranked,
            items_count=items_count,
            likes_count=likes_count,
            saves_count=saves_count,
            user=user,
            preview_items=preview_items,
        )

        browse_lists_response_200_data_item.additional_properties = d
        return browse_lists_response_200_data_item

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
