from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_issue_to_collection_response_422_type_0_errors import AddIssueToCollectionResponse422Type0Errors


T = TypeVar("T", bound="AddIssueToCollectionResponse422Type0")


@_attrs_define
class AddIssueToCollectionResponse422Type0:
    """
    Attributes:
        message (str):
        errors (AddIssueToCollectionResponse422Type0Errors):
    """

    message: str
    errors: AddIssueToCollectionResponse422Type0Errors
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_issue_to_collection_response_422_type_0_errors import (
            AddIssueToCollectionResponse422Type0Errors,  # noqa: PLC0415
        )

        d = dict(src_dict)
        message = d.pop("message")

        errors = AddIssueToCollectionResponse422Type0Errors.from_dict(d.pop("errors"))

        add_issue_to_collection_response_422_type_0 = cls(
            message=message,
            errors=errors,
        )

        add_issue_to_collection_response_422_type_0.additional_properties = d
        return add_issue_to_collection_response_422_type_0

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
