from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_creators_response_200_data_item_images import ListCreatorsResponse200DataItemImages
    from ..models.list_creators_response_200_data_item_role import ListCreatorsResponse200DataItemRole
    from ..models.list_creators_response_200_data_item_roles_item import ListCreatorsResponse200DataItemRolesItem


T = TypeVar("T", bound="ListCreatorsResponse200DataItem")


@_attrs_define
class ListCreatorsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        role (ListCreatorsResponse200DataItemRole | Unset):
        roles (list[ListCreatorsResponse200DataItemRolesItem] | Unset):
        photo_url (str | Unset):
        images (ListCreatorsResponse200DataItemImages | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    role: ListCreatorsResponse200DataItemRole | Unset = UNSET
    roles: list[ListCreatorsResponse200DataItemRolesItem] | Unset = UNSET
    photo_url: str | Unset = UNSET
    images: ListCreatorsResponse200DataItemImages | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_creators_response_200_data_item_images import ListCreatorsResponse200DataItemImages  # noqa: PLC0415
        from ..models.list_creators_response_200_data_item_role import ListCreatorsResponse200DataItemRole  # noqa: PLC0415
        from ..models.list_creators_response_200_data_item_roles_item import ListCreatorsResponse200DataItemRolesItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _role = d.pop("role", UNSET)
        role: ListCreatorsResponse200DataItemRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ListCreatorsResponse200DataItemRole.from_dict(_role)

        _roles = d.pop("roles", UNSET)
        roles: list[ListCreatorsResponse200DataItemRolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = ListCreatorsResponse200DataItemRolesItem.from_dict(roles_item_data)

                roles.append(roles_item)

        photo_url = d.pop("photo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListCreatorsResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListCreatorsResponse200DataItemImages.from_dict(_images)

        list_creators_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            role=role,
            roles=roles,
            photo_url=photo_url,
            images=images,
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
