from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LikeListOrReactToItBody")


@_attrs_define
class LikeListOrReactToItBody:
    """
    Attributes:
        reaction (str | Unset): One of heart, laugh, wow, fire, clap, confused. Omit for a plain like.
    """

    reaction: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction = self.reaction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reaction is not UNSET:
            field_dict["reaction"] = reaction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction = d.pop("reaction", UNSET)

        like_list_or_react_to_it_body = cls(
            reaction=reaction,
        )

        like_list_or_react_to_it_body.additional_properties = d
        return like_list_or_react_to_it_body

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
