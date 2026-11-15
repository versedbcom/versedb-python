from typing import Literal

UpdatePullListItemBodyPreferredCoverTypeType3Type1 = Literal["regular", "standard", "standard_and_regular"]

UPDATE_PULL_LIST_ITEM_BODY_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES: set[
    UpdatePullListItemBodyPreferredCoverTypeType3Type1
] = {
    "regular",
    "standard",
    "standard_and_regular",
}


def check_update_pull_list_item_body_preferred_cover_type_type_3_type_1(
    value: str,
) -> UpdatePullListItemBodyPreferredCoverTypeType3Type1:
    if value in UPDATE_PULL_LIST_ITEM_BODY_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PULL_LIST_ITEM_BODY_PREFERRED_COVER_TYPE_TYPE_3_TYPE_1_VALUES!r}"
    )
