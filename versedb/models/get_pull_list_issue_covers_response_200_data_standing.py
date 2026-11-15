from typing import Literal

GetPullListIssueCoversResponse200DataStanding = Literal["regular", "standard", "standard_and_regular"]

GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES: set[GetPullListIssueCoversResponse200DataStanding] = {
    "regular",
    "standard",
    "standard_and_regular",
}


def check_get_pull_list_issue_covers_response_200_data_standing(
    value: str,
) -> GetPullListIssueCoversResponse200DataStanding:
    if value in GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES!r}"
    )
