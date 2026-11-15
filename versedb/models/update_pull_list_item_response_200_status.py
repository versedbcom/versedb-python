from typing import Literal

UpdatePullListItemResponse200Status = Literal["active", "canceled", "paused"]

UPDATE_PULL_LIST_ITEM_RESPONSE_200_STATUS_VALUES: set[UpdatePullListItemResponse200Status] = {
    "active",
    "canceled",
    "paused",
}


def check_update_pull_list_item_response_200_status(value: str) -> UpdatePullListItemResponse200Status:
    if value in UPDATE_PULL_LIST_ITEM_RESPONSE_200_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PULL_LIST_ITEM_RESPONSE_200_STATUS_VALUES!r}")
