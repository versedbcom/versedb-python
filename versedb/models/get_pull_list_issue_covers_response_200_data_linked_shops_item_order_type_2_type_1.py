from typing import Literal

GetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1 = Literal["open", "set"]

GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_2_TYPE_1_VALUES: set[
    GetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1
] = {
    "open",
    "set",
}


def check_get_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_2_type_1(
    value: str,
) -> GetPullListIssueCoversResponse200DataLinkedShopsItemOrderType2Type1:
    if value in GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_2_TYPE_1_VALUES!r}"
    )
