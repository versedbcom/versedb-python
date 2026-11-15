from typing import Literal

CheckIssueInCollectionResponse200DataType0CoverKind = Literal["catalog", "custom", "main"]

CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_DATA_TYPE_0_COVER_KIND_VALUES: set[
    CheckIssueInCollectionResponse200DataType0CoverKind
] = {
    "catalog",
    "custom",
    "main",
}


def check_check_issue_in_collection_response_200_data_type_0_cover_kind(
    value: str,
) -> CheckIssueInCollectionResponse200DataType0CoverKind:
    if value in CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_DATA_TYPE_0_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_DATA_TYPE_0_COVER_KIND_VALUES!r}"
    )
