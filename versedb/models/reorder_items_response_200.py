from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reorder_items_response_200_items_item import ReorderItemsResponse200ItemsItem


T = TypeVar("T", bound="ReorderItemsResponse200")


@_attrs_define
class ReorderItemsResponse200:
    """
    Attributes:
        message (str | Unset):
        items (list[ReorderItemsResponse200ItemsItem] | Unset):
    """

    message: str | Unset = UNSET
    items: list[ReorderItemsResponse200ItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_items_response_200_items_item import ReorderItemsResponse200ItemsItem  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _items = d.pop("items", UNSET)
        items: list[ReorderItemsResponse200ItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ReorderItemsResponse200ItemsItem.from_dict(items_item_data)

                items.append(items_item)

        reorder_items_response_200 = cls(
            message=message,
            items=items,
        )

        reorder_items_response_200.additional_properties = d
        return reorder_items_response_200

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
