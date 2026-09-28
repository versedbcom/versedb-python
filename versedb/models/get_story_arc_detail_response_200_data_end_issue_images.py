from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStoryArcDetailResponse200DataEndIssueImages")


@_attrs_define
class GetStoryArcDetailResponse200DataEndIssueImages:
    """
    Attributes:
        cover_md (str | Unset):
    """

    cover_md: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_md = self.cover_md

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_md is not UNSET:
            field_dict["cover_md"] = cover_md

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_md = d.pop("cover_md", UNSET)

        get_story_arc_detail_response_200_data_end_issue_images = cls(
            cover_md=cover_md,
        )

        get_story_arc_detail_response_200_data_end_issue_images.additional_properties = d
        return get_story_arc_detail_response_200_data_end_issue_images

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
