from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_comic_shops_response_200_data_item_aliases_i18n import (
        ListComicShopsResponse200DataItemAliasesI18N,
    )
    from ..models.list_comic_shops_response_200_data_item_images_type_0 import (
        ListComicShopsResponse200DataItemImagesType0,
    )
    from ..models.list_comic_shops_response_200_data_item_name_i18n import ListComicShopsResponse200DataItemNameI18N


T = TypeVar("T", bound="ListComicShopsResponse200DataItem")


@_attrs_define
class ListComicShopsResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        name_i18n (ListComicShopsResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (ListComicShopsResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        city (None | str):
        state_province (None | str):
        country (None | str):
        country_code (None | str):
        logo_url (None | str):
        images (ListComicShopsResponse200DataItemImagesType0 | None):
    """

    id: int
    name: None | str
    name_i18n: ListComicShopsResponse200DataItemNameI18N
    aliases_i18n: ListComicShopsResponse200DataItemAliasesI18N
    original_locale: None | str
    city: None | str
    state_province: None | str
    country: None | str
    country_code: None | str
    logo_url: None | str
    images: ListComicShopsResponse200DataItemImagesType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_comic_shops_response_200_data_item_images_type_0 import (
            ListComicShopsResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        city: None | str
        city = self.city

        state_province: None | str
        state_province = self.state_province

        country: None | str
        country = self.country

        country_code: None | str
        country_code = self.country_code

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListComicShopsResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "city": city,
                "state_province": state_province,
                "country": country,
                "country_code": country_code,
                "logo_url": logo_url,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_comic_shops_response_200_data_item_aliases_i18n import (
            ListComicShopsResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.list_comic_shops_response_200_data_item_images_type_0 import (
            ListComicShopsResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.list_comic_shops_response_200_data_item_name_i18n import ListComicShopsResponse200DataItemNameI18N  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_i18n = ListComicShopsResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListComicShopsResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state_province(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_province = _parse_state_province(d.pop("state_province"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> ListComicShopsResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListComicShopsResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListComicShopsResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        list_comic_shops_response_200_data_item = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            city=city,
            state_province=state_province,
            country=country,
            country_code=country_code,
            logo_url=logo_url,
            images=images,
        )

        list_comic_shops_response_200_data_item.additional_properties = d
        return list_comic_shops_response_200_data_item

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
