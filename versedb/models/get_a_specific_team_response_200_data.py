from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_a_specific_team_response_200_data_aliases_i18n import GetASpecificTeamResponse200DataAliasesI18N
    from ..models.get_a_specific_team_response_200_data_images_type_0 import GetASpecificTeamResponse200DataImagesType0
    from ..models.get_a_specific_team_response_200_data_name_i18n import GetASpecificTeamResponse200DataNameI18N


T = TypeVar("T", bound="GetASpecificTeamResponse200Data")


@_attrs_define
class GetASpecificTeamResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        aliases (list[str]):
        formation_date (None | str):
        disbanded_date (None | str):
        headquarters (None | str):
        members_count (int):
        series_count (int):
        appearances_count (int):
        lists_count (int):
        image_url (None | str):
        images (GetASpecificTeamResponse200DataImagesType0 | None):
        name_i18n (GetASpecificTeamResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetASpecificTeamResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    aliases: list[str]
    formation_date: None | str
    disbanded_date: None | str
    headquarters: None | str
    members_count: int
    series_count: int
    appearances_count: int
    lists_count: int
    image_url: None | str
    images: GetASpecificTeamResponse200DataImagesType0 | None
    name_i18n: GetASpecificTeamResponse200DataNameI18N
    aliases_i18n: GetASpecificTeamResponse200DataAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_a_specific_team_response_200_data_images_type_0 import (
            GetASpecificTeamResponse200DataImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        aliases = self.aliases

        formation_date: None | str
        formation_date = self.formation_date

        disbanded_date: None | str
        disbanded_date = self.disbanded_date

        headquarters: None | str
        headquarters = self.headquarters

        members_count = self.members_count

        series_count = self.series_count

        appearances_count = self.appearances_count

        lists_count = self.lists_count

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetASpecificTeamResponse200DataImagesType0):
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
                "slug": slug,
                "aliases": aliases,
                "formation_date": formation_date,
                "disbanded_date": disbanded_date,
                "headquarters": headquarters,
                "members_count": members_count,
                "series_count": series_count,
                "appearances_count": appearances_count,
                "lists_count": lists_count,
                "image_url": image_url,
                "images": images,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_team_response_200_data_aliases_i18n import (
            GetASpecificTeamResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_a_specific_team_response_200_data_images_type_0 import (
            GetASpecificTeamResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_a_specific_team_response_200_data_name_i18n import GetASpecificTeamResponse200DataNameI18N  # noqa: PLC0415

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

        aliases = cast(list[str], d.pop("aliases"))

        def _parse_formation_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formation_date = _parse_formation_date(d.pop("formation_date"))

        def _parse_disbanded_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        disbanded_date = _parse_disbanded_date(d.pop("disbanded_date"))

        def _parse_headquarters(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headquarters = _parse_headquarters(d.pop("headquarters"))

        members_count = d.pop("members_count")

        series_count = d.pop("series_count")

        appearances_count = d.pop("appearances_count")

        lists_count = d.pop("lists_count")

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> GetASpecificTeamResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetASpecificTeamResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetASpecificTeamResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        name_i18n = GetASpecificTeamResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetASpecificTeamResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        get_a_specific_team_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            aliases=aliases,
            formation_date=formation_date,
            disbanded_date=disbanded_date,
            headquarters=headquarters,
            members_count=members_count,
            series_count=series_count,
            appearances_count=appearances_count,
            lists_count=lists_count,
            image_url=image_url,
            images=images,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        get_a_specific_team_response_200_data.additional_properties = d
        return get_a_specific_team_response_200_data

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
