from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListFollowsResponse200DataItemFollowableType0")


@_attrs_define
class ListFollowsResponse200DataItemFollowableType0:
    """The followed entity, or null when it is gone.

    Attributes:
        id (int):
        name (str):
        slug (None | str):
        username (None | str): A member's username; null for anything else.
        image_url (None | str):
    """

    id: int
    name: str
    slug: None | str
    username: None | str
    image_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug: None | str
        slug = self.slug

        username: None | str
        username = self.username

        image_url: None | str
        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "username": username,
                "image_url": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        list_follows_response_200_data_item_followable_type_0 = cls(
            id=id,
            name=name,
            slug=slug,
            username=username,
            image_url=image_url,
        )

        list_follows_response_200_data_item_followable_type_0.additional_properties = d
        return list_follows_response_200_data_item_followable_type_0

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
