from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_all_publishers_with_optional_search_response_200_data_item_aliases_i18n import (
        ListAllPublishersWithOptionalSearchResponse200DataItemAliasesI18N,
    )
    from ..models.list_all_publishers_with_optional_search_response_200_data_item_images_type_0 import (
        ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0,
    )
    from ..models.list_all_publishers_with_optional_search_response_200_data_item_name_i18n import (
        ListAllPublishersWithOptionalSearchResponse200DataItemNameI18N,
    )


T = TypeVar("T", bound="ListAllPublishersWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllPublishersWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        founded_year (int | None):
        headquarters (None | str):
        status (None | str): active, defunct, acquired or rebranded.
        series_count (int):
        logo_url (None | str):
        images (ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0 | None):
        name_i18n (ListAllPublishersWithOptionalSearchResponse200DataItemNameI18N): One name per language, keyed by BCP
            47 tag.
        aliases_i18n (ListAllPublishersWithOptionalSearchResponse200DataItemAliasesI18N): Alternative names per
            language.
        original_locale (None | str): The language the publisher is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    founded_year: int | None
    headquarters: None | str
    status: None | str
    series_count: int
    logo_url: None | str
    images: ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0 | None
    name_i18n: ListAllPublishersWithOptionalSearchResponse200DataItemNameI18N
    aliases_i18n: ListAllPublishersWithOptionalSearchResponse200DataItemAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_all_publishers_with_optional_search_response_200_data_item_images_type_0 import (
            ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        founded_year: int | None
        founded_year = self.founded_year

        headquarters: None | str
        headquarters = self.headquarters

        status: None | str
        status = self.status

        series_count = self.series_count

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0):
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
                "founded_year": founded_year,
                "headquarters": headquarters,
                "status": status,
                "series_count": series_count,
                "logo_url": logo_url,
                "images": images,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_publishers_with_optional_search_response_200_data_item_aliases_i18n import (
            ListAllPublishersWithOptionalSearchResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.list_all_publishers_with_optional_search_response_200_data_item_images_type_0 import (
            ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.list_all_publishers_with_optional_search_response_200_data_item_name_i18n import (
            ListAllPublishersWithOptionalSearchResponse200DataItemNameI18N,  # noqa: PLC0415
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

        def _parse_headquarters(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headquarters = _parse_headquarters(d.pop("headquarters"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        series_count = d.pop("series_count")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAllPublishersWithOptionalSearchResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        name_i18n = ListAllPublishersWithOptionalSearchResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListAllPublishersWithOptionalSearchResponse200DataItemAliasesI18N.from_dict(
            d.pop("aliases_i18n")
        )

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        list_all_publishers_with_optional_search_response_200_data_item = cls(
            id=id,
            name=name,
            founded_year=founded_year,
            headquarters=headquarters,
            status=status,
            series_count=series_count,
            logo_url=logo_url,
            images=images,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        list_all_publishers_with_optional_search_response_200_data_item.additional_properties = d
        return list_all_publishers_with_optional_search_response_200_data_item

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
