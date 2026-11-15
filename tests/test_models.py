"""Model tests: variant and collection copy fields parse from API payloads and serialize back."""

import attrs
import pytest

from versedb.models import (
    CheckIssueInCollectionResponse200CopiesItem,
    GetAnEventResponse200DataIssueVariantsItem,
    GetIssueVariantsResponse200DataItem,
    GetIssueVariantsResponse200DataItemShopsItem,
    GetVariantDetailsResponse200Data,
    ListCollectionResponse200DataItem,
    ListCollectionResponse200DataItemVariantType0,
)
from versedb.models.list_collection_response_200_data_item_cover_kind import (
    check_list_collection_response_200_data_item_cover_kind,
)
from versedb.types import UNSET

COPY = {
    "id": 1001,
    "variant_id": 789,
    "cover_kind": "catalog",
    "variant_label": "Cover B",
    "condition": "NM",
    "graded": False,
    "grade_score": None,
    "grading_company": None,
    "is_signed": False,
    "signed_by": None,
    "is_cgc_ss": False,
    "format": "single",
    "storage_location": None,
    "purchased_at": None,
    "notes": None,
    "created_at": "2024-01-15T10:30:00.000000Z",
    "updated_at": "2024-01-15T10:30:00.000000Z",
}

COPY_VARIANT = {
    "id": 789,
    "name": "Cover B",
    "type": "cover_variant",
    "cover_url": "https://example.com/cover_md.webp",
    "cover_url_lg": "https://example.com/cover_lg.webp",
    "ratio": "1:25",
    "printing": 1,
    "is_nsfw": False,
}


def field_names(model: type) -> set[str]:
    return {field.name for field in attrs.fields(model)}


@pytest.mark.parametrize("model", [GetIssueVariantsResponse200DataItem, GetVariantDetailsResponse200Data])
def test_variant_models_carry_print_run_cover_letter_and_shops(model):
    assert {"print_run", "cover_letter", "shops"} <= field_names(model)
    assert attrs.fields(model).shops.default is UNSET


def test_event_variants_carry_print_run_and_cover_letter_without_shops():
    names = field_names(GetAnEventResponse200DataIssueVariantsItem)
    assert {"print_run", "cover_letter"} <= names
    assert "shops" not in names


def test_variant_shop_round_trips():
    payload = {"id": 12, "name": "Third Eye Comics", "slug": "third-eye-comics"}
    shop = GetIssueVariantsResponse200DataItemShopsItem.from_dict(payload)
    assert (shop.id, shop.name, shop.slug) == (12, "Third Eye Comics", "third-eye-comics")
    assert shop.to_dict() == payload


def test_collection_copy_carries_variant_and_cover_kind():
    assert {"variant", "cover_kind"} <= field_names(ListCollectionResponse200DataItem)


def test_collection_copy_variant_round_trips():
    variant = ListCollectionResponse200DataItemVariantType0.from_dict(COPY_VARIANT)
    assert variant.type_ == "cover_variant"
    assert variant.cover_url_lg == "https://example.com/cover_lg.webp"
    assert variant.printing == 1
    assert variant.to_dict() == COPY_VARIANT


@pytest.mark.parametrize("kind", ["main", "catalog", "custom"])
def test_cover_kind_accepts_each_value(kind):
    assert check_list_collection_response_200_data_item_cover_kind(kind) == kind


def test_cover_kind_rejects_an_unknown_value():
    with pytest.raises(TypeError):
        check_list_collection_response_200_data_item_cover_kind("other")


def test_collection_check_copy_round_trips():
    copy = CheckIssueInCollectionResponse200CopiesItem.from_dict(COPY)
    assert copy.cover_kind == "catalog"
    assert copy.variant_label == "Cover B"
    assert copy.to_dict() == COPY


def test_collection_check_copy_of_the_main_cover_has_no_label():
    copy = CheckIssueInCollectionResponse200CopiesItem.from_dict(
        {**COPY, "variant_id": None, "cover_kind": "main", "variant_label": None}
    )
    assert copy.cover_kind == "main"
    assert copy.variant_label is None
