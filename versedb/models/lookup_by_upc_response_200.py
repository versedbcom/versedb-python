from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_by_upc_response_200_data import LookupByUpcResponse200Data
    from ..models.lookup_by_upc_response_200_variants_item import LookupByUpcResponse200VariantsItem


T = TypeVar("T", bound="LookupByUpcResponse200")


@_attrs_define
class LookupByUpcResponse200:
    """
    Attributes:
        data (LookupByUpcResponse200Data | Unset):
        suggested_variant_id (int | Unset):
        variants (list[LookupByUpcResponse200VariantsItem] | Unset):
    """

    data: LookupByUpcResponse200Data | Unset = UNSET
    suggested_variant_id: int | Unset = UNSET
    variants: list[LookupByUpcResponse200VariantsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        suggested_variant_id = self.suggested_variant_id

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if suggested_variant_id is not UNSET:
            field_dict["suggested_variant_id"] = suggested_variant_id
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_upc_response_200_data import LookupByUpcResponse200Data  # noqa: PLC0415
        from ..models.lookup_by_upc_response_200_variants_item import (
            LookupByUpcResponse200VariantsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: LookupByUpcResponse200Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = LookupByUpcResponse200Data.from_dict(_data)

        suggested_variant_id = d.pop("suggested_variant_id", UNSET)

        _variants = d.pop("variants", UNSET)
        variants: list[LookupByUpcResponse200VariantsItem] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = LookupByUpcResponse200VariantsItem.from_dict(variants_item_data)

                variants.append(variants_item)

        lookup_by_upc_response_200 = cls(
            data=data,
            suggested_variant_id=suggested_variant_id,
            variants=variants,
        )

        lookup_by_upc_response_200.additional_properties = d
        return lookup_by_upc_response_200

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
