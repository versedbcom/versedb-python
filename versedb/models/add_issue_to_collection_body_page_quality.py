from typing import Literal

AddIssueToCollectionBodyPageQuality = Literal[
    "brittle", "cream_to_off_white", "light_tan", "off_white", "off_white_to_white", "tan", "white"
]

ADD_ISSUE_TO_COLLECTION_BODY_PAGE_QUALITY_VALUES: set[AddIssueToCollectionBodyPageQuality] = {
    "brittle",
    "cream_to_off_white",
    "light_tan",
    "off_white",
    "off_white_to_white",
    "tan",
    "white",
}


def check_add_issue_to_collection_body_page_quality(value: str) -> AddIssueToCollectionBodyPageQuality:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_PAGE_QUALITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_PAGE_QUALITY_VALUES!r}")
