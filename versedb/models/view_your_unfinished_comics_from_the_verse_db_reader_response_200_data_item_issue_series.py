from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries")


@_attrs_define
class ViewYourUnfinishedComicsFromTheVerseDbReaderResponse200DataItemIssueSeries:
    """
    Attributes:
        name (None | str):
        publisher_name (None | str):
    """

    name: None | str
    publisher_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        publisher_name: None | str
        publisher_name = self.publisher_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "publisher_name": publisher_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name"))

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue_series = cls(
            name=name,
            publisher_name=publisher_name,
        )

        view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue_series.additional_properties = d
        return view_your_unfinished_comics_from_the_verse_db_reader_response_200_data_item_issue_series

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
