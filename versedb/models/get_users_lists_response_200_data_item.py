from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_users_lists_response_200_data_item_preview_items_item import (
        GetUsersListsResponse200DataItemPreviewItemsItem,
    )
    from ..models.get_users_lists_response_200_data_item_user_type_0 import GetUsersListsResponse200DataItemUserType0


T = TypeVar("T", bound="GetUsersListsResponse200DataItem")


@_attrs_define
class GetUsersListsResponse200DataItem:
    """
    Attributes:
        id (int):
        title (str):
        slug (str):
        entity_type (str): issues, series, characters, creators, story_arcs, teams, or mixed for a list of any type.
        list_type (str): custom, wishlist or reading_guide.
        entity_type_label (str):
        is_curated (bool): The list is VerseDB's own.
        is_smart (bool): A rule keeps the list up to date.
        is_ranked (bool):
        is_private (bool):
        items_count (int):
        saves_count (int):
        likes_count (int):
        created_at (str):
        updated_at (str):
        user (GetUsersListsResponse200DataItemUserType0 | None): The owner; null once the account is gone.
        description (str | Unset): The first 150 characters; left out when the list has none.
        preview_items (list[GetUsersListsResponse200DataItemPreviewItemsItem] | Unset): The list's first four items in
            its own order; left out when it holds none.
    """

    id: int
    title: str
    slug: str
    entity_type: str
    list_type: str
    entity_type_label: str
    is_curated: bool
    is_smart: bool
    is_ranked: bool
    is_private: bool
    items_count: int
    saves_count: int
    likes_count: int
    created_at: str
    updated_at: str
    user: GetUsersListsResponse200DataItemUserType0 | None
    description: str | Unset = UNSET
    preview_items: list[GetUsersListsResponse200DataItemPreviewItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_users_lists_response_200_data_item_user_type_0 import (
            GetUsersListsResponse200DataItemUserType0,  # noqa: PLC0415
        )

        id = self.id

        title = self.title

        slug = self.slug

        entity_type = self.entity_type

        list_type = self.list_type

        entity_type_label = self.entity_type_label

        is_curated = self.is_curated

        is_smart = self.is_smart

        is_ranked = self.is_ranked

        is_private = self.is_private

        items_count = self.items_count

        saves_count = self.saves_count

        likes_count = self.likes_count

        created_at = self.created_at

        updated_at = self.updated_at

        user: dict[str, Any] | None
        if isinstance(self.user, GetUsersListsResponse200DataItemUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        description = self.description

        preview_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preview_items, Unset):
            preview_items = []
            for preview_items_item_data in self.preview_items:
                preview_items_item = preview_items_item_data.to_dict()
                preview_items.append(preview_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "slug": slug,
                "entity_type": entity_type,
                "list_type": list_type,
                "entity_type_label": entity_type_label,
                "is_curated": is_curated,
                "is_smart": is_smart,
                "is_ranked": is_ranked,
                "is_private": is_private,
                "items_count": items_count,
                "saves_count": saves_count,
                "likes_count": likes_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "user": user,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if preview_items is not UNSET:
            field_dict["preview_items"] = preview_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_users_lists_response_200_data_item_preview_items_item import (
            GetUsersListsResponse200DataItemPreviewItemsItem,  # noqa: PLC0415
        )
        from ..models.get_users_lists_response_200_data_item_user_type_0 import (
            GetUsersListsResponse200DataItemUserType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        slug = d.pop("slug")

        entity_type = d.pop("entity_type")

        list_type = d.pop("list_type")

        entity_type_label = d.pop("entity_type_label")

        is_curated = d.pop("is_curated")

        is_smart = d.pop("is_smart")

        is_ranked = d.pop("is_ranked")

        is_private = d.pop("is_private")

        items_count = d.pop("items_count")

        saves_count = d.pop("saves_count")

        likes_count = d.pop("likes_count")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_user(data: object) -> GetUsersListsResponse200DataItemUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = GetUsersListsResponse200DataItemUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetUsersListsResponse200DataItemUserType0 | None, data)

        user = _parse_user(d.pop("user"))

        description = d.pop("description", UNSET)

        _preview_items = d.pop("preview_items", UNSET)
        preview_items: list[GetUsersListsResponse200DataItemPreviewItemsItem] | Unset = UNSET
        if _preview_items is not UNSET:
            preview_items = []
            for preview_items_item_data in _preview_items:
                preview_items_item = GetUsersListsResponse200DataItemPreviewItemsItem.from_dict(preview_items_item_data)

                preview_items.append(preview_items_item)

        get_users_lists_response_200_data_item = cls(
            id=id,
            title=title,
            slug=slug,
            entity_type=entity_type,
            list_type=list_type,
            entity_type_label=entity_type_label,
            is_curated=is_curated,
            is_smart=is_smart,
            is_ranked=is_ranked,
            is_private=is_private,
            items_count=items_count,
            saves_count=saves_count,
            likes_count=likes_count,
            created_at=created_at,
            updated_at=updated_at,
            user=user,
            description=description,
            preview_items=preview_items,
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
