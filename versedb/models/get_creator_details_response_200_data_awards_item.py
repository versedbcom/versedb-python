from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_creator_details_response_200_data_awards_item_aliases_i18n import (
        GetCreatorDetailsResponse200DataAwardsItemAliasesI18N,
    )
    from ..models.get_creator_details_response_200_data_awards_item_name_i18n import (
        GetCreatorDetailsResponse200DataAwardsItemNameI18N,
    )


T = TypeVar("T", bound="GetCreatorDetailsResponse200DataAwardsItem")


@_attrs_define
class GetCreatorDetailsResponse200DataAwardsItem:
    """
    Attributes:
        name (None | str):
        name_i18n (GetCreatorDetailsResponse200DataAwardsItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetCreatorDetailsResponse200DataAwardsItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        year (int | None):
    """

    name: None | str
    name_i18n: GetCreatorDetailsResponse200DataAwardsItemNameI18N
    aliases_i18n: GetCreatorDetailsResponse200DataAwardsItemAliasesI18N
    original_locale: None | str
    year: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        year: int | None
        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_details_response_200_data_awards_item_aliases_i18n import (
            GetCreatorDetailsResponse200DataAwardsItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_creator_details_response_200_data_awards_item_name_i18n import (
            GetCreatorDetailsResponse200DataAwardsItemNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_i18n = GetCreatorDetailsResponse200DataAwardsItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetCreatorDetailsResponse200DataAwardsItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        def _parse_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        year = _parse_year(d.pop("year"))

        get_creator_details_response_200_data_awards_item = cls(
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            year=year,
        )

        get_creator_details_response_200_data_awards_item.additional_properties = d
        return get_creator_details_response_200_data_awards_item

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
