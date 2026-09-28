from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_characters_for_a_specific_teammembers_response_200_data_item_images import (
        GetCharactersForASpecificTeammembersResponse200DataItemImages,
    )


T = TypeVar("T", bound="GetCharactersForASpecificTeammembersResponse200DataItem")


@_attrs_define
class GetCharactersForASpecificTeammembersResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        real_name (str | Unset):
        aliases (list[str] | Unset):
        race (str | Unset):
        image_url (str | Unset):
        images (GetCharactersForASpecificTeammembersResponse200DataItemImages | Unset):
        appearances_count (int | Unset):
        publisher_name (str | Unset):
        pivot_role (str | Unset):
        pivot_joined_date (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    real_name: str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    race: str | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetCharactersForASpecificTeammembersResponse200DataItemImages | Unset = UNSET
    appearances_count: int | Unset = UNSET
    publisher_name: str | Unset = UNSET
    pivot_role: str | Unset = UNSET
    pivot_joined_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        real_name = self.real_name

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        race = self.race

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        appearances_count = self.appearances_count

        publisher_name = self.publisher_name

        pivot_role = self.pivot_role

        pivot_joined_date = self.pivot_joined_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if real_name is not UNSET:
            field_dict["real_name"] = real_name
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if race is not UNSET:
            field_dict["race"] = race
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images
        if appearances_count is not UNSET:
            field_dict["appearances_count"] = appearances_count
        if publisher_name is not UNSET:
            field_dict["publisher_name"] = publisher_name
        if pivot_role is not UNSET:
            field_dict["pivot_role"] = pivot_role
        if pivot_joined_date is not UNSET:
            field_dict["pivot_joined_date"] = pivot_joined_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_characters_for_a_specific_teammembers_response_200_data_item_images import (
            GetCharactersForASpecificTeammembersResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        real_name = d.pop("real_name", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        race = d.pop("race", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetCharactersForASpecificTeammembersResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetCharactersForASpecificTeammembersResponse200DataItemImages.from_dict(_images)

        appearances_count = d.pop("appearances_count", UNSET)

        publisher_name = d.pop("publisher_name", UNSET)

        pivot_role = d.pop("pivot_role", UNSET)

        pivot_joined_date = d.pop("pivot_joined_date", UNSET)

        get_characters_for_a_specific_teammembers_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            real_name=real_name,
            aliases=aliases,
            race=race,
            image_url=image_url,
            images=images,
            appearances_count=appearances_count,
            publisher_name=publisher_name,
            pivot_role=pivot_role,
            pivot_joined_date=pivot_joined_date,
        )

        get_characters_for_a_specific_teammembers_response_200_data_item.additional_properties = d
        return get_characters_for_a_specific_teammembers_response_200_data_item

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
