from typing import Literal

ListPullListResponse200DataItemNextIssueCoversItemKind = Literal["exclusive", "ratio", "regular"]

LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_NEXT_ISSUE_COVERS_ITEM_KIND_VALUES: set[
    ListPullListResponse200DataItemNextIssueCoversItemKind
] = {
    "exclusive",
    "ratio",
    "regular",
}


def check_list_pull_list_response_200_data_item_next_issue_covers_item_kind(
    value: str,
) -> ListPullListResponse200DataItemNextIssueCoversItemKind:
    if value in LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_NEXT_ISSUE_COVERS_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_NEXT_ISSUE_COVERS_ITEM_KIND_VALUES!r}"
    )
