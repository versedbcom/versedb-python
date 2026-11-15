from typing import Literal

SetPullListIssueCoversResponse200DataShopOrderType2Type1 = Literal["open", "set"]

SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_2_TYPE_1_VALUES: set[
    SetPullListIssueCoversResponse200DataShopOrderType2Type1
] = {
    "open",
    "set",
}


def check_set_pull_list_issue_covers_response_200_data_shop_order_type_2_type_1(
    value: str,
) -> SetPullListIssueCoversResponse200DataShopOrderType2Type1:
    if value in SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_2_TYPE_1_VALUES!r}"
    )
