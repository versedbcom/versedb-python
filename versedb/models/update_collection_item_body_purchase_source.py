from typing import Literal

UpdateCollectionItemBodyPurchaseSource = Literal[
    "auction",
    "comic_shop",
    "convention",
    "digital_platform",
    "gift",
    "inheritance",
    "online_retailer",
    "other",
    "private_seller",
    "second_hand_store",
    "subscription",
    "trade",
]

UPDATE_COLLECTION_ITEM_BODY_PURCHASE_SOURCE_VALUES: set[UpdateCollectionItemBodyPurchaseSource] = {
    "auction",
    "comic_shop",
    "convention",
    "digital_platform",
    "gift",
    "inheritance",
    "online_retailer",
    "other",
    "private_seller",
    "second_hand_store",
    "subscription",
    "trade",
}


def check_update_collection_item_body_purchase_source(value: str) -> UpdateCollectionItemBodyPurchaseSource:
    if value in UPDATE_COLLECTION_ITEM_BODY_PURCHASE_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_PURCHASE_SOURCE_VALUES!r}"
    )
