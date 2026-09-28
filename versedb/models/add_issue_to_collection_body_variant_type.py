from typing import Literal

AddIssueToCollectionBodyVariantType = Literal[
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

ADD_ISSUE_TO_COLLECTION_BODY_VARIANT_TYPE_VALUES: set[AddIssueToCollectionBodyVariantType] = {
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


def check_add_issue_to_collection_body_variant_type(value: str) -> AddIssueToCollectionBodyVariantType:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_VARIANT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_VARIANT_TYPE_VALUES!r}")
