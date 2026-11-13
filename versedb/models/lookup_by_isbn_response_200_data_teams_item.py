from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_by_isbn_response_200_data_teams_item_images_type_0 import (
        LookupByIsbnResponse200DataTeamsItemImagesType0,
    )


T = TypeVar("T", bound="LookupByIsbnResponse200DataTeamsItem")


@_attrs_define
class LookupByIsbnResponse200DataTeamsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        headquarters (None | str):
        image_url (None | str):
        images (LookupByIsbnResponse200DataTeamsItemImagesType0 | None):
        sort_order (int | None):
    """

    id: int
    name: None | str
    slug: None | str
    headquarters: None | str
    image_url: None | str
    images: LookupByIsbnResponse200DataTeamsItemImagesType0 | None
    sort_order: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookup_by_isbn_response_200_data_teams_item_images_type_0 import (
            LookupByIsbnResponse200DataTeamsItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        headquarters: None | str
        headquarters = self.headquarters

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, LookupByIsbnResponse200DataTeamsItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        sort_order: int | None
        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "headquarters": headquarters,
                "image_url": image_url,
                "images": images,
                "sort_order": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_isbn_response_200_data_teams_item_images_type_0 import (
            LookupByIsbnResponse200DataTeamsItemImagesType0,  # noqa: PLC0415
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

        def _parse_headquarters(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headquarters = _parse_headquarters(d.pop("headquarters"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> LookupByIsbnResponse200DataTeamsItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = LookupByIsbnResponse200DataTeamsItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookupByIsbnResponse200DataTeamsItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_sort_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sort_order = _parse_sort_order(d.pop("sort_order"))

        lookup_by_isbn_response_200_data_teams_item = cls(
            id=id,
            name=name,
            slug=slug,
            headquarters=headquarters,
            image_url=image_url,
            images=images,
            sort_order=sort_order,
        )

        lookup_by_isbn_response_200_data_teams_item.additional_properties = d
        return lookup_by_isbn_response_200_data_teams_item

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
