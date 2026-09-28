from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LikeListOrReactToItResponse201ReactionsItem")


@_attrs_define
class LikeListOrReactToItResponse201ReactionsItem:
    """
    Attributes:
        reaction (str | Unset):
        emoji (str | Unset):
        label (str | Unset):
        count (int | Unset):
    """

    reaction: str | Unset = UNSET
    emoji: str | Unset = UNSET
    label: str | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction = self.reaction

        emoji = self.emoji

        label = self.label

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reaction is not UNSET:
            field_dict["reaction"] = reaction
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if label is not UNSET:
            field_dict["label"] = label
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction = d.pop("reaction", UNSET)

        emoji = d.pop("emoji", UNSET)

        label = d.pop("label", UNSET)

        count = d.pop("count", UNSET)

        like_list_or_react_to_it_response_201_reactions_item = cls(
            reaction=reaction,
            emoji=emoji,
            label=label,
            count=count,
        )

        like_list_or_react_to_it_response_201_reactions_item.additional_properties = d
        return like_list_or_react_to_it_response_201_reactions_item

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
