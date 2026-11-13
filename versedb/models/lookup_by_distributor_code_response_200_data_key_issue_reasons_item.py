from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupByDistributorCodeResponse200DataKeyIssueReasonsItem")


@_attrs_define
class LookupByDistributorCodeResponse200DataKeyIssueReasonsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        category (str):
        notes (None | str):
    """

    id: int
    name: None | str
    category: str
    notes: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        category = self.category

        notes: None | str
        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "category": category,
                "notes": notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        category = d.pop("category")

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

        lookup_by_distributor_code_response_200_data_key_issue_reasons_item = cls(
            id=id,
            name=name,
            category=category,
            notes=notes,
        )

        lookup_by_distributor_code_response_200_data_key_issue_reasons_item.additional_properties = d
        return lookup_by_distributor_code_response_200_data_key_issue_reasons_item

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
