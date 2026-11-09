from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200Meta")


@_attrs_define
class ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200Meta:
    """
    Attributes:
        current_page (int):
        last_page (int):
        per_page (int):
        total (int):
    """

    current_page: int
    last_page: int
    per_page: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "last_page": last_page,
                "per_page": per_page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page")

        last_page = d.pop("last_page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_meta = cls(
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            total=total,
        )

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_meta.additional_properties = d
        return view_your_unfinished_comics_from_the_verse_db_reader_response_200_meta

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
