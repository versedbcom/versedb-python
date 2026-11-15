from typing import Literal

UpdatePullListItemResponse200PreferredCoverTypeType2Type1 = Literal["regular", "standard_and_regular"]

UPDATE_PULL_LIST_ITEM_RESPONSE_200_PREFERRED_COVER_TYPE_TYPE_2_TYPE_1_VALUES: set[
    UpdatePullListItemResponse200PreferredCoverTypeType2Type1
] = {
    "regular",
    "standard_and_regular",
}


def check_update_pull_list_item_response_200_preferred_cover_type_type_2_type_1(
    value: str,
) -> UpdatePullListItemResponse200PreferredCoverTypeType2Type1:
    if value in UPDATE_PULL_LIST_ITEM_RESPONSE_200_PREFERRED_COVER_TYPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PULL_LIST_ITEM_RESPONSE_200_PREFERRED_COVER_TYPE_TYPE_2_TYPE_1_VALUES!r}"
    )
