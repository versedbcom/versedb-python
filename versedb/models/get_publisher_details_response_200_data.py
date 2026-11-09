from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_publisher_details_response_200_data_aliases_i18n import (
        GetPublisherDetailsResponse200DataAliasesI18N,
    )
    from ..models.get_publisher_details_response_200_data_aliases_type_4 import (
        GetPublisherDetailsResponse200DataAliasesType4,
    )
    from ..models.get_publisher_details_response_200_data_images_type_0 import (
        GetPublisherDetailsResponse200DataImagesType0,
    )
    from ..models.get_publisher_details_response_200_data_name_i18n import GetPublisherDetailsResponse200DataNameI18N


T = TypeVar("T", bound="GetPublisherDetailsResponse200Data")


@_attrs_define
class GetPublisherDetailsResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        founded_year (int | None):
        website (None | str):
        headquarters (None | str):
        parent_company (None | str):
        status (None | str): active, defunct, acquired or rebranded.
        logo_url (None | str):
        images (GetPublisherDetailsResponse200DataImagesType0 | None):
        first_published_year (int | None):
        aliases (bool | float | GetPublisherDetailsResponse200DataAliasesType4 | list[Any] | None | str): The other
            names, as stored: a list of strings in production.
        name_i18n (GetPublisherDetailsResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetPublisherDetailsResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the publisher is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    founded_year: int | None
    website: None | str
    headquarters: None | str
    parent_company: None | str
    status: None | str
    logo_url: None | str
    images: GetPublisherDetailsResponse200DataImagesType0 | None
    first_published_year: int | None
    aliases: bool | float | GetPublisherDetailsResponse200DataAliasesType4 | list[Any] | None | str
    name_i18n: GetPublisherDetailsResponse200DataNameI18N
    aliases_i18n: GetPublisherDetailsResponse200DataAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_publisher_details_response_200_data_aliases_type_4 import (
            GetPublisherDetailsResponse200DataAliasesType4,  # noqa: PLC0415
        )
        from ..models.get_publisher_details_response_200_data_images_type_0 import (
            GetPublisherDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        founded_year: int | None
        founded_year = self.founded_year

        website: None | str
        website = self.website

        headquarters: None | str
        headquarters = self.headquarters

        parent_company: None | str
        parent_company = self.parent_company

        status: None | str
        status = self.status

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetPublisherDetailsResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        first_published_year: int | None
        first_published_year = self.first_published_year

        aliases: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.aliases, list):
            aliases = self.aliases

        elif isinstance(self.aliases, GetPublisherDetailsResponse200DataAliasesType4):
            aliases = self.aliases.to_dict()
        else:
            aliases = self.aliases

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
                "founded_year": founded_year,
                "website": website,
                "headquarters": headquarters,
                "parent_company": parent_company,
                "status": status,
                "logo_url": logo_url,
                "images": images,
                "first_published_year": first_published_year,
                "aliases": aliases,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_publisher_details_response_200_data_aliases_i18n import (
            GetPublisherDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_publisher_details_response_200_data_aliases_type_4 import (
            GetPublisherDetailsResponse200DataAliasesType4,  # noqa: PLC0415
        )
        from ..models.get_publisher_details_response_200_data_images_type_0 import (
            GetPublisherDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_publisher_details_response_200_data_name_i18n import (
            GetPublisherDetailsResponse200DataNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_founded_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        founded_year = _parse_founded_year(d.pop("founded_year"))

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        def _parse_headquarters(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headquarters = _parse_headquarters(d.pop("headquarters"))

        def _parse_parent_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_company = _parse_parent_company(d.pop("parent_company"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> GetPublisherDetailsResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetPublisherDetailsResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublisherDetailsResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_first_published_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        first_published_year = _parse_first_published_year(d.pop("first_published_year"))

        def _parse_aliases(
            data: object,
        ) -> bool | float | GetPublisherDetailsResponse200DataAliasesType4 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_3 = cast(list[Any], data)

                return aliases_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aliases_type_4 = GetPublisherDetailsResponse200DataAliasesType4.from_dict(data)

                return aliases_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetPublisherDetailsResponse200DataAliasesType4 | list[Any] | None | str, data)

        aliases = _parse_aliases(d.pop("aliases"))

        name_i18n = GetPublisherDetailsResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetPublisherDetailsResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        get_publisher_details_response_200_data = cls(
            id=id,
            name=name,
            founded_year=founded_year,
            website=website,
            headquarters=headquarters,
            parent_company=parent_company,
            status=status,
            logo_url=logo_url,
            images=images,
            first_published_year=first_published_year,
            aliases=aliases,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        get_publisher_details_response_200_data.additional_properties = d
        return get_publisher_details_response_200_data

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
