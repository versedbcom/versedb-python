from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue import (
        ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue,
    )


T = TypeVar("T", bound="ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItem")


@_attrs_define
class ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItem:
    """
    Attributes:
        issue (ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue):
        percent (float):
    """

    issue: ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue = self.issue.to_dict()

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue": issue,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue import (
            ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue = ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssue.from_dict(d.pop("issue"))

        percent = d.pop("percent")

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item = cls(
            issue=issue,
            percent=percent,
        )

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item.additional_properties = d
        return view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item

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
