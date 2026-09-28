from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveIssueFromCollectionBody")


@_attrs_define
class RemoveIssueFromCollectionBody:
    """
    Attributes:
        variant_id (int | None | Unset): Specific variant ID to remove (optional).
        collection_item_id (int | None | Unset): Specific collection item ID to remove (optional).
    """

    variant_id: int | None | Unset = UNSET
    collection_item_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id: int | None | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        collection_item_id: int | None | Unset
        if isinstance(self.collection_item_id, Unset):
            collection_item_id = UNSET
        else:
            collection_item_id = self.collection_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if collection_item_id is not UNSET:
            field_dict["collection_item_id"] = collection_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_variant_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        def _parse_collection_item_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        collection_item_id = _parse_collection_item_id(d.pop("collection_item_id", UNSET))

        remove_issue_from_collection_body = cls(
            variant_id=variant_id,
            collection_item_id=collection_item_id,
        )

        remove_issue_from_collection_body.additional_properties = d
        return remove_issue_from_collection_body

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
