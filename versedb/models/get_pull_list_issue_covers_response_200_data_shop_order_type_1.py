from typing import Literal

GetPullListIssueCoversResponse200DataShopOrderType1 = Literal["open", "set"]

GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_1_VALUES: set[
    GetPullListIssueCoversResponse200DataShopOrderType1
] = {
    "open",
    "set",
}


def check_get_pull_list_issue_covers_response_200_data_shop_order_type_1(
    value: str,
) -> GetPullListIssueCoversResponse200DataShopOrderType1:
    if value in GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_SHOP_ORDER_TYPE_1_VALUES!r}"
    )
