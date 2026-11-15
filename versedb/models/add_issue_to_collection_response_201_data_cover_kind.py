from typing import Literal

AddIssueToCollectionResponse201DataCoverKind = Literal["catalog", "custom", "main"]

ADD_ISSUE_TO_COLLECTION_RESPONSE_201_DATA_COVER_KIND_VALUES: set[AddIssueToCollectionResponse201DataCoverKind] = {
    "catalog",
    "custom",
    "main",
}


def check_add_issue_to_collection_response_201_data_cover_kind(
    value: str,
) -> AddIssueToCollectionResponse201DataCoverKind:
    if value in ADD_ISSUE_TO_COLLECTION_RESPONSE_201_DATA_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_RESPONSE_201_DATA_COVER_KIND_VALUES!r}"
    )
