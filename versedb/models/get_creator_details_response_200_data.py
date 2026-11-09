from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_creator_details_response_200_data_aliases_i18n import GetCreatorDetailsResponse200DataAliasesI18N
    from ..models.get_creator_details_response_200_data_awards_item import GetCreatorDetailsResponse200DataAwardsItem
    from ..models.get_creator_details_response_200_data_images_type_0 import GetCreatorDetailsResponse200DataImagesType0
    from ..models.get_creator_details_response_200_data_links_type_0_item import (
        GetCreatorDetailsResponse200DataLinksType0Item,
    )
    from ..models.get_creator_details_response_200_data_links_type_1 import GetCreatorDetailsResponse200DataLinksType1
    from ..models.get_creator_details_response_200_data_name_i18n import GetCreatorDetailsResponse200DataNameI18N
    from ..models.get_creator_details_response_200_data_role_type_0 import GetCreatorDetailsResponse200DataRoleType0
    from ..models.get_creator_details_response_200_data_roles_item import GetCreatorDetailsResponse200DataRolesItem


T = TypeVar("T", bound="GetCreatorDetailsResponse200Data")


@_attrs_define
class GetCreatorDetailsResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        role (GetCreatorDetailsResponse200DataRoleType0 | None):
        roles (list[GetCreatorDetailsResponse200DataRolesItem]):
        photo_url (None | str):
        images (GetCreatorDetailsResponse200DataImagesType0 | None):
        gender (None | str):
        birth (None | str):
        death (None | str):
        birth_place (None | str):
        country (None | str):
        aliases (list[str] | None):
        links (GetCreatorDetailsResponse200DataLinksType1 | list[GetCreatorDetailsResponse200DataLinksType0Item] |
            None): The creator's links: a list of {url, type or label}, a few older rows a map by name, or null.
        awards (list[GetCreatorDetailsResponse200DataAwardsItem]):
        name_i18n (GetCreatorDetailsResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetCreatorDetailsResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    role: GetCreatorDetailsResponse200DataRoleType0 | None
    roles: list[GetCreatorDetailsResponse200DataRolesItem]
    photo_url: None | str
    images: GetCreatorDetailsResponse200DataImagesType0 | None
    gender: None | str
    birth: None | str
    death: None | str
    birth_place: None | str
    country: None | str
    aliases: list[str] | None
    links: GetCreatorDetailsResponse200DataLinksType1 | list[GetCreatorDetailsResponse200DataLinksType0Item] | None
    awards: list[GetCreatorDetailsResponse200DataAwardsItem]
    name_i18n: GetCreatorDetailsResponse200DataNameI18N
    aliases_i18n: GetCreatorDetailsResponse200DataAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_creator_details_response_200_data_images_type_0 import (
            GetCreatorDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_links_type_1 import (
            GetCreatorDetailsResponse200DataLinksType1,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_role_type_0 import GetCreatorDetailsResponse200DataRoleType0  # noqa: PLC0415

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        role: dict[str, Any] | None
        if isinstance(self.role, GetCreatorDetailsResponse200DataRoleType0):
            role = self.role.to_dict()
        else:
            role = self.role

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        photo_url: None | str
        photo_url = self.photo_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetCreatorDetailsResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        gender: None | str
        gender = self.gender

        birth: None | str
        birth = self.birth

        death: None | str
        death = self.death

        birth_place: None | str
        birth_place = self.birth_place

        country: None | str
        country = self.country

        aliases: list[str] | None
        if isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        links: dict[str, Any] | list[dict[str, Any]] | None
        if isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        elif isinstance(self.links, GetCreatorDetailsResponse200DataLinksType1):
            links = self.links.to_dict()
        else:
            links = self.links

        awards = []
        for awards_item_data in self.awards:
            awards_item = awards_item_data.to_dict()
            awards.append(awards_item)

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "role": role,
                "roles": roles,
                "photo_url": photo_url,
                "images": images,
                "gender": gender,
                "birth": birth,
                "death": death,
                "birth_place": birth_place,
                "country": country,
                "aliases": aliases,
                "links": links,
                "awards": awards,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_details_response_200_data_aliases_i18n import (
            GetCreatorDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_awards_item import (
            GetCreatorDetailsResponse200DataAwardsItem,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_images_type_0 import (
            GetCreatorDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_links_type_0_item import (
            GetCreatorDetailsResponse200DataLinksType0Item,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_links_type_1 import (
            GetCreatorDetailsResponse200DataLinksType1,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_name_i18n import GetCreatorDetailsResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_creator_details_response_200_data_role_type_0 import GetCreatorDetailsResponse200DataRoleType0  # noqa: PLC0415
        from ..models.get_creator_details_response_200_data_roles_item import GetCreatorDetailsResponse200DataRolesItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_role(data: object) -> GetCreatorDetailsResponse200DataRoleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_0 = GetCreatorDetailsResponse200DataRoleType0.from_dict(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCreatorDetailsResponse200DataRoleType0 | None, data)

        role = _parse_role(d.pop("role"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = GetCreatorDetailsResponse200DataRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        def _parse_photo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        photo_url = _parse_photo_url(d.pop("photo_url"))

        def _parse_images(data: object) -> GetCreatorDetailsResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetCreatorDetailsResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCreatorDetailsResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        def _parse_birth(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth = _parse_birth(d.pop("birth"))

        def _parse_death(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        death = _parse_death(d.pop("death"))

        def _parse_birth_place(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth_place = _parse_birth_place(d.pop("birth_place"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_aliases(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        aliases = _parse_aliases(d.pop("aliases"))

        def _parse_links(
            data: object,
        ) -> GetCreatorDetailsResponse200DataLinksType1 | list[GetCreatorDetailsResponse200DataLinksType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = GetCreatorDetailsResponse200DataLinksType0Item.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                links_type_1 = GetCreatorDetailsResponse200DataLinksType1.from_dict(data)

                return links_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCreatorDetailsResponse200DataLinksType1
                | list[GetCreatorDetailsResponse200DataLinksType0Item]
                | None,
                data,
            )

        links = _parse_links(d.pop("links"))

        awards = []
        _awards = d.pop("awards")
        for awards_item_data in _awards:
            awards_item = GetCreatorDetailsResponse200DataAwardsItem.from_dict(awards_item_data)

            awards.append(awards_item)

        name_i18n = GetCreatorDetailsResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetCreatorDetailsResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

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
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
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
