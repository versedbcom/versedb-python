from typing import Literal

UpdateCollectionItemBodyFormat = Literal[
    "annual",
    "deluxe_edition",
    "digest",
    "digital",
    "graphic_novel",
    "hardcover",
    "magazine",
    "omnibus",
    "other",
    "prestige",
    "standard",
    "trade_paperback",
    "treasury",
]

UPDATE_COLLECTION_ITEM_BODY_FORMAT_VALUES: set[UpdateCollectionItemBodyFormat] = {
    "annual",
    "deluxe_edition",
    "digest",
    "digital",
    "graphic_novel",
    "hardcover",
    "magazine",
    "omnibus",
    "other",
    "prestige",
    "standard",
    "trade_paperback",
    "treasury",
}


def check_update_collection_item_body_format(value: str) -> UpdateCollectionItemBodyFormat:
    if value in UPDATE_COLLECTION_ITEM_BODY_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_FORMAT_VALUES!r}")
