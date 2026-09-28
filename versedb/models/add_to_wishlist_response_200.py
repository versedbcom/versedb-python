from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddToWishlistResponse200")


@_attrs_define
class AddToWishlistResponse200:
    """
    Attributes:
        in_wishlist (bool | Unset):
        variant_id (int | Unset):
    """

    in_wishlist: bool | Unset = UNSET
    variant_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_wishlist = self.in_wishlist

        variant_id = self.variant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_wishlist is not UNSET:
            field_dict["in_wishlist"] = in_wishlist
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_wishlist = d.pop("in_wishlist", UNSET)

        variant_id = d.pop("variant_id", UNSET)

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
