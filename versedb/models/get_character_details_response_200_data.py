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
    from ..models.get_character_details_response_200_data_images import GetCharacterDetailsResponse200DataImages
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
        id (int | Unset):
        name (str | Unset):
        name_i18n (GetCharacterDetailsResponse200DataNameI18N | Unset):
        real_name_i18n (GetCharacterDetailsResponse200DataRealNameI18N | Unset):
        aliases_i18n (GetCharacterDetailsResponse200DataAliasesI18N | Unset):
        original_locale (str | Unset):
        slug (str | Unset):
        real_name (str | Unset):
        aliases (list[str] | Unset):
        image_url (str | Unset):
        images (GetCharacterDetailsResponse200DataImages | Unset):
        alter_ego (list[Any] | Unset):
        gender (str | Unset):
        race (str | Unset):
        birth_place (str | Unset):
        occupation (str | Unset):
        appearances_count (int | Unset):
        series_count (int | Unset):
        teams_count (int | Unset):
        story_arcs_count (int | Unset):
        powers (list[str] | Unset):
        publisher (GetCharacterDetailsResponse200DataPublisher | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    name_i18n: GetCharacterDetailsResponse200DataNameI18N | Unset = UNSET
    real_name_i18n: GetCharacterDetailsResponse200DataRealNameI18N | Unset = UNSET
    aliases_i18n: GetCharacterDetailsResponse200DataAliasesI18N | Unset = UNSET
    original_locale: str | Unset = UNSET
    slug: str | Unset = UNSET
    real_name: str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetCharacterDetailsResponse200DataImages | Unset = UNSET
    alter_ego: list[Any] | Unset = UNSET
    gender: str | Unset = UNSET
    race: str | Unset = UNSET
    birth_place: str | Unset = UNSET
    occupation: str | Unset = UNSET
    appearances_count: int | Unset = UNSET
    series_count: int | Unset = UNSET
    teams_count: int | Unset = UNSET
    story_arcs_count: int | Unset = UNSET
    powers: list[str] | Unset = UNSET
    publisher: GetCharacterDetailsResponse200DataPublisher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_i18n, Unset):
            name_i18n = self.name_i18n.to_dict()

        real_name_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real_name_i18n, Unset):
            real_name_i18n = self.real_name_i18n.to_dict()

        aliases_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aliases_i18n, Unset):
            aliases_i18n = self.aliases_i18n.to_dict()

        original_locale = self.original_locale

        slug = self.slug

        real_name = self.real_name

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        alter_ego: list[Any] | Unset = UNSET
        if not isinstance(self.alter_ego, Unset):
            alter_ego = self.alter_ego

        gender = self.gender

        race = self.race

        birth_place = self.birth_place

        occupation = self.occupation

        appearances_count = self.appearances_count

        series_count = self.series_count

        teams_count = self.teams_count

        story_arcs_count = self.story_arcs_count

        powers: list[str] | Unset = UNSET
        if not isinstance(self.powers, Unset):
            powers = self.powers

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_i18n is not UNSET:
            field_dict["name_i18n"] = name_i18n
        if real_name_i18n is not UNSET:
            field_dict["real_name_i18n"] = real_name_i18n
        if aliases_i18n is not UNSET:
            field_dict["aliases_i18n"] = aliases_i18n
        if original_locale is not UNSET:
            field_dict["original_locale"] = original_locale
        if slug is not UNSET:
            field_dict["slug"] = slug
        if real_name is not UNSET:
            field_dict["real_name"] = real_name
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images
        if alter_ego is not UNSET:
            field_dict["alter_ego"] = alter_ego
        if gender is not UNSET:
            field_dict["gender"] = gender
        if race is not UNSET:
            field_dict["race"] = race
        if birth_place is not UNSET:
            field_dict["birth_place"] = birth_place
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if appearances_count is not UNSET:
            field_dict["appearances_count"] = appearances_count
        if series_count is not UNSET:
            field_dict["series_count"] = series_count
        if teams_count is not UNSET:
            field_dict["teams_count"] = teams_count
        if story_arcs_count is not UNSET:
            field_dict["story_arcs_count"] = story_arcs_count
        if powers is not UNSET:
            field_dict["powers"] = powers
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_character_details_response_200_data_aliases_i18n import (
            GetCharacterDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_character_details_response_200_data_images import GetCharacterDetailsResponse200DataImages  # noqa: PLC0415
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
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _name_i18n = d.pop("name_i18n", UNSET)
        name_i18n: GetCharacterDetailsResponse200DataNameI18N | Unset
        if isinstance(_name_i18n, Unset):
            name_i18n = UNSET
        else:
            name_i18n = GetCharacterDetailsResponse200DataNameI18N.from_dict(_name_i18n)

        _real_name_i18n = d.pop("real_name_i18n", UNSET)
        real_name_i18n: GetCharacterDetailsResponse200DataRealNameI18N | Unset
        if isinstance(_real_name_i18n, Unset):
            real_name_i18n = UNSET
        else:
            real_name_i18n = GetCharacterDetailsResponse200DataRealNameI18N.from_dict(_real_name_i18n)

        _aliases_i18n = d.pop("aliases_i18n", UNSET)
        aliases_i18n: GetCharacterDetailsResponse200DataAliasesI18N | Unset
        if isinstance(_aliases_i18n, Unset):
            aliases_i18n = UNSET
        else:
            aliases_i18n = GetCharacterDetailsResponse200DataAliasesI18N.from_dict(_aliases_i18n)

        original_locale = d.pop("original_locale", UNSET)

        slug = d.pop("slug", UNSET)

        real_name = d.pop("real_name", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetCharacterDetailsResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetCharacterDetailsResponse200DataImages.from_dict(_images)

        alter_ego = cast(list[Any], d.pop("alter_ego", UNSET))

        gender = d.pop("gender", UNSET)

        race = d.pop("race", UNSET)

        birth_place = d.pop("birth_place", UNSET)

        occupation = d.pop("occupation", UNSET)

        appearances_count = d.pop("appearances_count", UNSET)

        series_count = d.pop("series_count", UNSET)

        teams_count = d.pop("teams_count", UNSET)

        story_arcs_count = d.pop("story_arcs_count", UNSET)

        powers = cast(list[str], d.pop("powers", UNSET))

        _publisher = d.pop("publisher", UNSET)
        publisher: GetCharacterDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetCharacterDetailsResponse200DataPublisher.from_dict(_publisher)

        get_character_details_response_200_data = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            real_name_i18n=real_name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            slug=slug,
            real_name=real_name,
            aliases=aliases,
            image_url=image_url,
            images=images,
            alter_ego=alter_ego,
            gender=gender,
            race=race,
            birth_place=birth_place,
            occupation=occupation,
            appearances_count=appearances_count,
            series_count=series_count,
            teams_count=teams_count,
            story_arcs_count=story_arcs_count,
            powers=powers,
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
