from typing import Literal

AddIssueToCollectionResponse409Error = Literal["add_in_progress", "copy_removed"]

ADD_ISSUE_TO_COLLECTION_RESPONSE_409_ERROR_VALUES: set[AddIssueToCollectionResponse409Error] = {
    "add_in_progress",
    "copy_removed",
}


def check_add_issue_to_collection_response_409_error(value: str) -> AddIssueToCollectionResponse409Error:
    if value in ADD_ISSUE_TO_COLLECTION_RESPONSE_409_ERROR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_RESPONSE_409_ERROR_VALUES!r}"
    )
