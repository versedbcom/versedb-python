from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_422_errors import LookUpAnIssueByCoverPhotoResponse422Errors


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse422")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse422:
    """
    Attributes:
        message (str):
        errors (LookUpAnIssueByCoverPhotoResponse422Errors):
    """

    message: str
    errors: LookUpAnIssueByCoverPhotoResponse422Errors
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
        from ..models.look_up_an_issue_by_cover_photo_response_422_errors import (
            LookUpAnIssueByCoverPhotoResponse422Errors,  # noqa: PLC0415
        )

        d = dict(src_dict)
        message = d.pop("message")

        errors = LookUpAnIssueByCoverPhotoResponse422Errors.from_dict(d.pop("errors"))

        look_up_an_issue_by_cover_photo_response_422 = cls(
            message=message,
            errors=errors,
        )

        look_up_an_issue_by_cover_photo_response_422.additional_properties = d
        return look_up_an_issue_by_cover_photo_response_422

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
