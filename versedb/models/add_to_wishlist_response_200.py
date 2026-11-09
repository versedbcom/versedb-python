from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddToWishlistResponse200")


@_attrs_define
class AddToWishlistResponse200:
    """
    Attributes:
        in_wishlist (bool):
        variant_id (int | None):
    """

    in_wishlist: bool
    variant_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_wishlist = self.in_wishlist

        variant_id: int | None
        variant_id = self.variant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in_wishlist": in_wishlist,
                "variant_id": variant_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_wishlist = d.pop("in_wishlist")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        add_to_wishlist_response_200 = cls(
            in_wishlist=in_wishlist,
            variant_id=variant_id,
        )

        add_to_wishlist_response_200.additional_properties = d
        return add_to_wishlist_response_200

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
