from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_details_response_200_data_awards_item import GetCreatorDetailsResponse200DataAwardsItem
    from ..models.get_creator_details_response_200_data_images import GetCreatorDetailsResponse200DataImages
    from ..models.get_creator_details_response_200_data_links import GetCreatorDetailsResponse200DataLinks
    from ..models.get_creator_details_response_200_data_role import GetCreatorDetailsResponse200DataRole
    from ..models.get_creator_details_response_200_data_roles_item import GetCreatorDetailsResponse200DataRolesItem


T = TypeVar("T", bound="GetCreatorDetailsResponse200Data")


@_attrs_define
class GetCreatorDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        role (GetCreatorDetailsResponse200DataRole | Unset):
        roles (list[GetCreatorDetailsResponse200DataRolesItem] | Unset):
        photo_url (str | Unset):
        images (GetCreatorDetailsResponse200DataImages | Unset):
        gender (str | Unset):
        birth (str | Unset):
        death (None | str | Unset):
        birth_place (str | Unset):
        country (str | Unset):
        aliases (list[Any] | Unset):
        links (GetCreatorDetailsResponse200DataLinks | Unset):
        awards (list[GetCreatorDetailsResponse200DataAwardsItem] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    role: GetCreatorDetailsResponse200DataRole | Unset = UNSET
    roles: list[GetCreatorDetailsResponse200DataRolesItem] | Unset = UNSET
    photo_url: str | Unset = UNSET
    images: GetCreatorDetailsResponse200DataImages | Unset = UNSET
    gender: str | Unset = UNSET
    birth: str | Unset = UNSET
    death: None | str | Unset = UNSET
    birth_place: str | Unset = UNSET
    country: str | Unset = UNSET
    aliases: list[Any] | Unset = UNSET
    links: GetCreatorDetailsResponse200DataLinks | Unset = UNSET
    awards: list[GetCreatorDetailsResponse200DataAwardsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        photo_url = self.photo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        gender = self.gender

        birth = self.birth

        death: None | str | Unset
        if isinstance(self.death, Unset):
            death = UNSET
        else:
            death = self.death

        birth_place = self.birth_place

        country = self.country

        aliases: list[Any] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        awards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if role is not UNSET:
            field_dict["role"] = role
        if roles is not UNSET:
            field_dict["roles"] = roles
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url
        if images is not UNSET:
            field_dict["images"] = images
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birth is not UNSET:
            field_dict["birth"] = birth
        if death is not UNSET:
            field_dict["death"] = death
        if birth_place is not UNSET:
            field_dict["birth_place"] = birth_place
        if country is not UNSET:
            field_dict["country"] = country
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if links is not UNSET:
            field_dict["links"] = links
        if awards is not UNSET:
            field_dict["awards"] = awards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_details_response_200_data_awards_item import (
            GetCreatorDetailsResponse200DataAwardsItem,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_images import GetCreatorDetailsResponse200DataImages  # noqa: PLC0415
        from ..models.get_creator_details_response_200_data_links import GetCreatorDetailsResponse200DataLinks  # noqa: PLC0415
        from ..models.get_creator_details_response_200_data_role import GetCreatorDetailsResponse200DataRole  # noqa: PLC0415
        from ..models.get_creator_details_response_200_data_roles_item import GetCreatorDetailsResponse200DataRolesItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _role = d.pop("role", UNSET)
        role: GetCreatorDetailsResponse200DataRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = GetCreatorDetailsResponse200DataRole.from_dict(_role)

        _roles = d.pop("roles", UNSET)
        roles: list[GetCreatorDetailsResponse200DataRolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = GetCreatorDetailsResponse200DataRolesItem.from_dict(roles_item_data)

                roles.append(roles_item)

        photo_url = d.pop("photo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetCreatorDetailsResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetCreatorDetailsResponse200DataImages.from_dict(_images)

        gender = d.pop("gender", UNSET)

        birth = d.pop("birth", UNSET)

        def _parse_death(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        death = _parse_death(d.pop("death", UNSET))

        birth_place = d.pop("birth_place", UNSET)

        country = d.pop("country", UNSET)

        aliases = cast(list[Any], d.pop("aliases", UNSET))

        _links = d.pop("links", UNSET)
        links: GetCreatorDetailsResponse200DataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GetCreatorDetailsResponse200DataLinks.from_dict(_links)

        _awards = d.pop("awards", UNSET)
        awards: list[GetCreatorDetailsResponse200DataAwardsItem] | Unset = UNSET
        if _awards is not UNSET:
            awards = []
            for awards_item_data in _awards:
                awards_item = GetCreatorDetailsResponse200DataAwardsItem.from_dict(awards_item_data)

                awards.append(awards_item)

        get_creator_details_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            role=role,
            roles=roles,
            photo_url=photo_url,
            images=images,
            gender=gender,
            birth=birth,
            death=death,
            birth_place=birth_place,
            country=country,
            aliases=aliases,
            links=links,
            awards=awards,
        )

        get_creator_details_response_200_data.additional_properties = d
        return get_creator_details_response_200_data

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
