from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_wishlist_response_200_data_item_entity import ListWishlistResponse200DataItemEntity


T = TypeVar("T", bound="ListWishlistResponse200DataItem")


@_attrs_define
class ListWishlistResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        position (None | str | Unset):
        note (None | str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
        variant_id (None | str | Unset):
        entity_type (str | Unset):
        entity (ListWishlistResponse200DataItemEntity | Unset):
    """

    id: int | Unset = UNSET
    position: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    variant_id: None | str | Unset = UNSET
    entity_type: str | Unset = UNSET
    entity: ListWishlistResponse200DataItemEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position: None | str | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        created_at = self.created_at

        updated_at = self.updated_at

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_wishlist_response_200_data_item_entity import ListWishlistResponse200DataItemEntity  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        entity_type = d.pop("entity_type", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: ListWishlistResponse200DataItemEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = ListWishlistResponse200DataItemEntity.from_dict(_entity)

        list_wishlist_response_200_data_item = cls(
            id=id,
            position=position,
            note=note,
            created_at=created_at,
            updated_at=updated_at,
            variant_id=variant_id,
            entity_type=entity_type,
            entity=entity,
        )

        list_wishlist_response_200_data_item.additional_properties = d
        return list_wishlist_response_200_data_item

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
