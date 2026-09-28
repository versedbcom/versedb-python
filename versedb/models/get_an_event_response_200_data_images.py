from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAnEventResponse200DataImages")


@_attrs_define
class GetAnEventResponse200DataImages:
    """
    Attributes:
        tile_sm (str | Unset):
        full_md (str | Unset):
        full_lg (str | Unset):
    """

    tile_sm: str | Unset = UNSET
    full_md: str | Unset = UNSET
    full_lg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tile_sm = self.tile_sm

        full_md = self.full_md

        full_lg = self.full_lg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tile_sm is not UNSET:
            field_dict["tile_sm"] = tile_sm
        if full_md is not UNSET:
            field_dict["full_md"] = full_md
        if full_lg is not UNSET:
            field_dict["full_lg"] = full_lg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tile_sm = d.pop("tile_sm", UNSET)

        full_md = d.pop("full_md", UNSET)

        full_lg = d.pop("full_lg", UNSET)

        get_an_event_response_200_data_images = cls(
            tile_sm=tile_sm,
            full_md=full_md,
            full_lg=full_lg,
        )

        get_an_event_response_200_data_images.additional_properties = d
        return get_an_event_response_200_data_images

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
