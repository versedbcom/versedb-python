from typing import Literal

AddIssueToCollectionBodySignatureWitness = Literal[
    "CBCS", "CGC", "JSA", "other", "PSA/DNA", "unwitnessed", "witnessed_in_person"
]

ADD_ISSUE_TO_COLLECTION_BODY_SIGNATURE_WITNESS_VALUES: set[AddIssueToCollectionBodySignatureWitness] = {
    "CBCS",
    "CGC",
    "JSA",
    "other",
    "PSA/DNA",
    "unwitnessed",
    "witnessed_in_person",
}


def check_add_issue_to_collection_body_signature_witness(value: str) -> AddIssueToCollectionBodySignatureWitness:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_SIGNATURE_WITNESS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_SIGNATURE_WITNESS_VALUES!r}"
    )
