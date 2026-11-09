from typing import Literal

FollowUpdatesResponse200FollowTypesType0AdditionalProperty = Literal["character", "creator", "team", "title"]

FOLLOW_UPDATES_RESPONSE_200_FOLLOW_TYPES_TYPE_0_ADDITIONAL_PROPERTY_VALUES: set[
    FollowUpdatesResponse200FollowTypesType0AdditionalProperty
] = {
    "character",
    "creator",
    "team",
    "title",
}


def check_follow_updates_response_200_follow_types_type_0_additional_property(
    value: str,
) -> FollowUpdatesResponse200FollowTypesType0AdditionalProperty:
    if value in FOLLOW_UPDATES_RESPONSE_200_FOLLOW_TYPES_TYPE_0_ADDITIONAL_PROPERTY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOLLOW_UPDATES_RESPONSE_200_FOLLOW_TYPES_TYPE_0_ADDITIONAL_PROPERTY_VALUES!r}"
    )
