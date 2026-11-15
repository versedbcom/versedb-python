from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_pull_list_issue_covers_response_200_data_options_item import (
        SetPullListIssueCoversResponse200DataOptionsItem,
    )


T = TypeVar("T", bound="SetPullListIssueCoversResponse200Data")


@_attrs_define
class SetPullListIssueCoversResponse200Data:
    """
    Attributes:
        issue_id (int):
        series_id (int | None):
        skipped (bool): The issue is skipped; saving covers adds it back to the pull.
        linked_shop (None | str): The linked Retail shop the series comes from, whose box follows the shop's own list;
            null without one.
        options (list[SetPullListIssueCoversResponse200DataOptionsItem]): The main cover first, then regular covers,
            ratio covers and exclusives.
    """

    issue_id: int
    series_id: int | None
    skipped: bool
    linked_shop: None | str
    options: list[SetPullListIssueCoversResponse200DataOptionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        series_id: int | None
        series_id = self.series_id

        skipped = self.skipped

        linked_shop: None | str
        linked_shop = self.linked_shop

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "series_id": series_id,
                "skipped": skipped,
                "linked_shop": linked_shop,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_pull_list_issue_covers_response_200_data_options_item import (
            SetPullListIssueCoversResponse200DataOptionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        skipped = d.pop("skipped")

        def _parse_linked_shop(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_shop = _parse_linked_shop(d.pop("linked_shop"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = SetPullListIssueCoversResponse200DataOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        set_pull_list_issue_covers_response_200_data = cls(
            issue_id=issue_id,
            series_id=series_id,
            skipped=skipped,
            linked_shop=linked_shop,
            options=options,
        )

        set_pull_list_issue_covers_response_200_data.additional_properties = d
        return set_pull_list_issue_covers_response_200_data

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
