from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_pull_list_item_body_preferred_cover_type_type_1 import (
    UpdatePullListItemBodyPreferredCoverTypeType1,
    check_update_pull_list_item_body_preferred_cover_type_type_1,
)
from ..models.update_pull_list_item_body_preferred_cover_type_type_2_type_1 import (
    UpdatePullListItemBodyPreferredCoverTypeType2Type1,
    check_update_pull_list_item_body_preferred_cover_type_type_2_type_1,
)
from ..models.update_pull_list_item_body_preferred_cover_type_type_3_type_1 import (
    UpdatePullListItemBodyPreferredCoverTypeType3Type1,
    check_update_pull_list_item_body_preferred_cover_type_type_3_type_1,
)
from ..models.update_pull_list_item_body_status import (
    UpdatePullListItemBodyStatus,
    check_update_pull_list_item_body_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePullListItemBody")


@_attrs_define
class UpdatePullListItemBody:
    """
    Attributes:
        status (UpdatePullListItemBodyStatus | Unset): The entry status.
        personal_notes (None | str | Unset): Notes on the entry.
        preferred_cover_type (None | Unset | UpdatePullListItemBodyPreferredCoverTypeType1 |
            UpdatePullListItemBodyPreferredCoverTypeType2Type1 | UpdatePullListItemBodyPreferredCoverTypeType3Type1): The
            standing cover choice; null is `standard`.
        pull_source_ids (list[int] | Unset): Up to three of the user's pull sources.
    """

    status: UpdatePullListItemBodyStatus | Unset = UNSET
    personal_notes: None | str | Unset = UNSET
    preferred_cover_type: (
        None
        | Unset
        | UpdatePullListItemBodyPreferredCoverTypeType1
        | UpdatePullListItemBodyPreferredCoverTypeType2Type1
        | UpdatePullListItemBodyPreferredCoverTypeType3Type1
    ) = UNSET
    pull_source_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        personal_notes: None | str | Unset
        if isinstance(self.personal_notes, Unset):
            personal_notes = UNSET
        else:
            personal_notes = self.personal_notes

        preferred_cover_type: None | str | Unset
        if isinstance(self.preferred_cover_type, Unset):
            preferred_cover_type = UNSET
        elif isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        elif isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        elif isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        else:
            preferred_cover_type = self.preferred_cover_type

        pull_source_ids: list[int] | Unset = UNSET
        if not isinstance(self.pull_source_ids, Unset):
            pull_source_ids = self.pull_source_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if personal_notes is not UNSET:
            field_dict["personal_notes"] = personal_notes
        if preferred_cover_type is not UNSET:
            field_dict["preferred_cover_type"] = preferred_cover_type
        if pull_source_ids is not UNSET:
            field_dict["pull_source_ids"] = pull_source_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: UpdatePullListItemBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_pull_list_item_body_status(_status)

        def _parse_personal_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        personal_notes = _parse_personal_notes(d.pop("personal_notes", UNSET))

        def _parse_preferred_cover_type(
            data: object,
        ) -> (
            None
            | Unset
            | UpdatePullListItemBodyPreferredCoverTypeType1
            | UpdatePullListItemBodyPreferredCoverTypeType2Type1
            | UpdatePullListItemBodyPreferredCoverTypeType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_1 = check_update_pull_list_item_body_preferred_cover_type_type_1(data)

                return preferred_cover_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_2_type_1 = (
                    check_update_pull_list_item_body_preferred_cover_type_type_2_type_1(data)
                )

                return preferred_cover_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_3_type_1 = (
                    check_update_pull_list_item_body_preferred_cover_type_type_3_type_1(data)
                )

                return preferred_cover_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | UpdatePullListItemBodyPreferredCoverTypeType1
                | UpdatePullListItemBodyPreferredCoverTypeType2Type1
                | UpdatePullListItemBodyPreferredCoverTypeType3Type1,
                data,
            )

        preferred_cover_type = _parse_preferred_cover_type(d.pop("preferred_cover_type", UNSET))

        pull_source_ids = cast(list[int], d.pop("pull_source_ids", UNSET))

        update_pull_list_item_body = cls(
            status=status,
            personal_notes=personal_notes,
            preferred_cover_type=preferred_cover_type,
            pull_source_ids=pull_source_ids,
        )

        update_pull_list_item_body.additional_properties = d
        return update_pull_list_item_body

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
