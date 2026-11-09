from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_a_specific_title_response_200_data_aliases_i18n import GetASpecificTitleResponse200DataAliasesI18N
    from ..models.get_a_specific_title_response_200_data_aliases_type_4 import (
        GetASpecificTitleResponse200DataAliasesType4,
    )
    from ..models.get_a_specific_title_response_200_data_images_type_0 import (
        GetASpecificTitleResponse200DataImagesType0,
    )
    from ..models.get_a_specific_title_response_200_data_name_i18n import GetASpecificTitleResponse200DataNameI18N


T = TypeVar("T", bound="GetASpecificTitleResponse200Data")


@_attrs_define
class GetASpecificTitleResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        start_year (int | None):
        end_year (int | None):
        status (None | str):
        type_ (None | str):
        image_url (None | str):
        images (GetASpecificTitleResponse200DataImagesType0 | None):
        content_rating_label (None | str):
        min_age (int | None):
        is_nsfw (bool | None):
        imprint_id (int | None):
        series_count (int | None):
        issues_count (int | None):
        average_rating (None | str):
        aliases (bool | float | GetASpecificTitleResponse200DataAliasesType4 | list[Any] | None | str): The other names,
            as stored: a list of strings in production.
        name_i18n (GetASpecificTitleResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetASpecificTitleResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the title is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    start_year: int | None
    end_year: int | None
    status: None | str
    type_: None | str
    image_url: None | str
    images: GetASpecificTitleResponse200DataImagesType0 | None
    content_rating_label: None | str
    min_age: int | None
    is_nsfw: bool | None
    imprint_id: int | None
    series_count: int | None
    issues_count: int | None
    average_rating: None | str
    aliases: bool | float | GetASpecificTitleResponse200DataAliasesType4 | list[Any] | None | str
    name_i18n: GetASpecificTitleResponse200DataNameI18N
    aliases_i18n: GetASpecificTitleResponse200DataAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_a_specific_title_response_200_data_aliases_type_4 import (
            GetASpecificTitleResponse200DataAliasesType4,  # noqa: PLC0415
        )
        from ..models.get_a_specific_title_response_200_data_images_type_0 import (
            GetASpecificTitleResponse200DataImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        start_year: int | None
        start_year = self.start_year

        end_year: int | None
        end_year = self.end_year

        status: None | str
        status = self.status

        type_: None | str
        type_ = self.type_

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetASpecificTitleResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        imprint_id: int | None
        imprint_id = self.imprint_id

        series_count: int | None
        series_count = self.series_count

        issues_count: int | None
        issues_count = self.issues_count

        average_rating: None | str
        average_rating = self.average_rating

        aliases: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.aliases, list):
            aliases = self.aliases

        elif isinstance(self.aliases, GetASpecificTitleResponse200DataAliasesType4):
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
                "slug": slug,
                "start_year": start_year,
                "end_year": end_year,
                "status": status,
                "type": type_,
                "image_url": image_url,
                "images": images,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "is_nsfw": is_nsfw,
                "imprint_id": imprint_id,
                "series_count": series_count,
                "issues_count": issues_count,
                "average_rating": average_rating,
                "aliases": aliases,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_title_response_200_data_aliases_i18n import (
            GetASpecificTitleResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_a_specific_title_response_200_data_aliases_type_4 import (
            GetASpecificTitleResponse200DataAliasesType4,  # noqa: PLC0415
        )
        from ..models.get_a_specific_title_response_200_data_images_type_0 import (
            GetASpecificTitleResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_title_response_200_data_name_i18n import GetASpecificTitleResponse200DataNameI18N  # noqa: PLC0415

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

        def _parse_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        start_year = _parse_start_year(d.pop("start_year"))

        def _parse_end_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        end_year = _parse_end_year(d.pop("end_year"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> GetASpecificTitleResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetASpecificTitleResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetASpecificTitleResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_content_rating_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_rating_label = _parse_content_rating_label(d.pop("content_rating_label"))

        def _parse_min_age(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_age = _parse_min_age(d.pop("min_age"))

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_imprint_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        imprint_id = _parse_imprint_id(d.pop("imprint_id"))

        def _parse_series_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_count = _parse_series_count(d.pop("series_count"))

        def _parse_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issues_count = _parse_issues_count(d.pop("issues_count"))

        def _parse_average_rating(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        average_rating = _parse_average_rating(d.pop("average_rating"))

        def _parse_aliases(
            data: object,
        ) -> bool | float | GetASpecificTitleResponse200DataAliasesType4 | list[Any] | None | str:
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
                aliases_type_4 = GetASpecificTitleResponse200DataAliasesType4.from_dict(data)

                return aliases_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetASpecificTitleResponse200DataAliasesType4 | list[Any] | None | str, data)

        aliases = _parse_aliases(d.pop("aliases"))

        name_i18n = GetASpecificTitleResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetASpecificTitleResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        get_a_specific_title_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
            end_year=end_year,
            status=status,
            type_=type_,
            image_url=image_url,
            images=images,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            imprint_id=imprint_id,
            series_count=series_count,
            issues_count=issues_count,
            average_rating=average_rating,
            aliases=aliases,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        get_a_specific_title_response_200_data.additional_properties = d
        return get_a_specific_title_response_200_data

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
