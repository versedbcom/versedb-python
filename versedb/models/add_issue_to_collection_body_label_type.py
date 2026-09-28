from typing import Literal

AddIssueToCollectionBodyLabelType = Literal[
    "cgcxjsa",
    "conserved",
    "qualified",
    "restored",
    "signature_series",
    "signed",
    "standard",
    "universal",
    "verified_signature",
]

ADD_ISSUE_TO_COLLECTION_BODY_LABEL_TYPE_VALUES: set[AddIssueToCollectionBodyLabelType] = {
    "cgcxjsa",
    "conserved",
    "qualified",
    "restored",
    "signature_series",
    "signed",
    "standard",
    "universal",
    "verified_signature",
}


def check_add_issue_to_collection_body_label_type(value: str) -> AddIssueToCollectionBodyLabelType:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_LABEL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_LABEL_TYPE_VALUES!r}")
