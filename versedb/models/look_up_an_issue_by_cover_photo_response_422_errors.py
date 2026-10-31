from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse422Errors")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse422Errors:
    """
    Attributes:
        image (list[str] | Unset):
    """

    image: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image: list[str] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = cast(list[str], d.pop("image", UNSET))

        look_up_an_issue_by_cover_photo_response_422_errors = cls(
            image=image,
        )

        look_up_an_issue_by_cover_photo_response_422_errors.additional_properties = d
        return look_up_an_issue_by_cover_photo_response_422_errors

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
