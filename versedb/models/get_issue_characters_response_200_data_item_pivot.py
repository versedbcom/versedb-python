from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetIssueCharactersResponse200DataItemPivot")


@_attrs_define
class GetIssueCharactersResponse200DataItemPivot:
    """
    Attributes:
        issue_id (int):
        character_id (int):
        is_spoiler (bool):
        sort_order (int | None):
        created_at (None | str):
        updated_at (None | str):
    """

    issue_id: int
    character_id: int
    is_spoiler: bool
    sort_order: int | None
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        character_id = self.character_id

        is_spoiler = self.is_spoiler

        sort_order: int | None
        sort_order = self.sort_order

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "character_id": character_id,
                "is_spoiler": is_spoiler,
                "sort_order": sort_order,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        character_id = d.pop("character_id")

        is_spoiler = d.pop("is_spoiler")

        def _parse_sort_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sort_order = _parse_sort_order(d.pop("sort_order"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        get_issue_characters_response_200_data_item_pivot = cls(
            issue_id=issue_id,
            character_id=character_id,
            is_spoiler=is_spoiler,
            sort_order=sort_order,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_issue_characters_response_200_data_item_pivot.additional_properties = d
        return get_issue_characters_response_200_data_item_pivot

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
