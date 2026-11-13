from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupByDistributorCodeResponse409MatchesItemVariantsItem")


@_attrs_define
class LookupByDistributorCodeResponse409MatchesItemVariantsItem:
    """
    Attributes:
        variant_id (int | None):
        variant_name (str):
        cover_url (None | str):
        upc (None | str):
        lunar_code (None | str):
        universal_code (None | str):
        diamond_code (None | str):
    """

    variant_id: int | None
    variant_name: str
    cover_url: None | str
    upc: None | str
    lunar_code: None | str
    universal_code: None | str
    diamond_code: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id: int | None
        variant_id = self.variant_id

        variant_name = self.variant_name

        cover_url: None | str
        cover_url = self.cover_url

        upc: None | str
        upc = self.upc

        lunar_code: None | str
        lunar_code = self.lunar_code

        universal_code: None | str
        universal_code = self.universal_code

        diamond_code: None | str
        diamond_code = self.diamond_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant_id": variant_id,
                "variant_name": variant_name,
                "cover_url": cover_url,
                "upc": upc,
                "lunar_code": lunar_code,
                "universal_code": universal_code,
                "diamond_code": diamond_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        variant_name = d.pop("variant_name")

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_upc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upc = _parse_upc(d.pop("upc"))

        def _parse_lunar_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lunar_code = _parse_lunar_code(d.pop("lunar_code"))

        def _parse_universal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        universal_code = _parse_universal_code(d.pop("universal_code"))

        def _parse_diamond_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        diamond_code = _parse_diamond_code(d.pop("diamond_code"))

        lookup_by_distributor_code_response_409_matches_item_variants_item = cls(
            variant_id=variant_id,
            variant_name=variant_name,
            cover_url=cover_url,
            upc=upc,
            lunar_code=lunar_code,
            universal_code=universal_code,
            diamond_code=diamond_code,
        )

        lookup_by_distributor_code_response_409_matches_item_variants_item.additional_properties = d
        return lookup_by_distributor_code_response_409_matches_item_variants_item

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
