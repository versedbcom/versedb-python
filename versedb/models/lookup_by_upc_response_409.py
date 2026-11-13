from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_by_upc_response_409_matches_item import LookupByUpcResponse409MatchesItem


T = TypeVar("T", bound="LookupByUpcResponse409")


@_attrs_define
class LookupByUpcResponse409:
    """
    Attributes:
        message (str):
        count (int):
        total_count (int):
        matches (list[LookupByUpcResponse409MatchesItem]):
    """

    message: str
    count: int
    total_count: int
    matches: list[LookupByUpcResponse409MatchesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        count = self.count

        total_count = self.total_count

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "count": count,
                "total_count": total_count,
                "matches": matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_upc_response_409_matches_item import LookupByUpcResponse409MatchesItem  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message")

        count = d.pop("count")

        total_count = d.pop("total_count")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = LookupByUpcResponse409MatchesItem.from_dict(matches_item_data)

            matches.append(matches_item)

        lookup_by_upc_response_409 = cls(
            message=message,
            count=count,
            total_count=total_count,
            matches=matches,
        )

        lookup_by_upc_response_409.additional_properties = d
        return lookup_by_upc_response_409

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
