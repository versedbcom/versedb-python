from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStoryArcsForASpecificCharacterResponse200Meta")


@_attrs_define
class GetStoryArcsForASpecificCharacterResponse200Meta:
    """
    Attributes:
        current_page (int | Unset):
        last_page (int | Unset):
        per_page (int | Unset):
        total (int | Unset):
    """

    current_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    per_page: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        per_page = d.pop("per_page", UNSET)

        total = d.pop("total", UNSET)

        get_story_arcs_for_a_specific_character_response_200_meta = cls(
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            total=total,
        )

        get_story_arcs_for_a_specific_character_response_200_meta.additional_properties = d
        return get_story_arcs_for_a_specific_character_response_200_meta

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
