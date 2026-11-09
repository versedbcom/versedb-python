from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reorder_items_response_200_items_item_entity_type_0 import ReorderItemsResponse200ItemsItemEntityType0
    from ..models.reorder_items_response_200_items_item_entity_type_1 import ReorderItemsResponse200ItemsItemEntityType1
    from ..models.reorder_items_response_200_items_item_entity_type_2 import ReorderItemsResponse200ItemsItemEntityType2
    from ..models.reorder_items_response_200_items_item_entity_type_3 import ReorderItemsResponse200ItemsItemEntityType3
    from ..models.reorder_items_response_200_items_item_entity_type_4 import ReorderItemsResponse200ItemsItemEntityType4
    from ..models.reorder_items_response_200_items_item_variant import ReorderItemsResponse200ItemsItemVariant


T = TypeVar("T", bound="ReorderItemsResponse200ItemsItem")


@_attrs_define
class ReorderItemsResponse200ItemsItem:
    """
    Attributes:
        id (int):
        position (int | None): Its place on a ranked or rule-built list.
        note (None | str):
        created_at (str):
        updated_at (str):
        variant_id (int | None):
        entity_type (str): issues, series, characters, creators, story_arcs or teams.
        variant (ReorderItemsResponse200ItemsItemVariant | Unset): The pinned cover, while it exists.
        entity (ReorderItemsResponse200ItemsItemEntityType0 | ReorderItemsResponse200ItemsItemEntityType1 |
            ReorderItemsResponse200ItemsItemEntityType2 | ReorderItemsResponse200ItemsItemEntityType3 |
            ReorderItemsResponse200ItemsItemEntityType4 | Unset): Left out once the entity is gone.
    """

    id: int
    position: int | None
    note: None | str
    created_at: str
    updated_at: str
    variant_id: int | None
    entity_type: str
    variant: ReorderItemsResponse200ItemsItemVariant | Unset = UNSET
    entity: (
        ReorderItemsResponse200ItemsItemEntityType0
        | ReorderItemsResponse200ItemsItemEntityType1
        | ReorderItemsResponse200ItemsItemEntityType2
        | ReorderItemsResponse200ItemsItemEntityType3
        | ReorderItemsResponse200ItemsItemEntityType4
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reorder_items_response_200_items_item_entity_type_0 import (
            ReorderItemsResponse200ItemsItemEntityType0,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_1 import (
            ReorderItemsResponse200ItemsItemEntityType1,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_2 import (
            ReorderItemsResponse200ItemsItemEntityType2,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_3 import (
            ReorderItemsResponse200ItemsItemEntityType3,  # noqa: PLC0415
        )

        id = self.id

        position: int | None
        position = self.position

        note: None | str
        note = self.note

        created_at = self.created_at

        updated_at = self.updated_at

        variant_id: int | None
        variant_id = self.variant_id

        entity_type = self.entity_type

        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        entity: dict[str, Any] | Unset
        if isinstance(self.entity, Unset):
            entity = UNSET
        elif isinstance(self.entity, ReorderItemsResponse200ItemsItemEntityType0):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, ReorderItemsResponse200ItemsItemEntityType1):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, ReorderItemsResponse200ItemsItemEntityType2):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, ReorderItemsResponse200ItemsItemEntityType3):
            entity = self.entity.to_dict()
        else:
            entity = self.entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "note": note,
                "created_at": created_at,
                "updated_at": updated_at,
                "variant_id": variant_id,
                "entity_type": entity_type,
            }
        )
        if variant is not UNSET:
            field_dict["variant"] = variant
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_items_response_200_items_item_entity_type_0 import (
            ReorderItemsResponse200ItemsItemEntityType0,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_1 import (
            ReorderItemsResponse200ItemsItemEntityType1,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_2 import (
            ReorderItemsResponse200ItemsItemEntityType2,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_3 import (
            ReorderItemsResponse200ItemsItemEntityType3,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_entity_type_4 import (
            ReorderItemsResponse200ItemsItemEntityType4,  # noqa: PLC0415
        )
        from ..models.reorder_items_response_200_items_item_variant import ReorderItemsResponse200ItemsItemVariant  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        entity_type = d.pop("entity_type")

        _variant = d.pop("variant", UNSET)
        variant: ReorderItemsResponse200ItemsItemVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = ReorderItemsResponse200ItemsItemVariant.from_dict(_variant)

        def _parse_entity(
            data: object,
        ) -> (
            ReorderItemsResponse200ItemsItemEntityType0
            | ReorderItemsResponse200ItemsItemEntityType1
            | ReorderItemsResponse200ItemsItemEntityType2
            | ReorderItemsResponse200ItemsItemEntityType3
            | ReorderItemsResponse200ItemsItemEntityType4
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_0 = ReorderItemsResponse200ItemsItemEntityType0.from_dict(data)

                return entity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_1 = ReorderItemsResponse200ItemsItemEntityType1.from_dict(data)

                return entity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_2 = ReorderItemsResponse200ItemsItemEntityType2.from_dict(data)

                return entity_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_3 = ReorderItemsResponse200ItemsItemEntityType3.from_dict(data)

                return entity_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            entity_type_4 = ReorderItemsResponse200ItemsItemEntityType4.from_dict(data)

            return entity_type_4

        entity = _parse_entity(d.pop("entity", UNSET))

        reorder_items_response_200_items_item = cls(
            id=id,
            position=position,
            note=note,
            created_at=created_at,
            updated_at=updated_at,
            variant_id=variant_id,
            entity_type=entity_type,
            variant=variant,
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
