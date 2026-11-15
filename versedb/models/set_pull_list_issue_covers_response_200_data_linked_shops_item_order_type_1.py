from typing import Literal

SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1 = Literal["open", "set"]

SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_1_VALUES: set[
    SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1
] = {
    "open",
    "set",
}


def check_set_pull_list_issue_covers_response_200_data_linked_shops_item_order_type_1(
    value: str,
) -> SetPullListIssueCoversResponse200DataLinkedShopsItemOrderType1:
    if value in SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_LINKED_SHOPS_ITEM_ORDER_TYPE_1_VALUES!r}"
    )
