from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckIssueInCollectionResponse200CopiesItem")


@_attrs_define
class CheckIssueInCollectionResponse200CopiesItem:
    """
    Attributes:
        id (int):
        variant_id (int | None):
        condition (None | str):
        graded (bool):
        grade_score (None | str):
        grading_company (None | str):
        is_signed (bool):
        signed_by (None | str):
        is_cgc_ss (bool):
        format_ (None | str):
        storage_location (None | str):
        purchased_at (None | str):
        notes (None | str):
        created_at (None | str):
        updated_at (None | str):
    """

    id: int
    variant_id: int | None
    condition: None | str
    graded: bool
    grade_score: None | str
    grading_company: None | str
    is_signed: bool
    signed_by: None | str
    is_cgc_ss: bool
    format_: None | str
    storage_location: None | str
    purchased_at: None | str
    notes: None | str
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        variant_id: int | None
        variant_id = self.variant_id

        condition: None | str
        condition = self.condition

        graded = self.graded

        grade_score: None | str
        grade_score = self.grade_score

        grading_company: None | str
        grading_company = self.grading_company

        is_signed = self.is_signed

        signed_by: None | str
        signed_by = self.signed_by

        is_cgc_ss = self.is_cgc_ss

        format_: None | str
        format_ = self.format_

        storage_location: None | str
        storage_location = self.storage_location

        purchased_at: None | str
        purchased_at = self.purchased_at

        notes: None | str
        notes = self.notes

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "variant_id": variant_id,
                "condition": condition,
                "graded": graded,
                "grade_score": grade_score,
                "grading_company": grading_company,
                "is_signed": is_signed,
                "signed_by": signed_by,
                "is_cgc_ss": is_cgc_ss,
                "format": format_,
                "storage_location": storage_location,
                "purchased_at": purchased_at,
                "notes": notes,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        def _parse_condition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        condition = _parse_condition(d.pop("condition"))

        graded = d.pop("graded")

        def _parse_grade_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grade_score = _parse_grade_score(d.pop("grade_score"))

        def _parse_grading_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grading_company = _parse_grading_company(d.pop("grading_company"))

        is_signed = d.pop("is_signed")

        def _parse_signed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signed_by = _parse_signed_by(d.pop("signed_by"))

        is_cgc_ss = d.pop("is_cgc_ss")

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

        def _parse_storage_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        storage_location = _parse_storage_location(d.pop("storage_location"))

        def _parse_purchased_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchased_at = _parse_purchased_at(d.pop("purchased_at"))

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        check_issue_in_collection_response_200_copies_item = cls(
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
            updated_at=updated_at,
        )

        check_issue_in_collection_response_200_copies_item.additional_properties = d
        return check_issue_in_collection_response_200_copies_item

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
