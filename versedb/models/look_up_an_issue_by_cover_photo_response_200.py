from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item import (
        LookUpAnIssueByCoverPhotoResponse200CandidatesItem,
    )


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse200")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse200:
    """
    Attributes:
        matched_by (str): Always `image`: the answer comes from the image match.
        clear_match (bool): Whether the image match is sure of the issue.
        issue_id (int | None): The matched issue when `clear_match` is true, otherwise null.
        variant_id (int | None): The matched variant cover when the match settled one, otherwise null.
        candidates (list[LookUpAnIssueByCoverPhotoResponse200CandidatesItem]): Best first: the matched issue alone on a
            clear match, otherwise up to five possibilities.
    """

    matched_by: str
    clear_match: bool
    issue_id: int | None
    variant_id: int | None
    candidates: list[LookUpAnIssueByCoverPhotoResponse200CandidatesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched_by = self.matched_by

        clear_match = self.clear_match

        issue_id: int | None
        issue_id = self.issue_id

        variant_id: int | None
        variant_id = self.variant_id

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched_by": matched_by,
                "clear_match": clear_match,
                "issue_id": issue_id,
                "variant_id": variant_id,
                "candidates": candidates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item import (
            LookUpAnIssueByCoverPhotoResponse200CandidatesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        matched_by = d.pop("matched_by")

        clear_match = d.pop("clear_match")

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

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = LookUpAnIssueByCoverPhotoResponse200CandidatesItem.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        look_up_an_issue_by_cover_photo_response_200 = cls(
            matched_by=matched_by,
            clear_match=clear_match,
            issue_id=issue_id,
            variant_id=variant_id,
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
