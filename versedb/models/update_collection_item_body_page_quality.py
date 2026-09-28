from typing import Literal

UpdateCollectionItemBodyPageQuality = Literal[
    "brittle", "cream_to_off_white", "light_tan", "off_white", "off_white_to_white", "tan", "white"
]

UPDATE_COLLECTION_ITEM_BODY_PAGE_QUALITY_VALUES: set[UpdateCollectionItemBodyPageQuality] = {
    "brittle",
    "cream_to_off_white",
    "light_tan",
    "off_white",
    "off_white_to_white",
    "tan",
    "white",
}


def check_update_collection_item_body_page_quality(value: str) -> UpdateCollectionItemBodyPageQuality:
    if value in UPDATE_COLLECTION_ITEM_BODY_PAGE_QUALITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_PAGE_QUALITY_VALUES!r}")
