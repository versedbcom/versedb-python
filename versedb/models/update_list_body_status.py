from typing import Literal

UpdateListBodyStatus = Literal["draft", "published"]

UPDATE_LIST_BODY_STATUS_VALUES: set[UpdateListBodyStatus] = {
    "draft",
    "published",
}


def check_update_list_body_status(value: str) -> UpdateListBodyStatus:
    if value in UPDATE_LIST_BODY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_LIST_BODY_STATUS_VALUES!r}")
