from typing import Literal

ListPullListResponse200DataItemPreferredCoverTypeType3Type1 = Literal["regular", "standard_and_regular"]

LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES: set[
    ListPullListResponse200DataItemPreferredCoverTypeType3Type1
] = {
    "regular",
    "standard_and_regular",
}


def check_list_pull_list_response_200_data_item_preferred_cover_type_type_3_type_1(
    value: str,
) -> ListPullListResponse200DataItemPreferredCoverTypeType3Type1:
    if value in LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PULL_LIST_RESPONSE_200_DATA_ITEM_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES!r}"
    )
