from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupByDistributorCodeResponse200DataComicEventsItem")


@_attrs_define
class LookupByDistributorCodeResponse200DataComicEventsItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        type_ (None | str):
        notes (None | str):
        display_order (int | None):
    """

    id: int
    name: None | str
    slug: None | str
    type_: None | str
    notes: None | str
    display_order: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        type_: None | str
        type_ = self.type_

        notes: None | str
        notes = self.notes

        display_order: int | None
        display_order = self.display_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "notes": notes,
                "display_order": display_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

        def _parse_display_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        display_order = _parse_display_order(d.pop("display_order"))

        lookup_by_distributor_code_response_200_data_comic_events_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            notes=notes,
            display_order=display_order,
        )

        lookup_by_distributor_code_response_200_data_comic_events_item.additional_properties = d
        return lookup_by_distributor_code_response_200_data_comic_events_item

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
