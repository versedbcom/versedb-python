from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue import (
        LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue,
    )


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse200CandidatesItem")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse200CandidatesItem:
    """
    Attributes:
        variant_id (int | None): The candidate's best-scoring variant cover; null is the issue's own cover.
        issue_id (int | Unset): The candidate issue.
        issue (LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue | Unset): The issue, as `GET /api/v1/issues`
            returns it with `include=series`.
    """

    variant_id: int | None
    issue_id: int | Unset = UNSET
    issue: LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id: int | None
        variant_id = self.variant_id

        issue_id = self.issue_id

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant_id": variant_id,
            }
        )
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if issue is not UNSET:
            field_dict["issue"] = issue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue import (
            LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        issue_id = d.pop("issue_id", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssue.from_dict(_issue)

        look_up_an_issue_by_cover_photo_response_200_candidates_item = cls(
            variant_id=variant_id,
            issue_id=issue_id,
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
