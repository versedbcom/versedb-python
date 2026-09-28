from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckIssueInCollectionResponse200Type0CopiesItem")


@_attrs_define
class CheckIssueInCollectionResponse200Type0CopiesItem:
    """
    Attributes:
        id (int | Unset):
        variant_id (int | Unset):
        condition (str | Unset):
        graded (bool | Unset):
        grade_score (str | Unset):
        grading_company (str | Unset):
        is_signed (bool | Unset):
        signed_by (None | str | Unset):
        is_cgc_ss (bool | Unset):
        format_ (str | Unset):
        storage_location (str | Unset):
        purchased_at (str | Unset):
        notes (str | Unset):
        created_at (str | Unset):
    """

    id: int | Unset = UNSET
    variant_id: int | Unset = UNSET
    condition: str | Unset = UNSET
    graded: bool | Unset = UNSET
    grade_score: str | Unset = UNSET
    grading_company: str | Unset = UNSET
    is_signed: bool | Unset = UNSET
    signed_by: None | str | Unset = UNSET
    is_cgc_ss: bool | Unset = UNSET
    format_: str | Unset = UNSET
    storage_location: str | Unset = UNSET
    purchased_at: str | Unset = UNSET
    notes: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        variant_id = self.variant_id

        condition = self.condition

        graded = self.graded

        grade_score = self.grade_score

        grading_company = self.grading_company

        is_signed = self.is_signed

        signed_by: None | str | Unset
        if isinstance(self.signed_by, Unset):
            signed_by = UNSET
        else:
            signed_by = self.signed_by

        is_cgc_ss = self.is_cgc_ss

        format_ = self.format_

        storage_location = self.storage_location

        purchased_at = self.purchased_at

        notes = self.notes

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if graded is not UNSET:
            field_dict["graded"] = graded
        if grade_score is not UNSET:
            field_dict["grade_score"] = grade_score
        if grading_company is not UNSET:
            field_dict["grading_company"] = grading_company
        if is_signed is not UNSET:
            field_dict["is_signed"] = is_signed
        if signed_by is not UNSET:
            field_dict["signed_by"] = signed_by
        if is_cgc_ss is not UNSET:
            field_dict["is_cgc_ss"] = is_cgc_ss
        if format_ is not UNSET:
            field_dict["format"] = format_
        if storage_location is not UNSET:
            field_dict["storage_location"] = storage_location
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        variant_id = d.pop("variant_id", UNSET)

        condition = d.pop("condition", UNSET)

        graded = d.pop("graded", UNSET)

        grade_score = d.pop("grade_score", UNSET)

        grading_company = d.pop("grading_company", UNSET)

        is_signed = d.pop("is_signed", UNSET)

        def _parse_signed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signed_by = _parse_signed_by(d.pop("signed_by", UNSET))

        is_cgc_ss = d.pop("is_cgc_ss", UNSET)

        format_ = d.pop("format", UNSET)

        storage_location = d.pop("storage_location", UNSET)

        purchased_at = d.pop("purchased_at", UNSET)

        notes = d.pop("notes", UNSET)

        created_at = d.pop("created_at", UNSET)

        check_issue_in_collection_response_200_type_0_copies_item = cls(
            id=id,
            variant_id=variant_id,
            condition=condition,
            graded=graded,
            grade_score=grade_score,
            grading_company=grading_company,
            is_signed=is_signed,
            signed_by=signed_by,
            is_cgc_ss=is_cgc_ss,
            format_=format_,
            storage_location=storage_location,
            purchased_at=purchased_at,
            notes=notes,
            created_at=created_at,
        )

        check_issue_in_collection_response_200_type_0_copies_item.additional_properties = d
        return check_issue_in_collection_response_200_type_0_copies_item

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
