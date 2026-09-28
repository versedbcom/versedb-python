from typing import Literal

UpdateCollectionItemBodySignatureWitness = Literal[
    "CBCS", "CGC", "JSA", "other", "PSA/DNA", "unwitnessed", "witnessed_in_person"
]

UPDATE_COLLECTION_ITEM_BODY_SIGNATURE_WITNESS_VALUES: set[UpdateCollectionItemBodySignatureWitness] = {
    "CBCS",
    "CGC",
    "JSA",
    "other",
    "PSA/DNA",
    "unwitnessed",
    "witnessed_in_person",
}


def check_update_collection_item_body_signature_witness(value: str) -> UpdateCollectionItemBodySignatureWitness:
    if value in UPDATE_COLLECTION_ITEM_BODY_SIGNATURE_WITNESS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_SIGNATURE_WITNESS_VALUES!r}"
    )
