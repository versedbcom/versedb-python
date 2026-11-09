from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateListResponse200DataReactionsItem")


@_attrs_define
class UpdateListResponse200DataReactionsItem:
    """
    Attributes:
        reaction (str):
        emoji (str):
        label (str):
        count (int):
    """

    reaction: str
    emoji: str
    label: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction = self.reaction

        emoji = self.emoji

        label = self.label

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reaction": reaction,
                "emoji": emoji,
                "label": label,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction = d.pop("reaction")

        emoji = d.pop("emoji")

        label = d.pop("label")

        count = d.pop("count")

        update_list_response_200_data_reactions_item = cls(
            reaction=reaction,
            emoji=emoji,
            label=label,
            count=count,
        )

        update_list_response_200_data_reactions_item.additional_properties = d
        return update_list_response_200_data_reactions_item

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
