from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_universes_response_200_data_item_aliases_i18n import ListUniversesResponse200DataItemAliasesI18N
    from ..models.list_universes_response_200_data_item_name_i18n import ListUniversesResponse200DataItemNameI18N


T = TypeVar("T", bound="ListUniversesResponse200DataItem")


@_attrs_define
class ListUniversesResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        name_i18n (ListUniversesResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (ListUniversesResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the universe is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    name_i18n: ListUniversesResponse200DataItemNameI18N
    aliases_i18n: ListUniversesResponse200DataItemAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

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
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_universes_response_200_data_item_aliases_i18n import (
            ListUniversesResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.list_universes_response_200_data_item_name_i18n import ListUniversesResponse200DataItemNameI18N  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_i18n = ListUniversesResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListUniversesResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        list_universes_response_200_data_item = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        list_universes_response_200_data_item.additional_properties = d
        return list_universes_response_200_data_item

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
