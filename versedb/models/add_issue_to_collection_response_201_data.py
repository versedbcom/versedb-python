from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_issue_to_collection_response_201_data_issue import AddIssueToCollectionResponse201DataIssue
    from ..models.add_issue_to_collection_response_201_data_series import AddIssueToCollectionResponse201DataSeries


T = TypeVar("T", bound="AddIssueToCollectionResponse201Data")


@_attrs_define
class AddIssueToCollectionResponse201Data:
    """
    Attributes:
        id (int | Unset):
        issue (AddIssueToCollectionResponse201DataIssue | Unset):
        series (AddIssueToCollectionResponse201DataSeries | Unset):
        variant_id (None | str | Unset):
        condition (str | Unset):
        price_paid (float | Unset):
        notes (str | Unset):
    """

    id: int | Unset = UNSET
    issue: AddIssueToCollectionResponse201DataIssue | Unset = UNSET
    series: AddIssueToCollectionResponse201DataSeries | Unset = UNSET
    variant_id: None | str | Unset = UNSET
    condition: str | Unset = UNSET
    price_paid: float | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        condition = self.condition

        price_paid = self.price_paid

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issue is not UNSET:
            field_dict["issue"] = issue
        if series is not UNSET:
            field_dict["series"] = series
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_issue_to_collection_response_201_data_issue import (
            AddIssueToCollectionResponse201DataIssue,  # noqa: PLC0415
        )
        from ..models.add_issue_to_collection_response_201_data_series import (
            AddIssueToCollectionResponse201DataSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: AddIssueToCollectionResponse201DataIssue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = AddIssueToCollectionResponse201DataIssue.from_dict(_issue)

        _series = d.pop("series", UNSET)
        series: AddIssueToCollectionResponse201DataSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = AddIssueToCollectionResponse201DataSeries.from_dict(_series)

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        condition = d.pop("condition", UNSET)

        price_paid = d.pop("price_paid", UNSET)

        notes = d.pop("notes", UNSET)

        add_issue_to_collection_response_201_data = cls(
            id=id,
            issue=issue,
            series=series,
            variant_id=variant_id,
            condition=condition,
            price_paid=price_paid,
            notes=notes,
        )

        add_issue_to_collection_response_201_data.additional_properties = d
        return add_issue_to_collection_response_201_data

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
