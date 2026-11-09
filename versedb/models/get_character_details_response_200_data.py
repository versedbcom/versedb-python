from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_character_details_response_200_data_aliases_i18n import (
        GetCharacterDetailsResponse200DataAliasesI18N,
    )
    from ..models.get_character_details_response_200_data_alter_ego_type_4 import (
        GetCharacterDetailsResponse200DataAlterEgoType4,
    )
    from ..models.get_character_details_response_200_data_images_type_0 import (
        GetCharacterDetailsResponse200DataImagesType0,
    )
    from ..models.get_character_details_response_200_data_name_i18n import GetCharacterDetailsResponse200DataNameI18N
    from ..models.get_character_details_response_200_data_publisher import GetCharacterDetailsResponse200DataPublisher
    from ..models.get_character_details_response_200_data_real_name_i18n import (
        GetCharacterDetailsResponse200DataRealNameI18N,
    )


T = TypeVar("T", bound="GetCharacterDetailsResponse200Data")


@_attrs_define
class GetCharacterDetailsResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        real_name (None | str):
        aliases (list[str] | None):
        image_url (None | str):
        images (GetCharacterDetailsResponse200DataImagesType0 | None):
        alter_ego (bool | float | GetCharacterDetailsResponse200DataAlterEgoType4 | list[Any] | None | str): Other
            identities, as stored: a list of strings in production.
        gender (None | str):
        birthday (None | str):
        race (None | str):
        birth_place (None | str):
        occupation (None | str):
        height (None | str):
        weight (None | str):
        citizenship (None | str):
        education (None | str):
        appearances_count (int):
        series_count (int):
        teams_count (int):
        story_arcs_count (int):
        name_i18n (GetCharacterDetailsResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetCharacterDetailsResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        real_name_i18n (GetCharacterDetailsResponse200DataRealNameI18N): One name per language, keyed by BCP 47 tag.
        eye_color (str | Unset): Present when the character has one.
        hair_color (str | Unset): Present when the character has one.
        powers (list[str] | Unset): Present when the character has one.
        weaknesses (list[str] | Unset): Present when the character has one.
        equipment (list[str] | Unset): Present when the character has one.
        abilities (list[str] | Unset): Present when the character has one.
        roles (list[str] | Unset): Present when the character has one.
        publisher (GetCharacterDetailsResponse200DataPublisher | Unset):
    """

    id: int
    name: None | str
    slug: None | str
    real_name: None | str
    aliases: list[str] | None
    image_url: None | str
    images: GetCharacterDetailsResponse200DataImagesType0 | None
    alter_ego: bool | float | GetCharacterDetailsResponse200DataAlterEgoType4 | list[Any] | None | str
    gender: None | str
    birthday: None | str
    race: None | str
    birth_place: None | str
    occupation: None | str
    height: None | str
    weight: None | str
    citizenship: None | str
    education: None | str
    appearances_count: int
    series_count: int
    teams_count: int
    story_arcs_count: int
    name_i18n: GetCharacterDetailsResponse200DataNameI18N
    aliases_i18n: GetCharacterDetailsResponse200DataAliasesI18N
    original_locale: None | str
    real_name_i18n: GetCharacterDetailsResponse200DataRealNameI18N
    eye_color: str | Unset = UNSET
    hair_color: str | Unset = UNSET
    powers: list[str] | Unset = UNSET
    weaknesses: list[str] | Unset = UNSET
    equipment: list[str] | Unset = UNSET
    abilities: list[str] | Unset = UNSET
    roles: list[str] | Unset = UNSET
    publisher: GetCharacterDetailsResponse200DataPublisher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_character_details_response_200_data_alter_ego_type_4 import (
            GetCharacterDetailsResponse200DataAlterEgoType4,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_images_type_0 import (
            GetCharacterDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        real_name: None | str
        real_name = self.real_name

        aliases: list[str] | None
        if isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetCharacterDetailsResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        alter_ego: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.alter_ego, list):
            alter_ego = self.alter_ego

        elif isinstance(self.alter_ego, GetCharacterDetailsResponse200DataAlterEgoType4):
            alter_ego = self.alter_ego.to_dict()
        else:
            alter_ego = self.alter_ego

        gender: None | str
        gender = self.gender

        birthday: None | str
        birthday = self.birthday

        race: None | str
        race = self.race

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

        appearances_count = self.appearances_count

        series_count = self.series_count

        teams_count = self.teams_count

        story_arcs_count = self.story_arcs_count

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        real_name_i18n = self.real_name_i18n.to_dict()

        eye_color = self.eye_color

        hair_color = self.hair_color

        powers: list[str] | Unset = UNSET
        if not isinstance(self.powers, Unset):
            powers = self.powers

        weaknesses: list[str] | Unset = UNSET
        if not isinstance(self.weaknesses, Unset):
            weaknesses = self.weaknesses

        equipment: list[str] | Unset = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment

        abilities: list[str] | Unset = UNSET
        if not isinstance(self.abilities, Unset):
            abilities = self.abilities

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "real_name": real_name,
                "aliases": aliases,
                "image_url": image_url,
                "images": images,
                "alter_ego": alter_ego,
                "gender": gender,
                "birthday": birthday,
                "race": race,
                "birth_place": birth_place,
                "occupation": occupation,
                "height": height,
                "weight": weight,
                "citizenship": citizenship,
                "education": education,
                "appearances_count": appearances_count,
                "series_count": series_count,
                "teams_count": teams_count,
                "story_arcs_count": story_arcs_count,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "real_name_i18n": real_name_i18n,
            }
        )
        if eye_color is not UNSET:
            field_dict["eye_color"] = eye_color
        if hair_color is not UNSET:
            field_dict["hair_color"] = hair_color
        if powers is not UNSET:
            field_dict["powers"] = powers
        if weaknesses is not UNSET:
            field_dict["weaknesses"] = weaknesses
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if abilities is not UNSET:
            field_dict["abilities"] = abilities
        if roles is not UNSET:
            field_dict["roles"] = roles
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_character_details_response_200_data_aliases_i18n import (
            GetCharacterDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_alter_ego_type_4 import (
            GetCharacterDetailsResponse200DataAlterEgoType4,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_images_type_0 import (
            GetCharacterDetailsResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_name_i18n import (
            GetCharacterDetailsResponse200DataNameI18N,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_publisher import (
            GetCharacterDetailsResponse200DataPublisher,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_real_name_i18n import (
            GetCharacterDetailsResponse200DataRealNameI18N,  # noqa: PLC0415
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

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> GetCharacterDetailsResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetCharacterDetailsResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCharacterDetailsResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_alter_ego(
            data: object,
        ) -> bool | float | GetCharacterDetailsResponse200DataAlterEgoType4 | list[Any] | None | str:
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
                alter_ego_type_4 = GetCharacterDetailsResponse200DataAlterEgoType4.from_dict(data)

                return alter_ego_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetCharacterDetailsResponse200DataAlterEgoType4 | list[Any] | None | str, data)

        alter_ego = _parse_alter_ego(d.pop("alter_ego"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        def _parse_birthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthday = _parse_birthday(d.pop("birthday"))

        def _parse_race(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        race = _parse_race(d.pop("race"))

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

        appearances_count = d.pop("appearances_count")

        series_count = d.pop("series_count")

        teams_count = d.pop("teams_count")

        story_arcs_count = d.pop("story_arcs_count")

        name_i18n = GetCharacterDetailsResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetCharacterDetailsResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        real_name_i18n = GetCharacterDetailsResponse200DataRealNameI18N.from_dict(d.pop("real_name_i18n"))

        eye_color = d.pop("eye_color", UNSET)

        hair_color = d.pop("hair_color", UNSET)

        powers = cast(list[str], d.pop("powers", UNSET))

        weaknesses = cast(list[str], d.pop("weaknesses", UNSET))

        equipment = cast(list[str], d.pop("equipment", UNSET))

        abilities = cast(list[str], d.pop("abilities", UNSET))

        roles = cast(list[str], d.pop("roles", UNSET))

        _publisher = d.pop("publisher", UNSET)
        publisher: GetCharacterDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetCharacterDetailsResponse200DataPublisher.from_dict(_publisher)

        get_character_details_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            real_name=real_name,
            aliases=aliases,
            image_url=image_url,
            images=images,
            alter_ego=alter_ego,
            gender=gender,
            birthday=birthday,
            race=race,
            birth_place=birth_place,
            occupation=occupation,
            height=height,
            weight=weight,
            citizenship=citizenship,
            education=education,
            appearances_count=appearances_count,
            series_count=series_count,
            teams_count=teams_count,
            story_arcs_count=story_arcs_count,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            real_name_i18n=real_name_i18n,
            eye_color=eye_color,
            hair_color=hair_color,
            powers=powers,
            weaknesses=weaknesses,
            equipment=equipment,
            abilities=abilities,
            roles=roles,
            publisher=publisher,
        )

        get_character_details_response_200_data.additional_properties = d
        return get_character_details_response_200_data

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
