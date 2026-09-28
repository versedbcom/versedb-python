from typing import Literal

AddIssueToCollectionBodyStatus = Literal["for_sale", "owned", "sold"]

ADD_ISSUE_TO_COLLECTION_BODY_STATUS_VALUES: set[AddIssueToCollectionBodyStatus] = {
    "for_sale",
    "owned",
    "sold",
}


def check_add_issue_to_collection_body_status(value: str) -> AddIssueToCollectionBodyStatus:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_STATUS_VALUES!r}")
