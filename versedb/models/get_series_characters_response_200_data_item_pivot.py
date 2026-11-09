from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSeriesCharactersResponse200DataItemPivot")


@_attrs_define
class GetSeriesCharactersResponse200DataItemPivot:
    """
    Attributes:
        series_id (int):
        character_id (int):
        created_at (None | str):
        updated_at (None | str):
    """

    series_id: int
    character_id: int
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_id = self.series_id

        character_id = self.character_id

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series_id": series_id,
                "character_id": character_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_id = d.pop("series_id")

        character_id = d.pop("character_id")

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

        get_series_characters_response_200_data_item_pivot = cls(
            series_id=series_id,
            character_id=character_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_series_characters_response_200_data_item_pivot.additional_properties = d
        return get_series_characters_response_200_data_item_pivot

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
