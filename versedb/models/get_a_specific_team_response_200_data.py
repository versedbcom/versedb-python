from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_a_specific_team_response_200_data_images import GetASpecificTeamResponse200DataImages


T = TypeVar("T", bound="GetASpecificTeamResponse200Data")


@_attrs_define
class GetASpecificTeamResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        aliases (list[str] | Unset):
        formation_date (str | Unset):
        disbanded_date (None | str | Unset):
        headquarters (str | Unset):
        members_count (int | Unset):
        series_count (int | Unset):
        appearances_count (int | Unset):
        lists_count (int | Unset):
        image_url (str | Unset):
        images (GetASpecificTeamResponse200DataImages | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    formation_date: str | Unset = UNSET
    disbanded_date: None | str | Unset = UNSET
    headquarters: str | Unset = UNSET
    members_count: int | Unset = UNSET
    series_count: int | Unset = UNSET
    appearances_count: int | Unset = UNSET
    lists_count: int | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetASpecificTeamResponse200DataImages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        formation_date = self.formation_date

        disbanded_date: None | str | Unset
        if isinstance(self.disbanded_date, Unset):
            disbanded_date = UNSET
        else:
            disbanded_date = self.disbanded_date

        headquarters = self.headquarters

        members_count = self.members_count

        series_count = self.series_count

        appearances_count = self.appearances_count

        lists_count = self.lists_count

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if formation_date is not UNSET:
            field_dict["formation_date"] = formation_date
        if disbanded_date is not UNSET:
            field_dict["disbanded_date"] = disbanded_date
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if members_count is not UNSET:
            field_dict["members_count"] = members_count
        if series_count is not UNSET:
            field_dict["series_count"] = series_count
        if appearances_count is not UNSET:
            field_dict["appearances_count"] = appearances_count
        if lists_count is not UNSET:
            field_dict["lists_count"] = lists_count
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_specific_team_response_200_data_images import GetASpecificTeamResponse200DataImages  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        formation_date = d.pop("formation_date", UNSET)

        def _parse_disbanded_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disbanded_date = _parse_disbanded_date(d.pop("disbanded_date", UNSET))

        headquarters = d.pop("headquarters", UNSET)

        members_count = d.pop("members_count", UNSET)

        series_count = d.pop("series_count", UNSET)

        appearances_count = d.pop("appearances_count", UNSET)

        lists_count = d.pop("lists_count", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetASpecificTeamResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetASpecificTeamResponse200DataImages.from_dict(_images)

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
