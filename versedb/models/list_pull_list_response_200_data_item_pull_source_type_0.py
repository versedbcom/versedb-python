from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListPullListResponse200DataItemPullSourceType0")


@_attrs_define
class ListPullListResponse200DataItemPullSourceType0:
    """Left out for a `read:showcase` token.

    Attributes:
        id (int):
        name (str):
        kind (str):
        kind_label (str):
        has_pickup (bool):
        comic_shop_id (int | None):
        location (None | str):
        pickup_note (None | str):
        is_default (bool):
        is_linked (bool): True when the source is a shop's own link to the member's account.
        shop_link_id (int | None):
        sort (int):
        created_at (None | str):
        updated_at (None | str):
    """

    id: int
    name: str
    kind: str
    kind_label: str
    has_pickup: bool
    comic_shop_id: int | None
    location: None | str
    pickup_note: None | str
    is_default: bool
    is_linked: bool
    shop_link_id: int | None
    sort: int
    created_at: None | str
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        kind = self.kind

        kind_label = self.kind_label

        has_pickup = self.has_pickup

        comic_shop_id: int | None
        comic_shop_id = self.comic_shop_id

        location: None | str
        location = self.location

        pickup_note: None | str
        pickup_note = self.pickup_note

        is_default = self.is_default

        is_linked = self.is_linked

        shop_link_id: int | None
        shop_link_id = self.shop_link_id

        sort = self.sort

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "kind_label": kind_label,
                "has_pickup": has_pickup,
                "comic_shop_id": comic_shop_id,
                "location": location,
                "pickup_note": pickup_note,
                "is_default": is_default,
                "is_linked": is_linked,
                "shop_link_id": shop_link_id,
                "sort": sort,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        kind = d.pop("kind")

        kind_label = d.pop("kind_label")

        has_pickup = d.pop("has_pickup")

        def _parse_comic_shop_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        comic_shop_id = _parse_comic_shop_id(d.pop("comic_shop_id"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_pickup_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pickup_note = _parse_pickup_note(d.pop("pickup_note"))

        is_default = d.pop("is_default")

        is_linked = d.pop("is_linked")

        def _parse_shop_link_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        shop_link_id = _parse_shop_link_id(d.pop("shop_link_id"))

        sort = d.pop("sort")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        list_pull_list_response_200_data_item_pull_source_type_0 = cls(
            id=id,
            name=name,
            kind=kind,
            kind_label=kind_label,
            has_pickup=has_pickup,
            comic_shop_id=comic_shop_id,
            location=location,
            pickup_note=pickup_note,
            is_default=is_default,
            is_linked=is_linked,
            shop_link_id=shop_link_id,
            sort=sort,
            created_at=created_at,
            updated_at=updated_at,
        )

        list_pull_list_response_200_data_item_pull_source_type_0.additional_properties = d
        return list_pull_list_response_200_data_item_pull_source_type_0

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
