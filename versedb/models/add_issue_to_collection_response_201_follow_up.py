from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddIssueToCollectionResponse201FollowUp")


@_attrs_define
class AddIssueToCollectionResponse201FollowUp:
    """
    Attributes:
        prompt (bool | Unset):
        can_mark_read (bool | Unset):
        can_review (bool | Unset):
        has_review (bool | Unset):
    """

    prompt: bool | Unset = UNSET
    can_mark_read: bool | Unset = UNSET
    can_review: bool | Unset = UNSET
    has_review: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        can_mark_read = self.can_mark_read

        can_review = self.can_review

        has_review = self.has_review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if can_mark_read is not UNSET:
            field_dict["can_mark_read"] = can_mark_read
        if can_review is not UNSET:
            field_dict["can_review"] = can_review
        if has_review is not UNSET:
            field_dict["has_review"] = has_review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt", UNSET)

        can_mark_read = d.pop("can_mark_read", UNSET)

        can_review = d.pop("can_review", UNSET)

        has_review = d.pop("has_review", UNSET)

        add_issue_to_collection_response_201_follow_up = cls(
            prompt=prompt,
            can_mark_read=can_mark_read,
            can_review=can_review,
            has_review=has_review,
        )

        add_issue_to_collection_response_201_follow_up.additional_properties = d
        return add_issue_to_collection_response_201_follow_up

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
