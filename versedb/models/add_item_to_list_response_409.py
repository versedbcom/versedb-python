from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_item_to_list_response_409_item import AddItemToListResponse409Item


T = TypeVar("T", bound="AddItemToListResponse409")


@_attrs_define
class AddItemToListResponse409:
    """
    Attributes:
        message (str | Unset):
        item (AddItemToListResponse409Item | Unset):
    """

    message: str | Unset = UNSET
    item: AddItemToListResponse409Item | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_item_to_list_response_409_item import AddItemToListResponse409Item  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _item = d.pop("item", UNSET)
        item: AddItemToListResponse409Item | Unset
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = AddItemToListResponse409Item.from_dict(_item)

        add_item_to_list_response_409 = cls(
            message=message,
            item=item,
        )

        add_item_to_list_response_409.additional_properties = d
        return add_item_to_list_response_409

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
