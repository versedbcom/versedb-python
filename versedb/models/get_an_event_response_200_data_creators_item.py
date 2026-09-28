from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_creators_item_images import GetAnEventResponse200DataCreatorsItemImages


T = TypeVar("T", bound="GetAnEventResponse200DataCreatorsItem")


@_attrs_define
class GetAnEventResponse200DataCreatorsItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        photo_url (str | Unset):
        images (GetAnEventResponse200DataCreatorsItemImages | Unset):
        country (str | Unset):
        appearance_types (list[str] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    photo_url: str | Unset = UNSET
    images: GetAnEventResponse200DataCreatorsItemImages | Unset = UNSET
    country: str | Unset = UNSET
    appearance_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        photo_url = self.photo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        country = self.country

        appearance_types: list[str] | Unset = UNSET
        if not isinstance(self.appearance_types, Unset):
            appearance_types = self.appearance_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url
        if images is not UNSET:
            field_dict["images"] = images
        if country is not UNSET:
            field_dict["country"] = country
        if appearance_types is not UNSET:
            field_dict["appearance_types"] = appearance_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_creators_item_images import (
            GetAnEventResponse200DataCreatorsItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        photo_url = d.pop("photo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetAnEventResponse200DataCreatorsItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetAnEventResponse200DataCreatorsItemImages.from_dict(_images)

        country = d.pop("country", UNSET)

        appearance_types = cast(list[str], d.pop("appearance_types", UNSET))

        get_an_event_response_200_data_creators_item = cls(
            id=id,
            name=name,
            slug=slug,
            photo_url=photo_url,
            images=images,
            country=country,
            appearance_types=appearance_types,
        )

        get_an_event_response_200_data_creators_item.additional_properties = d
        return get_an_event_response_200_data_creators_item

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
