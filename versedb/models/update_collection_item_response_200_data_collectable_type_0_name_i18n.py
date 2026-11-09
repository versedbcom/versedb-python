from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateCollectionItemResponse200DataCollectableType0NameI18N")


@_attrs_define
class UpdateCollectionItemResponse200DataCollectableType0NameI18N:
    """The name in each language, keyed by BCP 47 tag (trimmed by `?languages=`)."""

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_collection_item_response_200_data_collectable_type_0_name_i18n = cls()

        update_collection_item_response_200_data_collectable_type_0_name_i18n.additional_properties = d
        return update_collection_item_response_200_data_collectable_type_0_name_i18n

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
