from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_list_response_200_data_items_item_entity import GetListResponse200DataItemsItemEntity
    from ..models.get_list_response_200_data_items_item_variant import GetListResponse200DataItemsItemVariant


T = TypeVar("T", bound="GetListResponse200DataItemsItem")


@_attrs_define
class GetListResponse200DataItemsItem:
    """
    Attributes:
        id (int | Unset):
        position (int | Unset):
        note (str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
        variant_id (int | Unset):
        variant (GetListResponse200DataItemsItemVariant | Unset):
        entity_type (str | Unset):
        entity (GetListResponse200DataItemsItemEntity | Unset):
    """

    id: int | Unset = UNSET
    position: int | Unset = UNSET
    note: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    variant_id: int | Unset = UNSET
    variant: GetListResponse200DataItemsItemVariant | Unset = UNSET
    entity_type: str | Unset = UNSET
    entity: GetListResponse200DataItemsItemEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position

        note = self.note

        created_at = self.created_at

        updated_at = self.updated_at

        variant_id = self.variant_id

        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

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
        if variant is not UNSET:
            field_dict["variant"] = variant
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_list_response_200_data_items_item_entity import GetListResponse200DataItemsItemEntity  # noqa: PLC0415
        from ..models.get_list_response_200_data_items_item_variant import GetListResponse200DataItemsItemVariant  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        note = d.pop("note", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        variant_id = d.pop("variant_id", UNSET)

        _variant = d.pop("variant", UNSET)
        variant: GetListResponse200DataItemsItemVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = GetListResponse200DataItemsItemVariant.from_dict(_variant)

        entity_type = d.pop("entity_type", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: GetListResponse200DataItemsItemEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = GetListResponse200DataItemsItemEntity.from_dict(_entity)

        get_list_response_200_data_items_item = cls(
            id=id,
            position=position,
            note=note,
            created_at=created_at,
            updated_at=updated_at,
            variant_id=variant_id,
            variant=variant,
            entity_type=entity_type,
            entity=entity,
        )

        get_list_response_200_data_items_item.additional_properties = d
        return get_list_response_200_data_items_item

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
