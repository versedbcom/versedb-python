from typing import Literal

AddIssueToCollectionBodyPurchaseSource = Literal[
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

ADD_ISSUE_TO_COLLECTION_BODY_PURCHASE_SOURCE_VALUES: set[AddIssueToCollectionBodyPurchaseSource] = {
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


def check_add_issue_to_collection_body_purchase_source(value: str) -> AddIssueToCollectionBodyPurchaseSource:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_PURCHASE_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_PURCHASE_SOURCE_VALUES!r}"
    )
