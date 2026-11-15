from typing import Literal

ListCollectionResponse200DataItemCoverKind = Literal["catalog", "custom", "main"]

LIST_COLLECTION_RESPONSE_200_DATA_ITEM_COVER_KIND_VALUES: set[ListCollectionResponse200DataItemCoverKind] = {
    "catalog",
    "custom",
    "main",
}


def check_list_collection_response_200_data_item_cover_kind(value: str) -> ListCollectionResponse200DataItemCoverKind:
    if value in LIST_COLLECTION_RESPONSE_200_DATA_ITEM_COVER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_COLLECTION_RESPONSE_200_DATA_ITEM_COVER_KIND_VALUES!r}"
    )
