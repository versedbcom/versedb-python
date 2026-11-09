from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCreatorsIssuesResponse200Links")


@_attrs_define
class GetCreatorsIssuesResponse200Links:
    """
    Attributes:
        first (str):
        last (str):
        prev (None | str):
        next_ (None | str):
    """

    first: str
    last: str
    prev: None | str
    next_: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first = self.first

        last = self.last

        prev: None | str
        prev = self.prev

        next_: None | str
        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first": first,
                "last": last,
                "prev": prev,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first = d.pop("first")

        last = d.pop("last")

        def _parse_prev(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev = _parse_prev(d.pop("prev"))

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        get_creators_issues_response_200_links = cls(
            first=first,
            last=last,
            prev=prev,
            next_=next_,
        )

        get_creators_issues_response_200_links.additional_properties = d
        return get_creators_issues_response_200_links

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
