from typing import Literal

SetPullListIssueCoversResponse200DataStanding = Literal["regular", "standard", "standard_and_regular"]

SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES: set[SetPullListIssueCoversResponse200DataStanding] = {
    "regular",
    "standard",
    "standard_and_regular",
}


def check_set_pull_list_issue_covers_response_200_data_standing(
    value: str,
) -> SetPullListIssueCoversResponse200DataStanding:
    if value in SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_PULL_LIST_ISSUE_COVERS_RESPONSE_200_DATA_STANDING_VALUES!r}"
    )
