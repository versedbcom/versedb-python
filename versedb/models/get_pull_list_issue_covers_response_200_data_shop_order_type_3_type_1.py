from typing import Literal

GetPullListIssueCoversResponse200DataShopOrderType3Type1 = Literal["open", "set"]

GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_3_TYPE_1_VALUES: set[
    GetPullListIssueCoversResponse200DataShopOrderType3Type1
] = {
    "open",
    "set",
}


def check_get_pull_list_issue_covers_response_200_data_shop_order_type_3_type_1(
    value: str,
) -> GetPullListIssueCoversResponse200DataShopOrderType3Type1:
    if value in GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_3_TYPE_1_VALUES!r}"
    )
