from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_by_distributor_code_response_409_matches_item_variants_item import (
        LookupByDistributorCodeResponse409MatchesItemVariantsItem,
    )


T = TypeVar("T", bound="LookupByDistributorCodeResponse409MatchesItem")


@_attrs_define
class LookupByDistributorCodeResponse409MatchesItem:
    """
    Attributes:
        issue_id (int | Unset):
        series_name (str | Unset):
        series_id (int | Unset):
        issue_number (str | Unset):
        cover_url (str | Unset):
        variant_name (None | str | Unset):
        suggested_variant_id (None | str | Unset):
        variants (list[LookupByDistributorCodeResponse409MatchesItemVariantsItem] | Unset):
        publisher_name (str | Unset):
        release_date (str | Unset):
        start_year (int | Unset):
    """

    issue_id: int | Unset = UNSET
    series_name: str | Unset = UNSET
    series_id: int | Unset = UNSET
    issue_number: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    variant_name: None | str | Unset = UNSET
    suggested_variant_id: None | str | Unset = UNSET
    variants: list[LookupByDistributorCodeResponse409MatchesItemVariantsItem] | Unset = UNSET
    publisher_name: str | Unset = UNSET
    release_date: str | Unset = UNSET
    start_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        series_name = self.series_name

        series_id = self.series_id

        issue_number = self.issue_number

        cover_url = self.cover_url

        variant_name: None | str | Unset
        if isinstance(self.variant_name, Unset):
            variant_name = UNSET
        else:
            variant_name = self.variant_name

        suggested_variant_id: None | str | Unset
        if isinstance(self.suggested_variant_id, Unset):
            suggested_variant_id = UNSET
        else:
            suggested_variant_id = self.suggested_variant_id

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        publisher_name = self.publisher_name

        release_date = self.release_date

        start_year = self.start_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if series_name is not UNSET:
            field_dict["series_name"] = series_name
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if variant_name is not UNSET:
            field_dict["variant_name"] = variant_name
        if suggested_variant_id is not UNSET:
            field_dict["suggested_variant_id"] = suggested_variant_id
        if variants is not UNSET:
            field_dict["variants"] = variants
        if publisher_name is not UNSET:
            field_dict["publisher_name"] = publisher_name
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if start_year is not UNSET:
            field_dict["start_year"] = start_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_distributor_code_response_409_matches_item_variants_item import (
            LookupByDistributorCodeResponse409MatchesItemVariantsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id", UNSET)

        series_name = d.pop("series_name", UNSET)

        series_id = d.pop("series_id", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        def _parse_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_name = _parse_variant_name(d.pop("variant_name", UNSET))

        def _parse_suggested_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suggested_variant_id = _parse_suggested_variant_id(d.pop("suggested_variant_id", UNSET))

        _variants = d.pop("variants", UNSET)
        variants: list[LookupByDistributorCodeResponse409MatchesItemVariantsItem] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = LookupByDistributorCodeResponse409MatchesItemVariantsItem.from_dict(variants_item_data)

                variants.append(variants_item)

        publisher_name = d.pop("publisher_name", UNSET)

        release_date = d.pop("release_date", UNSET)

        start_year = d.pop("start_year", UNSET)

        lookup_by_distributor_code_response_409_matches_item = cls(
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

        lookup_by_distributor_code_response_409_matches_item.additional_properties = d
        return lookup_by_distributor_code_response_409_matches_item

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
