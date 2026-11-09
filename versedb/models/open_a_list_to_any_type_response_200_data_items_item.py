from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_0 import (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType0,
    )
    from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_1 import (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType1,
    )
    from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_2 import (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType2,
    )
    from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_3 import (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType3,
    )
    from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_4 import (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType4,
    )
    from ..models.open_a_list_to_any_type_response_200_data_items_item_variant import (
        OpenAListToAnyTypeResponse200DataItemsItemVariant,
    )


T = TypeVar("T", bound="OpenAListToAnyTypeResponse200DataItemsItem")


@_attrs_define
class OpenAListToAnyTypeResponse200DataItemsItem:
    """
    Attributes:
        id (int):
        position (int | None): Its place on a ranked or rule-built list.
        note (None | str):
        created_at (str):
        updated_at (str):
        variant_id (int | None):
        entity_type (str): issues, series, characters, creators, story_arcs or teams.
        variant (OpenAListToAnyTypeResponse200DataItemsItemVariant | Unset): The pinned cover, while it exists.
        entity (OpenAListToAnyTypeResponse200DataItemsItemEntityType0 |
            OpenAListToAnyTypeResponse200DataItemsItemEntityType1 | OpenAListToAnyTypeResponse200DataItemsItemEntityType2 |
            OpenAListToAnyTypeResponse200DataItemsItemEntityType3 | OpenAListToAnyTypeResponse200DataItemsItemEntityType4 |
            Unset): Left out once the entity is gone.
    """

    id: int
    position: int | None
    note: None | str
    created_at: str
    updated_at: str
    variant_id: int | None
    entity_type: str
    variant: OpenAListToAnyTypeResponse200DataItemsItemVariant | Unset = UNSET
    entity: (
        OpenAListToAnyTypeResponse200DataItemsItemEntityType0
        | OpenAListToAnyTypeResponse200DataItemsItemEntityType1
        | OpenAListToAnyTypeResponse200DataItemsItemEntityType2
        | OpenAListToAnyTypeResponse200DataItemsItemEntityType3
        | OpenAListToAnyTypeResponse200DataItemsItemEntityType4
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_0 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType0,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_1 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType1,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_2 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType2,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_3 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType3,  # noqa: PLC0415
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
        elif isinstance(self.entity, OpenAListToAnyTypeResponse200DataItemsItemEntityType0):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, OpenAListToAnyTypeResponse200DataItemsItemEntityType1):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, OpenAListToAnyTypeResponse200DataItemsItemEntityType2):
            entity = self.entity.to_dict()
        elif isinstance(self.entity, OpenAListToAnyTypeResponse200DataItemsItemEntityType3):
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
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_0 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType0,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_1 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType1,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_2 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType2,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_3 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType3,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_entity_type_4 import (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType4,  # noqa: PLC0415
        )
        from ..models.open_a_list_to_any_type_response_200_data_items_item_variant import (
            OpenAListToAnyTypeResponse200DataItemsItemVariant,  # noqa: PLC0415
        )

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
        variant: OpenAListToAnyTypeResponse200DataItemsItemVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = OpenAListToAnyTypeResponse200DataItemsItemVariant.from_dict(_variant)

        def _parse_entity(
            data: object,
        ) -> (
            OpenAListToAnyTypeResponse200DataItemsItemEntityType0
            | OpenAListToAnyTypeResponse200DataItemsItemEntityType1
            | OpenAListToAnyTypeResponse200DataItemsItemEntityType2
            | OpenAListToAnyTypeResponse200DataItemsItemEntityType3
            | OpenAListToAnyTypeResponse200DataItemsItemEntityType4
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_0 = OpenAListToAnyTypeResponse200DataItemsItemEntityType0.from_dict(data)

                return entity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_1 = OpenAListToAnyTypeResponse200DataItemsItemEntityType1.from_dict(data)

                return entity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_2 = OpenAListToAnyTypeResponse200DataItemsItemEntityType2.from_dict(data)

                return entity_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_type_3 = OpenAListToAnyTypeResponse200DataItemsItemEntityType3.from_dict(data)

                return entity_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            entity_type_4 = OpenAListToAnyTypeResponse200DataItemsItemEntityType4.from_dict(data)

            return entity_type_4

        entity = _parse_entity(d.pop("entity", UNSET))

        open_a_list_to_any_type_response_200_data_items_item = cls(
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

        open_a_list_to_any_type_response_200_data_items_item.additional_properties = d
        return open_a_list_to_any_type_response_200_data_items_item

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
