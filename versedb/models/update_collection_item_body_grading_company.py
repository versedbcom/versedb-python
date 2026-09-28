from typing import Literal

UpdateCollectionItemBodyGradingCompany = Literal["CBCS", "CGC", "other", "PGX", "self_graded"]

UPDATE_COLLECTION_ITEM_BODY_GRADING_COMPANY_VALUES: set[UpdateCollectionItemBodyGradingCompany] = {
    "CBCS",
    "CGC",
    "other",
    "PGX",
    "self_graded",
}


def check_update_collection_item_body_grading_company(value: str) -> UpdateCollectionItemBodyGradingCompany:
    if value in UPDATE_COLLECTION_ITEM_BODY_GRADING_COMPANY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_GRADING_COMPANY_VALUES!r}"
    )
