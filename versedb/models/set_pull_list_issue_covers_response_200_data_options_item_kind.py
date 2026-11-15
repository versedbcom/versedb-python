from typing import Literal

SetPullListIssueCoversResponse200DataOptionsItemKind = Literal["exclusive", "ratio", "regular"]

SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES: set[
    SetPullListIssueCoversResponse200DataOptionsItemKind
] = {
    "exclusive",
    "ratio",
    "regular",
}


def check_set_pull_list_issue_covers_response_200_data_options_item_kind(
    value: str,
) -> SetPullListIssueCoversResponse200DataOptionsItemKind:
    if value in SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_OPTIONS_ITEM_KIND_VALUES!r}"
    )
