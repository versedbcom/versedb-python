from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_creators_response_200_data_item_aliases_i18n import ListCreatorsResponse200DataItemAliasesI18N
    from ..models.list_creators_response_200_data_item_images_type_0 import ListCreatorsResponse200DataItemImagesType0
    from ..models.list_creators_response_200_data_item_name_i18n import ListCreatorsResponse200DataItemNameI18N
    from ..models.list_creators_response_200_data_item_role_type_0 import ListCreatorsResponse200DataItemRoleType0
    from ..models.list_creators_response_200_data_item_roles_item import ListCreatorsResponse200DataItemRolesItem


T = TypeVar("T", bound="ListCreatorsResponse200DataItem")


@_attrs_define
class ListCreatorsResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        role (ListCreatorsResponse200DataItemRoleType0 | None):
        roles (list[ListCreatorsResponse200DataItemRolesItem]):
        photo_url (None | str):
        images (ListCreatorsResponse200DataItemImagesType0 | None):
        name_i18n (ListCreatorsResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (ListCreatorsResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    role: ListCreatorsResponse200DataItemRoleType0 | None
    roles: list[ListCreatorsResponse200DataItemRolesItem]
    photo_url: None | str
    images: ListCreatorsResponse200DataItemImagesType0 | None
    name_i18n: ListCreatorsResponse200DataItemNameI18N
    aliases_i18n: ListCreatorsResponse200DataItemAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_creators_response_200_data_item_images_type_0 import (
            ListCreatorsResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.list_creators_response_200_data_item_role_type_0 import ListCreatorsResponse200DataItemRoleType0  # noqa: PLC0415

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        role: dict[str, Any] | None
        if isinstance(self.role, ListCreatorsResponse200DataItemRoleType0):
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
        if isinstance(self.images, ListCreatorsResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

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
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_creators_response_200_data_item_aliases_i18n import (
            ListCreatorsResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.list_creators_response_200_data_item_images_type_0 import (
            ListCreatorsResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.list_creators_response_200_data_item_name_i18n import ListCreatorsResponse200DataItemNameI18N  # noqa: PLC0415
        from ..models.list_creators_response_200_data_item_role_type_0 import ListCreatorsResponse200DataItemRoleType0  # noqa: PLC0415
        from ..models.list_creators_response_200_data_item_roles_item import ListCreatorsResponse200DataItemRolesItem  # noqa: PLC0415

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

        def _parse_role(data: object) -> ListCreatorsResponse200DataItemRoleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_0 = ListCreatorsResponse200DataItemRoleType0.from_dict(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCreatorsResponse200DataItemRoleType0 | None, data)

        role = _parse_role(d.pop("role"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = ListCreatorsResponse200DataItemRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        def _parse_photo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        photo_url = _parse_photo_url(d.pop("photo_url"))

        def _parse_images(data: object) -> ListCreatorsResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListCreatorsResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCreatorsResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        name_i18n = ListCreatorsResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListCreatorsResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        list_creators_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            role=role,
            roles=roles,
            photo_url=photo_url,
            images=images,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        list_creators_response_200_data_item.additional_properties = d
        return list_creators_response_200_data_item

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
