from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LendACopyOutBody")


@_attrs_define
class LendACopyOutBody:
    """
    Attributes:
        loaned_to (str): Who has the comic. Free text — the borrower does not need a VerseDB account. Must not be
            greater than 255 characters.
        loaned_at (None | str | Unset): The day it left (YYYY-MM-DD). Defaults to today. Must be a valid date.
        due_at (None | str | Unset): When it is due back (YYYY-MM-DD). Omit for an open-ended loan. Must be a valid
            date. Must be a date after or equal to <code>loaned_at</code>.
        notes (None | str | Unset): Anything worth recording about the loan. Must not be greater than 1000 characters.
    """

    loaned_to: str
    loaned_at: None | str | Unset = UNSET
    due_at: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loaned_to = self.loaned_to

        loaned_at: None | str | Unset
        if isinstance(self.loaned_at, Unset):
            loaned_at = UNSET
        else:
            loaned_at = self.loaned_at

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        else:
            due_at = self.due_at

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loaned_to": loaned_to,
            }
        )
        if loaned_at is not UNSET:
            field_dict["loaned_at"] = loaned_at
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        loaned_to = d.pop("loaned_to")

        def _parse_loaned_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loaned_at = _parse_loaned_at(d.pop("loaned_at", UNSET))

        def _parse_due_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        lend_a_copy_out_body = cls(
            loaned_to=loaned_to,
            loaned_at=loaned_at,
            due_at=due_at,
            notes=notes,
        )

        lend_a_copy_out_body.additional_properties = d
        return lend_a_copy_out_body

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
