from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue import (
        LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue,
    )


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse200CandidatesItem")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse200CandidatesItem:
    """
    Attributes:
        issue_id (int): The candidate issue.
        variant_id (int | None): The candidate's best-scoring variant cover; null is the issue's own cover.
        issue (LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue): The issue, as `GET /api/v1/issues` returns it
            with `include=series`.
    """

    issue_id: int
    variant_id: int | None
    issue: LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        variant_id: int | None
        variant_id = self.variant_id

        issue = self.issue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "variant_id": variant_id,
                "issue": issue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue import (
            LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        issue = LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue.from_dict(d.pop("issue"))

        look_up_an_issue_by_cover_photo_response_200_candidates_item = cls(
            issue_id=issue_id,
            variant_id=variant_id,
            issue=issue,
        )

        look_up_an_issue_by_cover_photo_response_200_candidates_item.additional_properties = d
        return look_up_an_issue_by_cover_photo_response_200_candidates_item

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
