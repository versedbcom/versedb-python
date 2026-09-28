from typing import Literal

UpdateCollectionItemBodyLabelType = Literal[
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

UPDATE_COLLECTION_ITEM_BODY_LABEL_TYPE_VALUES: set[UpdateCollectionItemBodyLabelType] = {
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


def check_update_collection_item_body_label_type(value: str) -> UpdateCollectionItemBodyLabelType:
    if value in UPDATE_COLLECTION_ITEM_BODY_LABEL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_LABEL_TYPE_VALUES!r}")
