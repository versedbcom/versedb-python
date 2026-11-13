from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue_name_i18n_additional_property import (
        LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty,
    )


T = TypeVar("T", bound="LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18N")


@_attrs_define
class LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18N:
    """One name per language, keyed by BCP 47 tag."""

    additional_properties: dict[
        str, LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.look_up_an_issue_by_cover_photo_response_200_candidates_item_issue_name_i18n_additional_property import (
            LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        look_up_an_issue_by_cover_photo_response_200_candidates_item_issue_name_i18n = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        look_up_an_issue_by_cover_photo_response_200_candidates_item_issue_name_i18n.additional_properties = (
            additional_properties
        )
        return look_up_an_issue_by_cover_photo_response_200_candidates_item_issue_name_i18n

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: LookUpAnIssueByCoverPhotoResponse200CandidatesItemIssueNameI18NAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
