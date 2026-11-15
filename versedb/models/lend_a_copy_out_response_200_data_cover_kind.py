from typing import Literal

LendACopyOutResponse200DataCoverKind = Literal["catalog", "custom", "main"]

LEND_A_COPY_OUT_RESPONSE_200_DATA_COVER_KIND_VALUES: set[LendACopyOutResponse200DataCoverKind] = {
    "catalog",
    "custom",
    "main",
}


def check_lend_a_copy_out_response_200_data_cover_kind(value: str) -> LendACopyOutResponse200DataCoverKind:
    if value in LEND_A_COPY_OUT_RESPONSE_200_DATA_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LEND_A_COPY_OUT_RESPONSE_200_DATA_COVER_KIND_VALUES!r}"
    )
