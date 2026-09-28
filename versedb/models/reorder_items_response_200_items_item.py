from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reorder_items_response_200_items_item_entity import ReorderItemsResponse200ItemsItemEntity


T = TypeVar("T", bound="ReorderItemsResponse200ItemsItem")


@_attrs_define
class ReorderItemsResponse200ItemsItem:
    """
    Attributes:
        id (int | Unset):
        position (int | Unset):
        note (None | str | Unset):
        entity_type (str | Unset):
        entity (ReorderItemsResponse200ItemsItemEntity | Unset):
    """

    id: int | Unset = UNSET
    position: int | Unset = UNSET
    note: None | str | Unset = UNSET
    entity_type: str | Unset = UNSET
    entity: ReorderItemsResponse200ItemsItemEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        entity_type = self.entity_type

        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if note is not UNSET:
            field_dict["note"] = note
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_items_response_200_items_item_entity import (
            ReorderItemsResponse200ItemsItemEntity,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        entity_type = d.pop("entity_type", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: ReorderItemsResponse200ItemsItemEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = ReorderItemsResponse200ItemsItemEntity.from_dict(_entity)

        reorder_items_response_200_items_item = cls(
            id=id,
            position=position,
            note=note,
            entity_type=entity_type,
            entity=entity,
        )

        reorder_items_response_200_items_item.additional_properties = d
        return reorder_items_response_200_items_item

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
