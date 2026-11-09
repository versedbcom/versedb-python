from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_series_creators_response_200_data_item_aliases_i18n import (
        GetSeriesCreatorsResponse200DataItemAliasesI18N,
    )
    from ..models.get_series_creators_response_200_data_item_links_type_0 import (
        GetSeriesCreatorsResponse200DataItemLinksType0,
    )
    from ..models.get_series_creators_response_200_data_item_name_i18n import (
        GetSeriesCreatorsResponse200DataItemNameI18N,
    )
    from ..models.get_series_creators_response_200_data_item_pivot import GetSeriesCreatorsResponse200DataItemPivot
    from ..models.get_series_creators_response_200_data_item_role_type_0 import (
        GetSeriesCreatorsResponse200DataItemRoleType0,
    )


T = TypeVar("T", bound="GetSeriesCreatorsResponse200DataItem")


@_attrs_define
class GetSeriesCreatorsResponse200DataItem:
    """
    Attributes:
        id (int):
        name (str):
        slug (str):
        role_id (int | None):
        profile_photo_path (None | str):
        biography (None | str):
        gender (None | str):
        birth (None | str):
        death (None | str):
        birth_place (None | str):
        country (None | str):
        links (GetSeriesCreatorsResponse200DataItemLinksType0 | None):
        created_at (None | str):
        updated_at (None | str):
        deleted_at (None | str):
        aliases (list[str] | None):
        cached_issues_count (int):
        cached_series_count (int):
        cached_titles_count (int):
        last_edited_by (int | None):
        last_edited_at (None | str):
        public_lists_count (int):
        original_locale (None | str):
        name_i18n (GetSeriesCreatorsResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetSeriesCreatorsResponse200DataItemAliasesI18N): Alternative names per language.
        role (GetSeriesCreatorsResponse200DataItemRoleType0 | None):
        pivot (GetSeriesCreatorsResponse200DataItemPivot):
    """

    id: int
    name: str
    slug: str
    role_id: int | None
    profile_photo_path: None | str
    biography: None | str
    gender: None | str
    birth: None | str
    death: None | str
    birth_place: None | str
    country: None | str
    links: GetSeriesCreatorsResponse200DataItemLinksType0 | None
    created_at: None | str
    updated_at: None | str
    deleted_at: None | str
    aliases: list[str] | None
    cached_issues_count: int
    cached_series_count: int
    cached_titles_count: int
    last_edited_by: int | None
    last_edited_at: None | str
    public_lists_count: int
    original_locale: None | str
    name_i18n: GetSeriesCreatorsResponse200DataItemNameI18N
    aliases_i18n: GetSeriesCreatorsResponse200DataItemAliasesI18N
    role: GetSeriesCreatorsResponse200DataItemRoleType0 | None
    pivot: GetSeriesCreatorsResponse200DataItemPivot
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_creators_response_200_data_item_links_type_0 import (
            GetSeriesCreatorsResponse200DataItemLinksType0,  # noqa: PLC0415
        )
        from ..models.get_series_creators_response_200_data_item_role_type_0 import (
            GetSeriesCreatorsResponse200DataItemRoleType0,  # noqa: PLC0415
        )

        id = self.id

        name = self.name

        slug = self.slug

        role_id: int | None
        role_id = self.role_id

        profile_photo_path: None | str
        profile_photo_path = self.profile_photo_path

        biography: None | str
        biography = self.biography

        gender: None | str
        gender = self.gender

        birth: None | str
        birth = self.birth

        death: None | str
        death = self.death

        birth_place: None | str
        birth_place = self.birth_place

        country: None | str
        country = self.country

        links: dict[str, Any] | None
        if isinstance(self.links, GetSeriesCreatorsResponse200DataItemLinksType0):
            links = self.links.to_dict()
        else:
            links = self.links

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        deleted_at: None | str
        deleted_at = self.deleted_at

        aliases: list[str] | None
        if isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        cached_issues_count = self.cached_issues_count

        cached_series_count = self.cached_series_count

        cached_titles_count = self.cached_titles_count

        last_edited_by: int | None
        last_edited_by = self.last_edited_by

        last_edited_at: None | str
        last_edited_at = self.last_edited_at

        public_lists_count = self.public_lists_count

        original_locale: None | str
        original_locale = self.original_locale

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        role: dict[str, Any] | None
        if isinstance(self.role, GetSeriesCreatorsResponse200DataItemRoleType0):
            role = self.role.to_dict()
        else:
            role = self.role

        pivot = self.pivot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "role_id": role_id,
                "profile_photo_path": profile_photo_path,
                "biography": biography,
                "gender": gender,
                "birth": birth,
                "death": death,
                "birth_place": birth_place,
                "country": country,
                "links": links,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "aliases": aliases,
                "cached_issues_count": cached_issues_count,
                "cached_series_count": cached_series_count,
                "cached_titles_count": cached_titles_count,
                "last_edited_by": last_edited_by,
                "last_edited_at": last_edited_at,
                "public_lists_count": public_lists_count,
                "original_locale": original_locale,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "role": role,
                "pivot": pivot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_creators_response_200_data_item_aliases_i18n import (
            GetSeriesCreatorsResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_series_creators_response_200_data_item_links_type_0 import (
            GetSeriesCreatorsResponse200DataItemLinksType0,  # noqa: PLC0415
        )
        from ..models.get_series_creators_response_200_data_item_name_i18n import (
            GetSeriesCreatorsResponse200DataItemNameI18N,  # noqa: PLC0415
        )
        from ..models.get_series_creators_response_200_data_item_pivot import GetSeriesCreatorsResponse200DataItemPivot  # noqa: PLC0415
        from ..models.get_series_creators_response_200_data_item_role_type_0 import (
            GetSeriesCreatorsResponse200DataItemRoleType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_role_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        role_id = _parse_role_id(d.pop("role_id"))

        def _parse_profile_photo_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_photo_path = _parse_profile_photo_path(d.pop("profile_photo_path"))

        def _parse_biography(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        biography = _parse_biography(d.pop("biography"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        def _parse_birth(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth = _parse_birth(d.pop("birth"))

        def _parse_death(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        death = _parse_death(d.pop("death"))

        def _parse_birth_place(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth_place = _parse_birth_place(d.pop("birth_place"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_links(data: object) -> GetSeriesCreatorsResponse200DataItemLinksType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                links_type_0 = GetSeriesCreatorsResponse200DataItemLinksType0.from_dict(data)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesCreatorsResponse200DataItemLinksType0 | None, data)

        links = _parse_links(d.pop("links"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        def _parse_aliases(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        aliases = _parse_aliases(d.pop("aliases"))

        cached_issues_count = d.pop("cached_issues_count")

        cached_series_count = d.pop("cached_series_count")

        cached_titles_count = d.pop("cached_titles_count")

        def _parse_last_edited_by(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_edited_by = _parse_last_edited_by(d.pop("last_edited_by"))

        def _parse_last_edited_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_edited_at = _parse_last_edited_at(d.pop("last_edited_at"))

        public_lists_count = d.pop("public_lists_count")

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        name_i18n = GetSeriesCreatorsResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetSeriesCreatorsResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_role(data: object) -> GetSeriesCreatorsResponse200DataItemRoleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_0 = GetSeriesCreatorsResponse200DataItemRoleType0.from_dict(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesCreatorsResponse200DataItemRoleType0 | None, data)

        role = _parse_role(d.pop("role"))

        pivot = GetSeriesCreatorsResponse200DataItemPivot.from_dict(d.pop("pivot"))

        get_series_creators_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            role_id=role_id,
            profile_photo_path=profile_photo_path,
            biography=biography,
            gender=gender,
            birth=birth,
            death=death,
            birth_place=birth_place,
            country=country,
            links=links,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            aliases=aliases,
            cached_issues_count=cached_issues_count,
            cached_series_count=cached_series_count,
            cached_titles_count=cached_titles_count,
            last_edited_by=last_edited_by,
            last_edited_at=last_edited_at,
            public_lists_count=public_lists_count,
            original_locale=original_locale,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            role=role,
            pivot=pivot,
        )

        get_series_creators_response_200_data_item.additional_properties = d
        return get_series_creators_response_200_data_item

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
