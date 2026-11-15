from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_pull_list_issue_covers_response_200_data_shop_order_type_1 import (
    SetPullListIssueCoversResponse200DataShopOrderType1,
    check_set_pull_list_issue_covers_response_200_data_shop_order_type_1,
)
from ..models.set_pull_list_issue_covers_response_200_data_shop_order_type_2_type_1 import (
    SetPullListIssueCoversResponse200DataShopOrderType2Type1,
    check_set_pull_list_issue_covers_response_200_data_shop_order_type_2_type_1,
)
from ..models.set_pull_list_issue_covers_response_200_data_shop_order_type_3_type_1 import (
    SetPullListIssueCoversResponse200DataShopOrderType3Type1,
    check_set_pull_list_issue_covers_response_200_data_shop_order_type_3_type_1,
)
from ..models.set_pull_list_issue_covers_response_200_data_standing import (
    SetPullListIssueCoversResponse200DataStanding,
    check_set_pull_list_issue_covers_response_200_data_standing,
)

if TYPE_CHECKING:
    from ..models.set_pull_list_issue_covers_response_200_data_linked_shops_item import (
        SetPullListIssueCoversResponse200DataLinkedShopsItem,
    )
    from ..models.set_pull_list_issue_covers_response_200_data_options_item import (
        SetPullListIssueCoversResponse200DataOptionsItem,
    )


T = TypeVar("T", bound="SetPullListIssueCoversResponse200Data")


@_attrs_define
class SetPullListIssueCoversResponse200Data:
    """
    Attributes:
        issue_id (int):
        series_id (int | None):
        skipped (bool): The issue is skipped; saving covers adds it back to the pull.
        linked_shops (list[SetPullListIssueCoversResponse200DataLinkedShopsItem]): Every linked Retail shop the series
            comes from, in the user's order of pull sources; empty without one. A save that changes the covers reaches each
            shop whose order is `open`, and an unchanged one writes nothing there; a return to the usual covers clears the
            shop's own choice for the issue, so the shop's usual covers apply, and an unskip that follows the series lifts
            only the shop's skip.
        linked_shop (None | str): The first of `linked_shops`: its name; null without a linked shop.
        shop_order (None | SetPullListIssueCoversResponse200DataShopOrderType1 |
            SetPullListIssueCoversResponse200DataShopOrderType2Type1 |
            SetPullListIssueCoversResponse200DataShopOrderType3Type1): The first of `linked_shops`: its `order`; null
            without a linked shop.
        options (list[SetPullListIssueCoversResponse200DataOptionsItem]): The main cover first, then regular covers,
            ratio covers and exclusives.
        follows_series (bool): The issue has no covers chosen of its own, so `selected` follows the series' standing
            choice.
        standing (SetPullListIssueCoversResponse200DataStanding): The series' standing cover choice
            (`updatePullListItem`'s `preferred_cover_type`).
    """

    issue_id: int
    series_id: int | None
    skipped: bool
    linked_shops: list[SetPullListIssueCoversResponse200DataLinkedShopsItem]
    linked_shop: None | str
    shop_order: (
        None
        | SetPullListIssueCoversResponse200DataShopOrderType1
        | SetPullListIssueCoversResponse200DataShopOrderType2Type1
        | SetPullListIssueCoversResponse200DataShopOrderType3Type1
    )
    options: list[SetPullListIssueCoversResponse200DataOptionsItem]
    follows_series: bool
    standing: SetPullListIssueCoversResponse200DataStanding
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        series_id: int | None
        series_id = self.series_id

        skipped = self.skipped

        linked_shops = []
        for linked_shops_item_data in self.linked_shops:
            linked_shops_item = linked_shops_item_data.to_dict()
            linked_shops.append(linked_shops_item)

        linked_shop: None | str
        linked_shop = self.linked_shop

        shop_order: None | str
        if isinstance(self.shop_order, str):
            shop_order = self.shop_order
        elif isinstance(self.shop_order, str):
            shop_order = self.shop_order
        elif isinstance(self.shop_order, str):
            shop_order = self.shop_order
        else:
            shop_order = self.shop_order

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        follows_series = self.follows_series

        standing: str = self.standing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "series_id": series_id,
                "skipped": skipped,
                "linked_shops": linked_shops,
                "linked_shop": linked_shop,
                "shop_order": shop_order,
                "options": options,
                "follows_series": follows_series,
                "standing": standing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_pull_list_issue_covers_response_200_data_linked_shops_item import (
            SetPullListIssueCoversResponse200DataLinkedShopsItem,  # noqa: PLC0415
        )
        from ..models.set_pull_list_issue_covers_response_200_data_options_item import (
            SetPullListIssueCoversResponse200DataOptionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        skipped = d.pop("skipped")

        linked_shops = []
        _linked_shops = d.pop("linked_shops")
        for linked_shops_item_data in _linked_shops:
            linked_shops_item = SetPullListIssueCoversResponse200DataLinkedShopsItem.from_dict(linked_shops_item_data)

            linked_shops.append(linked_shops_item)

        def _parse_linked_shop(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_shop = _parse_linked_shop(d.pop("linked_shop"))

        def _parse_shop_order(
            data: object,
        ) -> (
            None
            | SetPullListIssueCoversResponse200DataShopOrderType1
            | SetPullListIssueCoversResponse200DataShopOrderType2Type1
            | SetPullListIssueCoversResponse200DataShopOrderType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shop_order_type_1 = check_set_pull_list_issue_covers_response_200_data_shop_order_type_1(data)

                return shop_order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shop_order_type_2_type_1 = check_set_pull_list_issue_covers_response_200_data_shop_order_type_2_type_1(
                    data
                )

                return shop_order_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shop_order_type_3_type_1 = check_set_pull_list_issue_covers_response_200_data_shop_order_type_3_type_1(
                    data
                )

                return shop_order_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SetPullListIssueCoversResponse200DataShopOrderType1
                | SetPullListIssueCoversResponse200DataShopOrderType2Type1
                | SetPullListIssueCoversResponse200DataShopOrderType3Type1,
                data,
            )

        shop_order = _parse_shop_order(d.pop("shop_order"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = SetPullListIssueCoversResponse200DataOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        follows_series = d.pop("follows_series")

        standing = check_set_pull_list_issue_covers_response_200_data_standing(d.pop("standing"))

        set_pull_list_issue_covers_response_200_data = cls(
            issue_id=issue_id,
            series_id=series_id,
            skipped=skipped,
            linked_shops=linked_shops,
            linked_shop=linked_shop,
            shop_order=shop_order,
            options=options,
            follows_series=follows_series,
            standing=standing,
        )

        set_pull_list_issue_covers_response_200_data.additional_properties = d
        return set_pull_list_issue_covers_response_200_data

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
