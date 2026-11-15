from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_issue_to_collection_response_409_error import (
    AddIssueToCollectionResponse409Error,
    check_add_issue_to_collection_response_409_error,
)

T = TypeVar("T", bound="AddIssueToCollectionResponse409")


@_attrs_define
class AddIssueToCollectionResponse409:
    """
    Attributes:
        message (str):
        error (AddIssueToCollectionResponse409Error):
    """

    message: str
    error: AddIssueToCollectionResponse409Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        error: str = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        error = check_add_issue_to_collection_response_409_error(d.pop("error"))

        add_issue_to_collection_response_409 = cls(
            message=message,
            error=error,
        )

        add_issue_to_collection_response_409.additional_properties = d
        return add_issue_to_collection_response_409

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
