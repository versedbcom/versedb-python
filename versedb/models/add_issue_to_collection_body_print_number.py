from typing import Literal

AddIssueToCollectionBodyPrintNumber = Literal[
    "10th", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "other"
]

ADD_ISSUE_TO_COLLECTION_BODY_PRINT_NUMBER_VALUES: set[AddIssueToCollectionBodyPrintNumber] = {
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


def check_add_issue_to_collection_body_print_number(value: str) -> AddIssueToCollectionBodyPrintNumber:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_PRINT_NUMBER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_PRINT_NUMBER_VALUES!r}")
