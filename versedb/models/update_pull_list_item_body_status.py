from typing import Literal

UpdatePullListItemBodyStatus = Literal["active", "canceled", "paused"]

UPDATE_PULL_LIST_ITEM_BODY_STATUS_VALUES: set[UpdatePullListItemBodyStatus] = {
    "active",
    "canceled",
    "paused",
}


def check_update_pull_list_item_body_status(value: str) -> UpdatePullListItemBodyStatus:
    if value in UPDATE_PULL_LIST_ITEM_BODY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PULL_LIST_ITEM_BODY_STATUS_VALUES!r}")
