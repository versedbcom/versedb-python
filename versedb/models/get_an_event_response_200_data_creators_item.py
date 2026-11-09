from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_creators_item_images_type_0 import (
        GetAnEventResponse200DataCreatorsItemImagesType0,
    )


T = TypeVar("T", bound="GetAnEventResponse200DataCreatorsItem")


@_attrs_define
class GetAnEventResponse200DataCreatorsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        photo_url (None | str):
        images (GetAnEventResponse200DataCreatorsItemImagesType0 | None):
        country (None | str):
        appearance_types (list[str]):
    """

    id: int
    name: None | str
    slug: None | str
    photo_url: None | str
    images: GetAnEventResponse200DataCreatorsItemImagesType0 | None
    country: None | str
    appearance_types: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_an_event_response_200_data_creators_item_images_type_0 import (
            GetAnEventResponse200DataCreatorsItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        photo_url: None | str
        photo_url = self.photo_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetAnEventResponse200DataCreatorsItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        country: None | str
        country = self.country

        appearance_types = self.appearance_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "photo_url": photo_url,
                "images": images,
                "country": country,
                "appearance_types": appearance_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_creators_item_images_type_0 import (
            GetAnEventResponse200DataCreatorsItemImagesType0,  # noqa: PLC0415
        )

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

        def _parse_photo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        photo_url = _parse_photo_url(d.pop("photo_url"))

        def _parse_images(data: object) -> GetAnEventResponse200DataCreatorsItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetAnEventResponse200DataCreatorsItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAnEventResponse200DataCreatorsItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        appearance_types = cast(list[str], d.pop("appearance_types"))

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
