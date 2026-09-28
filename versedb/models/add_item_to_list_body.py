from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddItemToListBody")


@_attrs_define
class AddItemToListBody:
    """
    Attributes:
        entity_id (int): The entity ID to add.
        entity_type (None | str | Unset): Required when the list holds any type: the type of the entity being added
            (issues, series, characters, creators, story_arcs, teams). Ignored on a single-type list.
        variant_id (int | None | Unset): Optional cover variant of the issue (issue items only, must belong to
            entity_id). Omit for "any cover".
        position (int | None | Unset): Position in list (auto-assigned if omitted).
        note (None | str | Unset): Personal note for this item (max 500 chars).
    """

    entity_id: int
    entity_type: None | str | Unset = UNSET
    variant_id: int | None | Unset = UNSET
    position: int | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        variant_id: int | None | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_id": entity_id,
            }
        )
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if position is not UNSET:
            field_dict["position"] = position
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entity_id")

        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

        def _parse_variant_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        add_item_to_list_body = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            variant_id=variant_id,
            position=position,
            note=note,
        )

        add_item_to_list_body.additional_properties = d
        return add_item_to_list_body

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
