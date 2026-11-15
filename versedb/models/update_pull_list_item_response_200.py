from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_pull_list_item_response_200_preferred_cover_type_type_1 import (
    UpdatePullListItemResponse200PreferredCoverTypeType1,
    check_update_pull_list_item_response_200_preferred_cover_type_type_1,
)
from ..models.update_pull_list_item_response_200_preferred_cover_type_type_2_type_1 import (
    UpdatePullListItemResponse200PreferredCoverTypeType2Type1,
    check_update_pull_list_item_response_200_preferred_cover_type_type_2_type_1,
)
from ..models.update_pull_list_item_response_200_preferred_cover_type_type_3_type_1 import (
    UpdatePullListItemResponse200PreferredCoverTypeType3Type1,
    check_update_pull_list_item_response_200_preferred_cover_type_type_3_type_1,
)
from ..models.update_pull_list_item_response_200_status import (
    UpdatePullListItemResponse200Status,
    check_update_pull_list_item_response_200_status,
)

T = TypeVar("T", bound="UpdatePullListItemResponse200")


@_attrs_define
class UpdatePullListItemResponse200:
    """
    Attributes:
        id (int):
        series_id (int | None):
        status (UpdatePullListItemResponse200Status):
        personal_notes (None | str):
        preferred_cover_type (None | UpdatePullListItemResponse200PreferredCoverTypeType1 |
            UpdatePullListItemResponse200PreferredCoverTypeType2Type1 |
            UpdatePullListItemResponse200PreferredCoverTypeType3Type1): The standing cover choice; null is `standard`.
        pull_source_id (int | None):
        pull_source_ids (list[int]):
        updated_at (None | str):
    """

    id: int
    series_id: int | None
    status: UpdatePullListItemResponse200Status
    personal_notes: None | str
    preferred_cover_type: (
        None
        | UpdatePullListItemResponse200PreferredCoverTypeType1
        | UpdatePullListItemResponse200PreferredCoverTypeType2Type1
        | UpdatePullListItemResponse200PreferredCoverTypeType3Type1
    )
    pull_source_id: int | None
    pull_source_ids: list[int]
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        series_id: int | None
        series_id = self.series_id

        status: str = self.status

        personal_notes: None | str
        personal_notes = self.personal_notes

        preferred_cover_type: None | str
        if isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        elif isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        elif isinstance(self.preferred_cover_type, str):
            preferred_cover_type = self.preferred_cover_type
        else:
            preferred_cover_type = self.preferred_cover_type

        pull_source_id: int | None
        pull_source_id = self.pull_source_id

        pull_source_ids = self.pull_source_ids

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "series_id": series_id,
                "status": status,
                "personal_notes": personal_notes,
                "preferred_cover_type": preferred_cover_type,
                "pull_source_id": pull_source_id,
                "pull_source_ids": pull_source_ids,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        status = check_update_pull_list_item_response_200_status(d.pop("status"))

        def _parse_personal_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        personal_notes = _parse_personal_notes(d.pop("personal_notes"))

        def _parse_preferred_cover_type(
            data: object,
        ) -> (
            None
            | UpdatePullListItemResponse200PreferredCoverTypeType1
            | UpdatePullListItemResponse200PreferredCoverTypeType2Type1
            | UpdatePullListItemResponse200PreferredCoverTypeType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_1 = check_update_pull_list_item_response_200_preferred_cover_type_type_1(data)

                return preferred_cover_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_2_type_1 = (
                    check_update_pull_list_item_response_200_preferred_cover_type_type_2_type_1(data)
                )

                return preferred_cover_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_cover_type_type_3_type_1 = (
                    check_update_pull_list_item_response_200_preferred_cover_type_type_3_type_1(data)
                )

                return preferred_cover_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | UpdatePullListItemResponse200PreferredCoverTypeType1
                | UpdatePullListItemResponse200PreferredCoverTypeType2Type1
                | UpdatePullListItemResponse200PreferredCoverTypeType3Type1,
                data,
            )

        preferred_cover_type = _parse_preferred_cover_type(d.pop("preferred_cover_type"))

        def _parse_pull_source_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pull_source_id = _parse_pull_source_id(d.pop("pull_source_id"))

        pull_source_ids = cast(list[int], d.pop("pull_source_ids"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        update_pull_list_item_response_200 = cls(
            id=id,
            series_id=series_id,
            status=status,
            personal_notes=personal_notes,
            preferred_cover_type=preferred_cover_type,
            pull_source_id=pull_source_id,
            pull_source_ids=pull_source_ids,
            updated_at=updated_at,
        )

        update_pull_list_item_response_200.additional_properties = d
        return update_pull_list_item_response_200

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
