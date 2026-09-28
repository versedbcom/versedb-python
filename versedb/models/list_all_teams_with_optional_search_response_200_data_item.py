from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_all_teams_with_optional_search_response_200_data_item_images import (
        ListAllTeamsWithOptionalSearchResponse200DataItemImages,
    )


T = TypeVar("T", bound="ListAllTeamsWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllTeamsWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        aliases (list[str] | Unset):
        headquarters (str | Unset):
        members_count (int | Unset):
        appearances_count (int | Unset):
        image_url (str | Unset):
        images (ListAllTeamsWithOptionalSearchResponse200DataItemImages | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    headquarters: str | Unset = UNSET
    members_count: int | Unset = UNSET
    appearances_count: int | Unset = UNSET
    image_url: str | Unset = UNSET
    images: ListAllTeamsWithOptionalSearchResponse200DataItemImages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        headquarters = self.headquarters

        members_count = self.members_count

        appearances_count = self.appearances_count

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if members_count is not UNSET:
            field_dict["members_count"] = members_count
        if appearances_count is not UNSET:
            field_dict["appearances_count"] = appearances_count
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_teams_with_optional_search_response_200_data_item_images import (
            ListAllTeamsWithOptionalSearchResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        headquarters = d.pop("headquarters", UNSET)

        members_count = d.pop("members_count", UNSET)

        appearances_count = d.pop("appearances_count", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListAllTeamsWithOptionalSearchResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListAllTeamsWithOptionalSearchResponse200DataItemImages.from_dict(_images)

        list_all_teams_with_optional_search_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            aliases=aliases,
            headquarters=headquarters,
            members_count=members_count,
            appearances_count=appearances_count,
            image_url=image_url,
            images=images,
        )

        list_all_teams_with_optional_search_response_200_data_item.additional_properties = d
        return list_all_teams_with_optional_search_response_200_data_item

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
