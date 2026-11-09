from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_series_characters_response_200_data_item_aliases_i18n import (
        GetSeriesCharactersResponse200DataItemAliasesI18N,
    )
    from ..models.get_series_characters_response_200_data_item_alter_ego_type_4 import (
        GetSeriesCharactersResponse200DataItemAlterEgoType4,
    )
    from ..models.get_series_characters_response_200_data_item_name_i18n import (
        GetSeriesCharactersResponse200DataItemNameI18N,
    )
    from ..models.get_series_characters_response_200_data_item_pivot import GetSeriesCharactersResponse200DataItemPivot
    from ..models.get_series_characters_response_200_data_item_real_name_i18n import (
        GetSeriesCharactersResponse200DataItemRealNameI18N,
    )
    from ..models.get_series_characters_response_200_data_item_tags_item import (
        GetSeriesCharactersResponse200DataItemTagsItem,
    )


T = TypeVar("T", bound="GetSeriesCharactersResponse200DataItem")


@_attrs_define
class GetSeriesCharactersResponse200DataItem:
    """
    Attributes:
        id (int):
        name (str):
        slug (str):
        real_name (None | str):
        description (None | str):
        alter_ego (bool | float | GetSeriesCharactersResponse200DataItemAlterEgoType4 | list[Any] | None | str): Other
            identities, as stored: a list of strings in production.
        birthday (None | str):
        birth_place (None | str):
        occupation (None | str):
        height (None | str):
        weight (None | str):
        citizenship (None | str):
        education (None | str):
        aliases (list[str] | None):
        profile_photo_path (None | str):
        gender (None | str):
        created_at (None | str):
        updated_at (None | str):
        deleted_at (None | str):
        last_edited_by (int | None):
        last_edited_at (None | str):
        public_lists_count (int):
        debut_date (None | str):
        debut_issue_id (int | None):
        debut_editorial (bool):
        original_locale (None | str):
        name_i18n (GetSeriesCharactersResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetSeriesCharactersResponse200DataItemAliasesI18N): Alternative names per language.
        real_name_i18n (GetSeriesCharactersResponse200DataItemRealNameI18N): One name per language, keyed by BCP 47 tag.
        race (None | str):
        tags (list[GetSeriesCharactersResponse200DataItemTagsItem]):
        pivot (GetSeriesCharactersResponse200DataItemPivot):
    """

    id: int
    name: str
    slug: str
    real_name: None | str
    description: None | str
    alter_ego: bool | float | GetSeriesCharactersResponse200DataItemAlterEgoType4 | list[Any] | None | str
    birthday: None | str
    birth_place: None | str
    occupation: None | str
    height: None | str
    weight: None | str
    citizenship: None | str
    education: None | str
    aliases: list[str] | None
    profile_photo_path: None | str
    gender: None | str
    created_at: None | str
    updated_at: None | str
    deleted_at: None | str
    last_edited_by: int | None
    last_edited_at: None | str
    public_lists_count: int
    debut_date: None | str
    debut_issue_id: int | None
    debut_editorial: bool
    original_locale: None | str
    name_i18n: GetSeriesCharactersResponse200DataItemNameI18N
    aliases_i18n: GetSeriesCharactersResponse200DataItemAliasesI18N
    real_name_i18n: GetSeriesCharactersResponse200DataItemRealNameI18N
    race: None | str
    tags: list[GetSeriesCharactersResponse200DataItemTagsItem]
    pivot: GetSeriesCharactersResponse200DataItemPivot
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_characters_response_200_data_item_alter_ego_type_4 import (
            GetSeriesCharactersResponse200DataItemAlterEgoType4,  # noqa: PLC0415
        )

        id = self.id

        name = self.name

        slug = self.slug

        real_name: None | str
        real_name = self.real_name

        description: None | str
        description = self.description

        alter_ego: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.alter_ego, list):
            alter_ego = self.alter_ego

        elif isinstance(self.alter_ego, GetSeriesCharactersResponse200DataItemAlterEgoType4):
            alter_ego = self.alter_ego.to_dict()
        else:
            alter_ego = self.alter_ego

        birthday: None | str
        birthday = self.birthday

        birth_place: None | str
        birth_place = self.birth_place

        occupation: None | str
        occupation = self.occupation

        height: None | str
        height = self.height

        weight: None | str
        weight = self.weight

        citizenship: None | str
        citizenship = self.citizenship

        education: None | str
        education = self.education

        aliases: list[str] | None
        if isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        profile_photo_path: None | str
        profile_photo_path = self.profile_photo_path

        gender: None | str
        gender = self.gender

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        deleted_at: None | str
        deleted_at = self.deleted_at

        last_edited_by: int | None
        last_edited_by = self.last_edited_by

        last_edited_at: None | str
        last_edited_at = self.last_edited_at

        public_lists_count = self.public_lists_count

        debut_date: None | str
        debut_date = self.debut_date

        debut_issue_id: int | None
        debut_issue_id = self.debut_issue_id

        debut_editorial = self.debut_editorial

        original_locale: None | str
        original_locale = self.original_locale

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        real_name_i18n = self.real_name_i18n.to_dict()

        race: None | str
        race = self.race

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        pivot = self.pivot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "real_name": real_name,
                "description": description,
                "alter_ego": alter_ego,
                "birthday": birthday,
                "birth_place": birth_place,
                "occupation": occupation,
                "height": height,
                "weight": weight,
                "citizenship": citizenship,
                "education": education,
                "aliases": aliases,
                "profile_photo_path": profile_photo_path,
                "gender": gender,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "last_edited_by": last_edited_by,
                "last_edited_at": last_edited_at,
                "public_lists_count": public_lists_count,
                "debut_date": debut_date,
                "debut_issue_id": debut_issue_id,
                "debut_editorial": debut_editorial,
                "original_locale": original_locale,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "real_name_i18n": real_name_i18n,
                "race": race,
                "tags": tags,
                "pivot": pivot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_characters_response_200_data_item_aliases_i18n import (
            GetSeriesCharactersResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_series_characters_response_200_data_item_alter_ego_type_4 import (
            GetSeriesCharactersResponse200DataItemAlterEgoType4,  # noqa: PLC0415
        )
        from ..models.get_series_characters_response_200_data_item_name_i18n import (
            GetSeriesCharactersResponse200DataItemNameI18N,  # noqa: PLC0415
        )
        from ..models.get_series_characters_response_200_data_item_pivot import (
            GetSeriesCharactersResponse200DataItemPivot,  # noqa: PLC0415
        )
        from ..models.get_series_characters_response_200_data_item_real_name_i18n import (
            GetSeriesCharactersResponse200DataItemRealNameI18N,  # noqa: PLC0415
        )
        from ..models.get_series_characters_response_200_data_item_tags_item import (
            GetSeriesCharactersResponse200DataItemTagsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_real_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        real_name = _parse_real_name(d.pop("real_name"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_alter_ego(
            data: object,
        ) -> bool | float | GetSeriesCharactersResponse200DataItemAlterEgoType4 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alter_ego_type_3 = cast(list[Any], data)

                return alter_ego_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alter_ego_type_4 = GetSeriesCharactersResponse200DataItemAlterEgoType4.from_dict(data)

                return alter_ego_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool | float | GetSeriesCharactersResponse200DataItemAlterEgoType4 | list[Any] | None | str, data
            )

        alter_ego = _parse_alter_ego(d.pop("alter_ego"))

        def _parse_birthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthday = _parse_birthday(d.pop("birthday"))

        def _parse_birth_place(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth_place = _parse_birth_place(d.pop("birth_place"))

        def _parse_occupation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        occupation = _parse_occupation(d.pop("occupation"))

        def _parse_height(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        height = _parse_height(d.pop("height"))

        def _parse_weight(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        weight = _parse_weight(d.pop("weight"))

        def _parse_citizenship(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        citizenship = _parse_citizenship(d.pop("citizenship"))

        def _parse_education(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        education = _parse_education(d.pop("education"))

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

        def _parse_profile_photo_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_photo_path = _parse_profile_photo_path(d.pop("profile_photo_path"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

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

        def _parse_debut_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        debut_date = _parse_debut_date(d.pop("debut_date"))

        def _parse_debut_issue_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        debut_issue_id = _parse_debut_issue_id(d.pop("debut_issue_id"))

        debut_editorial = d.pop("debut_editorial")

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        name_i18n = GetSeriesCharactersResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetSeriesCharactersResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        real_name_i18n = GetSeriesCharactersResponse200DataItemRealNameI18N.from_dict(d.pop("real_name_i18n"))

        def _parse_race(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        race = _parse_race(d.pop("race"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = GetSeriesCharactersResponse200DataItemTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        pivot = GetSeriesCharactersResponse200DataItemPivot.from_dict(d.pop("pivot"))

        get_series_characters_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            real_name=real_name,
            description=description,
            alter_ego=alter_ego,
            birthday=birthday,
            birth_place=birth_place,
            occupation=occupation,
            height=height,
            weight=weight,
            citizenship=citizenship,
            education=education,
            aliases=aliases,
            profile_photo_path=profile_photo_path,
            gender=gender,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            last_edited_by=last_edited_by,
            last_edited_at=last_edited_at,
            public_lists_count=public_lists_count,
            debut_date=debut_date,
            debut_issue_id=debut_issue_id,
            debut_editorial=debut_editorial,
            original_locale=original_locale,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            real_name_i18n=real_name_i18n,
            race=race,
            tags=tags,
            pivot=pivot,
        )

        get_series_characters_response_200_data_item.additional_properties = d
        return get_series_characters_response_200_data_item

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
