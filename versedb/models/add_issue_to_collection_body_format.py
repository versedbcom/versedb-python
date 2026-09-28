from typing import Literal

AddIssueToCollectionBodyFormat = Literal[
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

ADD_ISSUE_TO_COLLECTION_BODY_FORMAT_VALUES: set[AddIssueToCollectionBodyFormat] = {
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


def check_add_issue_to_collection_body_format(value: str) -> AddIssueToCollectionBodyFormat:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_FORMAT_VALUES!r}")
