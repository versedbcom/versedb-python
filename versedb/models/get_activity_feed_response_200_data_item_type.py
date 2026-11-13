from typing import Literal

GetActivityFeedResponse200DataItemType = Literal["collection", "follow", "read", "review"]

GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_TYPE_VALUES: set[GetActivityFeedResponse200DataItemType] = {
    "collection",
    "follow",
    "read",
    "review",
}


def check_get_activity_feed_response_200_data_item_type(value: str) -> GetActivityFeedResponse200DataItemType:
    if value in GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ACTIVITY_FEED_RESPONSE_200_DATA_ITEM_TYPE_VALUES!r}"
    )
