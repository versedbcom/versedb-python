from typing import Literal

UpdateCollectionItemResponse200DataCoverKind = Literal["catalog", "custom", "main"]

UPDATE_COLLECTION_ITEM_RESPONSE_200_DATA_COVER_KIND_VALUES: set[UpdateCollectionItemResponse200DataCoverKind] = {
    "catalog",
    "custom",
    "main",
}


def check_update_collection_item_response_200_data_cover_kind(
    value: str,
) -> UpdateCollectionItemResponse200DataCoverKind:
    if value in UPDATE_COLLECTION_ITEM_RESPONSE_200_DATA_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_RESPONSE_200_DATA_COVER_KIND_VALUES!r}"
    )
