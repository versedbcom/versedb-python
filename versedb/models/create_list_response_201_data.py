from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_list_response_201_data_user import CreateListResponse201DataUser


T = TypeVar("T", bound="CreateListResponse201Data")


@_attrs_define
class CreateListResponse201Data:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        description (str | Unset):
        entity_type (str | Unset):
        is_ranked (bool | Unset):
        is_private (bool | Unset):
        items_count (int | Unset):
        user (CreateListResponse201DataUser | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    is_ranked: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    items_count: int | Unset = UNSET
    user: CreateListResponse201DataUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        entity_type = self.entity_type

        is_ranked = self.is_ranked

        is_private = self.is_private

        items_count = self.items_count

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
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_list_response_201_data_user import CreateListResponse201DataUser  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        is_ranked = d.pop("is_ranked", UNSET)

        is_private = d.pop("is_private", UNSET)

        items_count = d.pop("items_count", UNSET)

        _user = d.pop("user", UNSET)
        user: CreateListResponse201DataUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CreateListResponse201DataUser.from_dict(_user)

        create_list_response_201_data = cls(
            id=id,
            title=title,
            description=description,
            entity_type=entity_type,
            is_ranked=is_ranked,
            is_private=is_private,
            items_count=items_count,
            user=user,
        )

        create_list_response_201_data.additional_properties = d
        return create_list_response_201_data

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
