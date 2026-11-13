from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_by_distributor_code_response_200_data import LookupByDistributorCodeResponse200Data
    from ..models.lookup_by_distributor_code_response_200_variants_item import (
        LookupByDistributorCodeResponse200VariantsItem,
    )


T = TypeVar("T", bound="LookupByDistributorCodeResponse200")


@_attrs_define
class LookupByDistributorCodeResponse200:
    """
    Attributes:
        data (LookupByDistributorCodeResponse200Data):
        suggested_variant_id (int | None):
        variants (list[LookupByDistributorCodeResponse200VariantsItem]):
    """

    data: LookupByDistributorCodeResponse200Data
    suggested_variant_id: int | None
    variants: list[LookupByDistributorCodeResponse200VariantsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        suggested_variant_id: int | None
        suggested_variant_id = self.suggested_variant_id

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "suggested_variant_id": suggested_variant_id,
                "variants": variants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_distributor_code_response_200_data import LookupByDistributorCodeResponse200Data  # noqa: PLC0415
        from ..models.lookup_by_distributor_code_response_200_variants_item import (
            LookupByDistributorCodeResponse200VariantsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LookupByDistributorCodeResponse200Data.from_dict(d.pop("data"))

        def _parse_suggested_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        suggested_variant_id = _parse_suggested_variant_id(d.pop("suggested_variant_id"))

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = LookupByDistributorCodeResponse200VariantsItem.from_dict(variants_item_data)

            variants.append(variants_item)

        lookup_by_distributor_code_response_200 = cls(
            data=data,
            suggested_variant_id=suggested_variant_id,
            variants=variants,
        )

        lookup_by_distributor_code_response_200.additional_properties = d
        return lookup_by_distributor_code_response_200

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
