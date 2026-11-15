from typing import Literal

MarkTheCopysOpenLoanReturnedResponse200DataCoverKind = Literal["catalog", "custom", "main"]

MARK_THE_COPYS_OPEN_LOAN_RETURNED_RESPONSE_200_DATA_COVER_KIND_VALUES: set[
    MarkTheCopysOpenLoanReturnedResponse200DataCoverKind
] = {
    "catalog",
    "custom",
    "main",
}


def check_mark_the_copys_open_loan_returned_response_200_data_cover_kind(
    value: str,
) -> MarkTheCopysOpenLoanReturnedResponse200DataCoverKind:
    if value in MARK_THE_COPYS_OPEN_LOAN_RETURNED_RESPONSE_200_DATA_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARK_THE_COPYS_OPEN_LOAN_RETURNED_RESPONSE_200_DATA_COVER_KIND_VALUES!r}"
    )
