from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem")


@_attrs_define
class ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        category (str | Unset):
        slug (str | Unset):
        notes (None | str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    category: str | Unset = UNSET
    slug: str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        category = self.category

        slug = self.slug

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if slug is not UNSET:
            field_dict["slug"] = slug
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        category = d.pop("category", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        list_collection_response_200_data_item_collectable_key_issue_reasons_item = cls(
            id=id,
            name=name,
            category=category,
            slug=slug,
            notes=notes,
        )

        list_collection_response_200_data_item_collectable_key_issue_reasons_item.additional_properties = d
        return list_collection_response_200_data_item_collectable_key_issue_reasons_item

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
