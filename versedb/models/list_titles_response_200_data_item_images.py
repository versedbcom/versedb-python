from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTitlesResponse200DataItemImages")


@_attrs_define
class ListTitlesResponse200DataItemImages:
    """
    Attributes:
        cover_sm (str | Unset):
        cover_md (str | Unset):
        cover_lg (str | Unset):
    """

    cover_sm: str | Unset = UNSET
    cover_md: str | Unset = UNSET
    cover_lg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_sm = self.cover_sm

        cover_md = self.cover_md

        cover_lg = self.cover_lg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_sm is not UNSET:
            field_dict["cover_sm"] = cover_sm
        if cover_md is not UNSET:
            field_dict["cover_md"] = cover_md
        if cover_lg is not UNSET:
            field_dict["cover_lg"] = cover_lg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_sm = d.pop("cover_sm", UNSET)

        cover_md = d.pop("cover_md", UNSET)

        cover_lg = d.pop("cover_lg", UNSET)

        list_titles_response_200_data_item_images = cls(
            cover_sm=cover_sm,
            cover_md=cover_md,
            cover_lg=cover_lg,
        )

        list_titles_response_200_data_item_images.additional_properties = d
        return list_titles_response_200_data_item_images

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
