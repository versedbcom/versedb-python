from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_character_teams_response_200_data_item_membership import (
        GetCharacterTeamsResponse200DataItemMembership,
    )


T = TypeVar("T", bound="GetCharacterTeamsResponse200DataItem")


@_attrs_define
class GetCharacterTeamsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        image_url (str | Unset):
        membership (GetCharacterTeamsResponse200DataItemMembership | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    image_url: str | Unset = UNSET
    membership: GetCharacterTeamsResponse200DataItemMembership | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        image_url = self.image_url

        membership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.membership, Unset):
            membership = self.membership.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if membership is not UNSET:
            field_dict["membership"] = membership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_character_teams_response_200_data_item_membership import (
            GetCharacterTeamsResponse200DataItemMembership,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        image_url = d.pop("image_url", UNSET)

        _membership = d.pop("membership", UNSET)
        membership: GetCharacterTeamsResponse200DataItemMembership | Unset
        if isinstance(_membership, Unset):
            membership = UNSET
        else:
            membership = GetCharacterTeamsResponse200DataItemMembership.from_dict(_membership)

        get_character_teams_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            image_url=image_url,
            membership=membership,
        )

        get_character_teams_response_200_data_item.additional_properties = d
        return get_character_teams_response_200_data_item

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
