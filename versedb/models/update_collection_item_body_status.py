from typing import Literal

UpdateCollectionItemBodyStatus = Literal["for_sale", "owned", "sold"]

UPDATE_COLLECTION_ITEM_BODY_STATUS_VALUES: set[UpdateCollectionItemBodyStatus] = {
    "for_sale",
    "owned",
    "sold",
}


def check_update_collection_item_body_status(value: str) -> UpdateCollectionItemBodyStatus:
    if value in UPDATE_COLLECTION_ITEM_BODY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_STATUS_VALUES!r}")
