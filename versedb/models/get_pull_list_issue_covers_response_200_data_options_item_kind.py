from typing import Literal

GetPullListIssueCoversResponse200DataOptionsItemKind = Literal["exclusive", "ratio", "regular"]

GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES: set[
    GetPullListIssueCoversResponse200DataOptionsItemKind
] = {
    "exclusive",
    "ratio",
    "regular",
}


def check_get_pull_list_issue_covers_response_200_data_options_item_kind(
    value: str,
) -> GetPullListIssueCoversResponse200DataOptionsItemKind:
    if value in GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES!r}"
    )
