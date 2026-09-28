from typing import Literal

UpdateCollectionItemBodyAcquisitionMethod = Literal[
    "found", "gift", "inheritance", "other", "purchase", "subscription", "trade"
]

UPDATE_COLLECTION_ITEM_BODY_ACQUISITION_METHOD_VALUES: set[UpdateCollectionItemBodyAcquisitionMethod] = {
    "found",
    "gift",
    "inheritance",
    "other",
    "purchase",
    "subscription",
    "trade",
}


def check_update_collection_item_body_acquisition_method(value: str) -> UpdateCollectionItemBodyAcquisitionMethod:
    if value in UPDATE_COLLECTION_ITEM_BODY_ACQUISITION_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_ACQUISITION_METHOD_VALUES!r}"
    )
