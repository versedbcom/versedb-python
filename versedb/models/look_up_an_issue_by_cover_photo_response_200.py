from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item import (
        LookUpAnIssueByCoverPhotoResponse200CandidatesItem,
    )


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse200")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse200:
    """
    Attributes:
        issue_id (int | None): The matched issue when `clear_match` is true, otherwise null.
        variant_id (int | None): The matched variant cover when the match settled one, otherwise null.
        matched_by (str | Unset): Always `image`: the answer comes from the image match.
        clear_match (bool | Unset): Whether the image match is sure of the issue.
        candidates (list[LookUpAnIssueByCoverPhotoResponse200CandidatesItem] | Unset): Best first: the matched issue
            alone on a clear match, otherwise up to five possibilities.
    """

    issue_id: int | None
    variant_id: int | None
    matched_by: str | Unset = UNSET
    clear_match: bool | Unset = UNSET
    candidates: list[LookUpAnIssueByCoverPhotoResponse200CandidatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id: int | None
        issue_id = self.issue_id

        variant_id: int | None
        variant_id = self.variant_id

        matched_by = self.matched_by

        clear_match = self.clear_match

        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "variant_id": variant_id,
            }
        )
        if matched_by is not UNSET:
            field_dict["matched_by"] = matched_by
        if clear_match is not UNSET:
            field_dict["clear_match"] = clear_match
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item import (
            LookUpAnIssueByCoverPhotoResponse200CandidatesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_issue_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issue_id = _parse_issue_id(d.pop("issue_id"))

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        matched_by = d.pop("matched_by", UNSET)

        clear_match = d.pop("clear_match", UNSET)

        _candidates = d.pop("candidates", UNSET)
        candidates: list[LookUpAnIssueByCoverPhotoResponse200CandidatesItem] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = LookUpAnIssueByCoverPhotoResponse200CandidatesItem.from_dict(candidates_item_data)

                candidates.append(candidates_item)

        look_up_an_issue_by_cover_photo_response_200 = cls(
            issue_id=issue_id,
            variant_id=variant_id,
            matched_by=matched_by,
            clear_match=clear_match,
            candidates=candidates,
        )

        look_up_an_issue_by_cover_photo_response_200.additional_properties = d
        return look_up_an_issue_by_cover_photo_response_200

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
