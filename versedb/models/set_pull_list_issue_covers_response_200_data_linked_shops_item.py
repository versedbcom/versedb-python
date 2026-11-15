from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_1 import (
    SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1,
    check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_1,
)
from ..models.set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_2_type_1 import (
    SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1,
    check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_2_type_1,
)
from ..models.set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_3_type_1 import (
    SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType3Type1,
    check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_3_type_1,
)

T = TypeVar("T", bound="SetPullListIssueCoversResponse200DataLinkedShopsItem")


@_attrs_define
class SetPullListIssueCoversResponse200DataLinkedShopsItem:
    """
    Attributes:
        name (str):
        order (None | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1 |
            SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1 |
            SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType3Type1): Where the shop's order for this issue
            stands: `open` while a cover choice also goes on the user's list at the shop, `set` once the shop has ordered
            the issue (the choice stays on the user's VerseDB list); null when the issue isn't on the shop's list.
    """

    name: str
    order: (
        None
        | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1
        | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1
        | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType3Type1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        order: None | str
        if isinstance(self.order, str):
            order = self.order
        elif isinstance(self.order, str):
            order = self.order
        elif isinstance(self.order, str):
            order = self.order
        else:
            order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_order(
            data: object,
        ) -> (
            None
            | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1
            | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1
            | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_1 = check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_1(data)

                return order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_2_type_1 = (
                    check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_2_type_1(data)
                )

                return order_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_3_type_1 = (
                    check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_3_type_1(data)
                )

                return order_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1
                | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1
                | SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType3Type1,
                data,
            )

        order = _parse_order(d.pop("order"))

        set_pull_list_issue_covers_response_200_data_linked_shops_item = cls(
            name=name,
            order=order,
        )

        set_pull_list_issue_covers_response_200_data_linked_shops_item.additional_properties = d
        return set_pull_list_issue_covers_response_200_data_linked_shops_item

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
