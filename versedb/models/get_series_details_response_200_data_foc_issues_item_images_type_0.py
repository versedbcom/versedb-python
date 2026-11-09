from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeriesDetailsResponse200DataFocIssuesItemImagesType0")


@_attrs_define
class GetSeriesDetailsResponse200DataFocIssuesItemImagesType0:
    """
    Attributes:
        thumb (str | Unset):
        cover_sm (str | Unset):
        cover_md (str | Unset):
        cover_lg (str | Unset):
    """

    thumb: str | Unset = UNSET
    cover_sm: str | Unset = UNSET
    cover_md: str | Unset = UNSET
    cover_lg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumb = self.thumb

        cover_sm = self.cover_sm

        cover_md = self.cover_md

        cover_lg = self.cover_lg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumb is not UNSET:
            field_dict["thumb"] = thumb
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
        thumb = d.pop("thumb", UNSET)

        cover_sm = d.pop("cover_sm", UNSET)

        cover_md = d.pop("cover_md", UNSET)

        cover_lg = d.pop("cover_lg", UNSET)

        get_series_details_response_200_data_foc_issues_item_images_type_0 = cls(
            thumb=thumb,
            cover_sm=cover_sm,
            cover_md=cover_md,
            cover_lg=cover_lg,
        )

        get_series_details_response_200_data_foc_issues_item_images_type_0.additional_properties = d
        return get_series_details_response_200_data_foc_issues_item_images_type_0

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
