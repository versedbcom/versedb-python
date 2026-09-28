from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookupByUpcResponse409MatchesItemVariantsItem")


@_attrs_define
class LookupByUpcResponse409MatchesItemVariantsItem:
    """
    Attributes:
        variant_id (None | str | Unset):
        variant_name (str | Unset):
        cover_url (str | Unset):
        upc (str | Unset):
    """

    variant_id: None | str | Unset = UNSET
    variant_name: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    upc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        variant_name = self.variant_name

        cover_url = self.cover_url

        upc = self.upc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if variant_name is not UNSET:
            field_dict["variant_name"] = variant_name
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if upc is not UNSET:
            field_dict["upc"] = upc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        variant_name = d.pop("variant_name", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        upc = d.pop("upc", UNSET)

        lookup_by_upc_response_409_matches_item_variants_item = cls(
            variant_id=variant_id,
            variant_name=variant_name,
            cover_url=cover_url,
            upc=upc,
        )

        lookup_by_upc_response_409_matches_item_variants_item.additional_properties = d
        return lookup_by_upc_response_409_matches_item_variants_item

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
