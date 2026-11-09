from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StopAListUpdatingItselfResponse200DataItemsItemEntityType0SeriesType0")


@_attrs_define
class StopAListUpdatingItselfResponse200DataItemsItemEntityType0SeriesType0:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        start_year (int | None):
    """

    id: int
    name: None | str
    slug: None | str
    start_year: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        start_year: int | None
        start_year = self.start_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "start_year": start_year,
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

        def _parse_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        start_year = _parse_start_year(d.pop("start_year"))

        stop_a_list_updating_itself_response_200_data_items_item_entity_type_0_series_type_0 = cls(
            id=id,
            name=name,
            slug=slug,
            start_year=start_year,
        )

        stop_a_list_updating_itself_response_200_data_items_item_entity_type_0_series_type_0.additional_properties = d
        return stop_a_list_updating_itself_response_200_data_items_item_entity_type_0_series_type_0

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
