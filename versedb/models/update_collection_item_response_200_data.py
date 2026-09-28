from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCollectionItemResponse200Data")


@_attrs_define
class UpdateCollectionItemResponse200Data:
    """
    Attributes:
        id (int | Unset):
        condition (str | Unset):
        price_paid (float | Unset):
        graded (bool | Unset):
    """

    id: int | Unset = UNSET
    condition: str | Unset = UNSET
    price_paid: float | Unset = UNSET
    graded: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        condition = self.condition

        price_paid = self.price_paid

        graded = self.graded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
        if graded is not UNSET:
            field_dict["graded"] = graded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        condition = d.pop("condition", UNSET)

        price_paid = d.pop("price_paid", UNSET)

        graded = d.pop("graded", UNSET)

        update_collection_item_response_200_data = cls(
            id=id,
            condition=condition,
            price_paid=price_paid,
            graded=graded,
        )

        update_collection_item_response_200_data.additional_properties = d
        return update_collection_item_response_200_data

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
