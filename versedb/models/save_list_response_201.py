from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SaveListResponse201")


@_attrs_define
class SaveListResponse201:
    """
    Attributes:
        message (str):
        saved (bool):
        saves_count (int):
    """

    message: str
    saved: bool
    saves_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        saved = self.saved

        saves_count = self.saves_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "saved": saved,
                "saves_count": saves_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        saved = d.pop("saved")

        saves_count = d.pop("saves_count")

        save_list_response_201 = cls(
            message=message,
            saved=saved,
            saves_count=saves_count,
        )

        save_list_response_201.additional_properties = d
        return save_list_response_201

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
