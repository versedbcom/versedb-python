from typing import Literal

AddIssueToCollectionBodyAcquisitionMethod = Literal[
    "found", "gift", "inheritance", "other", "purchase", "subscription", "trade"
]

ADD_ISSUE_TO_COLLECTION_BODY_ACQUISITION_METHOD_VALUES: set[AddIssueToCollectionBodyAcquisitionMethod] = {
    "found",
    "gift",
    "inheritance",
    "other",
    "purchase",
    "subscription",
    "trade",
}


def check_add_issue_to_collection_body_acquisition_method(value: str) -> AddIssueToCollectionBodyAcquisitionMethod:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_ACQUISITION_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_ACQUISITION_METHOD_VALUES!r}"
    )
