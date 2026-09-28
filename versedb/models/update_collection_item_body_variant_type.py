from typing import Literal

UpdateCollectionItemBodyVariantType = Literal[
    "artist_variant",
    "blank_variant",
    "convention_exclusive",
    "cover_variant",
    "facsimile",
    "foil_variant",
    "glow_in_dark_variant",
    "hologram_variant",
    "incentive_variant",
    "other",
    "ratio_variant",
    "reprint",
    "retailer_exclusive",
    "sketch_variant",
    "standard",
    "virgin_variant",
]

UPDATE_COLLECTION_ITEM_BODY_VARIANT_TYPE_VALUES: set[UpdateCollectionItemBodyVariantType] = {
    "artist_variant",
    "blank_variant",
    "convention_exclusive",
    "cover_variant",
    "facsimile",
    "foil_variant",
    "glow_in_dark_variant",
    "hologram_variant",
    "incentive_variant",
    "other",
    "ratio_variant",
    "reprint",
    "retailer_exclusive",
    "sketch_variant",
    "standard",
    "virgin_variant",
}


def check_update_collection_item_body_variant_type(value: str) -> UpdateCollectionItemBodyVariantType:
    if value in UPDATE_COLLECTION_ITEM_BODY_VARIANT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_VARIANT_TYPE_VALUES!r}")
