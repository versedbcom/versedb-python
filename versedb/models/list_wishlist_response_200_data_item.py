from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_wishlist_response_200_data_item_entity import ListWishlistResponse200DataItemEntity
    from ..models.list_wishlist_response_200_data_item_variant import ListWishlistResponse200DataItemVariant


T = TypeVar("T", bound="ListWishlistResponse200DataItem")


@_attrs_define
class ListWishlistResponse200DataItem:
    """
    Attributes:
        id (int):
        position (int | None):
        created_at (str):
        updated_at (str):
        variant_id (int | None):
        entity_type (str):
        note (None | str | Unset): Left out for a `read:showcase` token.
        variant (ListWishlistResponse200DataItemVariant | Unset): The pinned cover, while it exists.
        entity (ListWishlistResponse200DataItemEntity | Unset): Left out once the issue is gone.
    """

    id: int
    position: int | None
    created_at: str
    updated_at: str
    variant_id: int | None
    entity_type: str
    note: None | str | Unset = UNSET
    variant: ListWishlistResponse200DataItemVariant | Unset = UNSET
    entity: ListWishlistResponse200DataItemEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position: int | None
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        variant_id: int | None
        variant_id = self.variant_id

        entity_type = self.entity_type

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
                "variant_id": variant_id,
                "entity_type": entity_type,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if variant is not UNSET:
            field_dict["variant"] = variant
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_wishlist_response_200_data_item_entity import ListWishlistResponse200DataItemEntity  # noqa: PLC0415
        from ..models.list_wishlist_response_200_data_item_variant import ListWishlistResponse200DataItemVariant  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        entity_type = d.pop("entity_type")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _variant = d.pop("variant", UNSET)
        variant: ListWishlistResponse200DataItemVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = ListWishlistResponse200DataItemVariant.from_dict(_variant)

        _entity = d.pop("entity", UNSET)
        entity: ListWishlistResponse200DataItemEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = ListWishlistResponse200DataItemEntity.from_dict(_entity)

        list_wishlist_response_200_data_item = cls(
            id=id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            variant_id=variant_id,
            entity_type=entity_type,
            note=note,
            variant=variant,
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
