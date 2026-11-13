from typing import Literal

GetActivityFeedResponse200DataItemAction = Literal[
    "added_to_collection", "marked_as_read", "started_following", "wrote_review"
]

GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_ACTION_VALUES: set[GetActivityFeedResponse200DataItemAction] = {
    "added_to_collection",
    "marked_as_read",
    "started_following",
    "wrote_review",
}


def check_get_activity_feed_response_200_data_item_action(value: str) -> GetActivityFeedResponse200DataItemAction:
    if value in GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_ACTION_VALUES!r}"
    )
