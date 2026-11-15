from typing import Literal

CheckIssueInCollectionResponse200CopiesItemCoverKind = Literal["catalog", "custom", "main"]

CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_COPIES_ITEM_COVER_KIND_VALUES: set[
    CheckIssueInCollectionResponse200CopiesItemCoverKind
] = {
    "catalog",
    "custom",
    "main",
}


def check_check_issue_in_collection_response_200_copies_item_cover_kind(
    value: str,
) -> CheckIssueInCollectionResponse200CopiesItemCoverKind:
    if value in CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_COPIES_ITEM_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_ISSUE_IN_COLLECTION_RESPONSE_200_COPIES_ITEM_COVER_KIND_VALUES!r}"
    )
