from typing import Literal

AddIssueToCollectionBodyGradingCompany = Literal["CBCS", "CGC", "other", "PGX", "self_graded"]

ADD_ISSUE_TO_COLLECTION_BODY_GRADING_COMPANY_VALUES: set[AddIssueToCollectionBodyGradingCompany] = {
    "CBCS",
    "CGC",
    "other",
    "PGX",
    "self_graded",
}


def check_add_issue_to_collection_body_grading_company(value: str) -> AddIssueToCollectionBodyGradingCompany:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_GRADING_COMPANY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_GRADING_COMPANY_VALUES!r}"
    )
