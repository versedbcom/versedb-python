from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCharacterTeamsResponse200DataItemMembership")


@_attrs_define
class GetCharacterTeamsResponse200DataItemMembership:
    """
    Attributes:
        role (str | Unset):
        joined_date (str | Unset):
        left_date (None | str | Unset):
    """

    role: str | Unset = UNSET
    joined_date: str | Unset = UNSET
    left_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        joined_date = self.joined_date

        left_date: None | str | Unset
        if isinstance(self.left_date, Unset):
            left_date = UNSET
        else:
            left_date = self.left_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date
        if left_date is not UNSET:
            field_dict["left_date"] = left_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role", UNSET)

        joined_date = d.pop("joined_date", UNSET)

        def _parse_left_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        left_date = _parse_left_date(d.pop("left_date", UNSET))

        get_character_teams_response_200_data_item_membership = cls(
            role=role,
            joined_date=joined_date,
            left_date=left_date,
        )

        get_character_teams_response_200_data_item_membership.additional_properties = d
        return get_character_teams_response_200_data_item_membership

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
