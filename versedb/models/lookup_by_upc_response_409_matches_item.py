from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_by_upc_response_409_matches_item_variants_item import (
        LookupByUpcResponse409MatchesItemVariantsItem,
    )


T = TypeVar("T", bound="LookupByUpcResponse409MatchesItem")


@_attrs_define
class LookupByUpcResponse409MatchesItem:
    """
    Attributes:
        issue_id (int):
        series_name (None | str):
        series_id (int | None):
        issue_number (None | str):
        cover_url (None | str):
        variant_name (None):
        suggested_variant_id (int | None):
        variants (list[LookupByUpcResponse409MatchesItemVariantsItem]):
        publisher_name (None | str):
        release_date (None | str):
        start_year (int | None):
    """

    issue_id: int
    series_name: None | str
    series_id: int | None
    issue_number: None | str
    cover_url: None | str
    variant_name: None
    suggested_variant_id: int | None
    variants: list[LookupByUpcResponse409MatchesItemVariantsItem]
    publisher_name: None | str
    release_date: None | str
    start_year: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        series_name: None | str
        series_name = self.series_name

        series_id: int | None
        series_id = self.series_id

        issue_number: None | str
        issue_number = self.issue_number

        cover_url: None | str
        cover_url = self.cover_url

        variant_name = self.variant_name

        suggested_variant_id: int | None
        suggested_variant_id = self.suggested_variant_id

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        publisher_name: None | str
        publisher_name = self.publisher_name

        release_date: None | str
        release_date = self.release_date

        start_year: int | None
        start_year = self.start_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "series_name": series_name,
                "series_id": series_id,
                "issue_number": issue_number,
                "cover_url": cover_url,
                "variant_name": variant_name,
                "suggested_variant_id": suggested_variant_id,
                "variants": variants,
                "publisher_name": publisher_name,
                "release_date": release_date,
                "start_year": start_year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_upc_response_409_matches_item_variants_item import (
            LookupByUpcResponse409MatchesItemVariantsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        def _parse_series_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_name = _parse_series_name(d.pop("series_name"))

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        variant_name = d.pop("variant_name")

        def _parse_suggested_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        suggested_variant_id = _parse_suggested_variant_id(d.pop("suggested_variant_id"))

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = LookupByUpcResponse409MatchesItemVariantsItem.from_dict(variants_item_data)

            variants.append(variants_item)

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name"))

        def _parse_release_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        release_date = _parse_release_date(d.pop("release_date"))

        def _parse_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        start_year = _parse_start_year(d.pop("start_year"))

        lookup_by_upc_response_409_matches_item = cls(
            issue_id=issue_id,
            series_name=series_name,
            series_id=series_id,
            issue_number=issue_number,
            cover_url=cover_url,
            variant_name=variant_name,
            suggested_variant_id=suggested_variant_id,
            variants=variants,
            publisher_name=publisher_name,
            release_date=release_date,
            start_year=start_year,
        )

        lookup_by_upc_response_409_matches_item.additional_properties = d
        return lookup_by_upc_response_409_matches_item

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
