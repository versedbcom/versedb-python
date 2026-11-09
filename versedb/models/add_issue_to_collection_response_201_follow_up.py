from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddIssueToCollectionResponse201FollowUp")


@_attrs_define
class AddIssueToCollectionResponse201FollowUp:
    """
    Attributes:
        prompt (bool): The member asked to be prompted, and there is something to offer.
        can_mark_read (bool):
        can_review (bool):
        has_review (bool):
    """

    prompt: bool
    can_mark_read: bool
    can_review: bool
    has_review: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        can_mark_read = self.can_mark_read

        can_review = self.can_review

        has_review = self.has_review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "can_mark_read": can_mark_read,
                "can_review": can_review,
                "has_review": has_review,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        can_mark_read = d.pop("can_mark_read")

        can_review = d.pop("can_review")

        has_review = d.pop("has_review")

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
