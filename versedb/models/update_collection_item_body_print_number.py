from typing import Literal

UpdateCollectionItemBodyPrintNumber = Literal[
    "10th", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "other"
]

UPDATE_COLLECTION_ITEM_BODY_PRINT_NUMBER_VALUES: set[UpdateCollectionItemBodyPrintNumber] = {
    "10th",
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "6th",
    "7th",
    "8th",
    "9th",
    "other",
}


def check_update_collection_item_body_print_number(value: str) -> UpdateCollectionItemBodyPrintNumber:
    if value in UPDATE_COLLECTION_ITEM_BODY_PRINT_NUMBER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_PRINT_NUMBER_VALUES!r}")
