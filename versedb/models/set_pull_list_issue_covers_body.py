from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetPullListIssueCoversBody")


@_attrs_define
class SetPullListIssueCoversBody:
    """
    Attributes:
        standard (bool): Whether the user is getting the main cover, the standard cover.
        variant_ids (list[int]): The variants the user is getting, up to 50. May be empty when `standard` is true.
    """

    standard: bool
    variant_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard = self.standard

        variant_ids = self.variant_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standard": standard,
                "variant_ids": variant_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        standard = d.pop("standard")

        variant_ids = cast(list[int], d.pop("variant_ids"))

        set_pull_list_issue_covers_body = cls(
            standard=standard,
            variant_ids=variant_ids,
        )

        set_pull_list_issue_covers_body.additional_properties = d
        return set_pull_list_issue_covers_body

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
