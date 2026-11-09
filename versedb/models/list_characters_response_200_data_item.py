from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_characters_response_200_data_item_aliases_i18n import (
        ListCharactersResponse200DataItemAliasesI18N,
    )
    from ..models.list_characters_response_200_data_item_images_type_0 import (
        ListCharactersResponse200DataItemImagesType0,
    )
    from ..models.list_characters_response_200_data_item_name_i18n import ListCharactersResponse200DataItemNameI18N
    from ..models.list_characters_response_200_data_item_real_name_i18n import (
        ListCharactersResponse200DataItemRealNameI18N,
    )


T = TypeVar("T", bound="ListCharactersResponse200DataItem")


@_attrs_define
class ListCharactersResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        real_name (None | str):
        aliases (list[str]):
        race (None | str):
        image_url (None | str):
        images (ListCharactersResponse200DataItemImagesType0 | None):
        appearances_count (int):
        name_i18n (ListCharactersResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (ListCharactersResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        real_name_i18n (ListCharactersResponse200DataItemRealNameI18N): One name per language, keyed by BCP 47 tag.
        publisher_name (None | str | Unset): Present when the character has a publisher.
    """

    id: int
    name: None | str
    slug: None | str
    real_name: None | str
    aliases: list[str]
    race: None | str
    image_url: None | str
    images: ListCharactersResponse200DataItemImagesType0 | None
    appearances_count: int
    name_i18n: ListCharactersResponse200DataItemNameI18N
    aliases_i18n: ListCharactersResponse200DataItemAliasesI18N
    original_locale: None | str
    real_name_i18n: ListCharactersResponse200DataItemRealNameI18N
    publisher_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_characters_response_200_data_item_images_type_0 import (
            ListCharactersResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        real_name: None | str
        real_name = self.real_name

        aliases = self.aliases

        race: None | str
        race = self.race

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListCharactersResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        appearances_count = self.appearances_count

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        real_name_i18n = self.real_name_i18n.to_dict()

        publisher_name: None | str | Unset
        if isinstance(self.publisher_name, Unset):
            publisher_name = UNSET
        else:
            publisher_name = self.publisher_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "real_name": real_name,
                "aliases": aliases,
                "race": race,
                "image_url": image_url,
                "images": images,
                "appearances_count": appearances_count,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "real_name_i18n": real_name_i18n,
            }
        )
        if publisher_name is not UNSET:
            field_dict["publisher_name"] = publisher_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_characters_response_200_data_item_aliases_i18n import (
            ListCharactersResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.list_characters_response_200_data_item_images_type_0 import (
            ListCharactersResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.list_characters_response_200_data_item_name_i18n import ListCharactersResponse200DataItemNameI18N  # noqa: PLC0415
        from ..models.list_characters_response_200_data_item_real_name_i18n import (
            ListCharactersResponse200DataItemRealNameI18N,  # noqa: PLC0415
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

        def _parse_real_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        real_name = _parse_real_name(d.pop("real_name"))

        aliases = cast(list[str], d.pop("aliases"))

        def _parse_race(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        race = _parse_race(d.pop("race"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> ListCharactersResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListCharactersResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListCharactersResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        appearances_count = d.pop("appearances_count")

        name_i18n = ListCharactersResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListCharactersResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        real_name_i18n = ListCharactersResponse200DataItemRealNameI18N.from_dict(d.pop("real_name_i18n"))

        def _parse_publisher_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name", UNSET))

        list_characters_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            real_name=real_name,
            aliases=aliases,
            race=race,
            image_url=image_url,
            images=images,
            appearances_count=appearances_count,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            real_name_i18n=real_name_i18n,
            publisher_name=publisher_name,
        )

        list_characters_response_200_data_item.additional_properties = d
        return list_characters_response_200_data_item

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
