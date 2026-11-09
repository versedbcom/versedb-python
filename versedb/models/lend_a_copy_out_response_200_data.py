from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lend_a_copy_out_response_200_data_collectable_type_0 import (
        LendACopyOutResponse200DataCollectableType0,
    )
    from ..models.lend_a_copy_out_response_200_data_comic_shop import LendACopyOutResponse200DataComicShop
    from ..models.lend_a_copy_out_response_200_data_loan_type_0 import LendACopyOutResponse200DataLoanType0


T = TypeVar("T", bound="LendACopyOutResponse200Data")


@_attrs_define
class LendACopyOutResponse200Data:
    """
    Attributes:
        id (int):
        user_id (int):
        collectable_type (str):
        collectable_id (int):
        variant_id (int | None | str): As sent: a number, or digits as text.
        condition (None | str):
        format_ (None | str):
        is_variant (bool | None):
        variant_description (None | str):
        variant_type (None | str):
        graded (bool | None):
        grade_score (None | str):
        grading_company (None | str):
        grading_number (None | str):
        label_type (None | str):
        page_quality (None | str):
        comic_shop_id (int | None | str): As sent: a number, or digits as text.
        personal_rating (float | None | str): As sent on a write: a number, or text.
        is_signed (bool | None):
        signed_by (None | str):
        signature_witness (None | str):
        signature_authenticated (bool):
        is_cgc_ss (bool):
        print_number (None | str):
        status (None | str): `owned`, `for_sale` or `sold`.
        for_sale (bool | None):
        for_trade (bool | None):
        is_public (bool | None):
        cover_scan_url (None | str):
        cover_scan_url_lg (None | str):
        cover_scan_uploaded_at (None | str):
        created_at (None | str):
        updated_at (None | str):
        collectable (LendACopyOutResponse200DataCollectableType0 | None): The issue.
        purchased_at (None | str | Unset): Left out for a `read:showcase` token.
        notes (None | str | Unset): Left out for a `read:showcase` token.
        storage_location (None | str | Unset): Left out for a `read:showcase` token.
        price_paid (None | str | Unset): Left out for a `read:showcase` token.
        grader_notes (None | str | Unset): Left out for a `read:showcase` token.
        purchase_source (None | str | Unset): Left out for a `read:showcase` token.
        comic_shop (LendACopyOutResponse200DataComicShop | Unset): The shop the copy came from, while it is listed; left
            out otherwise and for a `read:showcase` token.
        acquisition_method (None | str | Unset): Left out for a `read:showcase` token.
        purchase_store (None | str | Unset): Left out for a `read:showcase` token.
        custom_label (None | str | Unset): Left out for a `read:showcase` token.
        bagged_at (None | str | Unset): Left out for a `read:showcase` token.
        tags (list[str] | Unset): Left out for a `read:showcase` token.
        loan (LendACopyOutResponse200DataLoanType0 | None | Unset): Left out for a `read:showcase` token.
        estimated_value (None | str | Unset): Left out for a `read:showcase` token.
        value_last_updated (None | str | Unset): Left out for a `read:showcase` token.
        sold_at (None | str | Unset): Left out for a `read:showcase` token.
        price_sold (None | str | Unset): Left out for a `read:showcase` token.
    """

    id: int
    user_id: int
    collectable_type: str
    collectable_id: int
    variant_id: int | None | str
    condition: None | str
    format_: None | str
    is_variant: bool | None
    variant_description: None | str
    variant_type: None | str
    graded: bool | None
    grade_score: None | str
    grading_company: None | str
    grading_number: None | str
    label_type: None | str
    page_quality: None | str
    comic_shop_id: int | None | str
    personal_rating: float | None | str
    is_signed: bool | None
    signed_by: None | str
    signature_witness: None | str
    signature_authenticated: bool
    is_cgc_ss: bool
    print_number: None | str
    status: None | str
    for_sale: bool | None
    for_trade: bool | None
    is_public: bool | None
    cover_scan_url: None | str
    cover_scan_url_lg: None | str
    cover_scan_uploaded_at: None | str
    created_at: None | str
    updated_at: None | str
    collectable: LendACopyOutResponse200DataCollectableType0 | None
    purchased_at: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    storage_location: None | str | Unset = UNSET
    price_paid: None | str | Unset = UNSET
    grader_notes: None | str | Unset = UNSET
    purchase_source: None | str | Unset = UNSET
    comic_shop: LendACopyOutResponse200DataComicShop | Unset = UNSET
    acquisition_method: None | str | Unset = UNSET
    purchase_store: None | str | Unset = UNSET
    custom_label: None | str | Unset = UNSET
    bagged_at: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    loan: LendACopyOutResponse200DataLoanType0 | None | Unset = UNSET
    estimated_value: None | str | Unset = UNSET
    value_last_updated: None | str | Unset = UNSET
    sold_at: None | str | Unset = UNSET
    price_sold: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lend_a_copy_out_response_200_data_collectable_type_0 import (
            LendACopyOutResponse200DataCollectableType0,  # noqa: PLC0415
        )
        from ..models.lend_a_copy_out_response_200_data_loan_type_0 import LendACopyOutResponse200DataLoanType0  # noqa: PLC0415

        id = self.id

        user_id = self.user_id

        collectable_type = self.collectable_type

        collectable_id = self.collectable_id

        variant_id: int | None | str
        variant_id = self.variant_id

        condition: None | str
        condition = self.condition

        format_: None | str
        format_ = self.format_

        is_variant: bool | None
        is_variant = self.is_variant

        variant_description: None | str
        variant_description = self.variant_description

        variant_type: None | str
        variant_type = self.variant_type

        graded: bool | None
        graded = self.graded

        grade_score: None | str
        grade_score = self.grade_score

        grading_company: None | str
        grading_company = self.grading_company

        grading_number: None | str
        grading_number = self.grading_number

        label_type: None | str
        label_type = self.label_type

        page_quality: None | str
        page_quality = self.page_quality

        comic_shop_id: int | None | str
        comic_shop_id = self.comic_shop_id

        personal_rating: float | None | str
        personal_rating = self.personal_rating

        is_signed: bool | None
        is_signed = self.is_signed

        signed_by: None | str
        signed_by = self.signed_by

        signature_witness: None | str
        signature_witness = self.signature_witness

        signature_authenticated = self.signature_authenticated

        is_cgc_ss = self.is_cgc_ss

        print_number: None | str
        print_number = self.print_number

        status: None | str
        status = self.status

        for_sale: bool | None
        for_sale = self.for_sale

        for_trade: bool | None
        for_trade = self.for_trade

        is_public: bool | None
        is_public = self.is_public

        cover_scan_url: None | str
        cover_scan_url = self.cover_scan_url

        cover_scan_url_lg: None | str
        cover_scan_url_lg = self.cover_scan_url_lg

        cover_scan_uploaded_at: None | str
        cover_scan_uploaded_at = self.cover_scan_uploaded_at

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        collectable: dict[str, Any] | None
        if isinstance(self.collectable, LendACopyOutResponse200DataCollectableType0):
            collectable = self.collectable.to_dict()
        else:
            collectable = self.collectable

        purchased_at: None | str | Unset
        if isinstance(self.purchased_at, Unset):
            purchased_at = UNSET
        else:
            purchased_at = self.purchased_at

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        storage_location: None | str | Unset
        if isinstance(self.storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = self.storage_location

        price_paid: None | str | Unset
        if isinstance(self.price_paid, Unset):
            price_paid = UNSET
        else:
            price_paid = self.price_paid

        grader_notes: None | str | Unset
        if isinstance(self.grader_notes, Unset):
            grader_notes = UNSET
        else:
            grader_notes = self.grader_notes

        purchase_source: None | str | Unset
        if isinstance(self.purchase_source, Unset):
            purchase_source = UNSET
        else:
            purchase_source = self.purchase_source

        comic_shop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comic_shop, Unset):
            comic_shop = self.comic_shop.to_dict()

        acquisition_method: None | str | Unset
        if isinstance(self.acquisition_method, Unset):
            acquisition_method = UNSET
        else:
            acquisition_method = self.acquisition_method

        purchase_store: None | str | Unset
        if isinstance(self.purchase_store, Unset):
            purchase_store = UNSET
        else:
            purchase_store = self.purchase_store

        custom_label: None | str | Unset
        if isinstance(self.custom_label, Unset):
            custom_label = UNSET
        else:
            custom_label = self.custom_label

        bagged_at: None | str | Unset
        if isinstance(self.bagged_at, Unset):
            bagged_at = UNSET
        else:
            bagged_at = self.bagged_at

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        loan: dict[str, Any] | None | Unset
        if isinstance(self.loan, Unset):
            loan = UNSET
        elif isinstance(self.loan, LendACopyOutResponse200DataLoanType0):
            loan = self.loan.to_dict()
        else:
            loan = self.loan

        estimated_value: None | str | Unset
        if isinstance(self.estimated_value, Unset):
            estimated_value = UNSET
        else:
            estimated_value = self.estimated_value

        value_last_updated: None | str | Unset
        if isinstance(self.value_last_updated, Unset):
            value_last_updated = UNSET
        else:
            value_last_updated = self.value_last_updated

        sold_at: None | str | Unset
        if isinstance(self.sold_at, Unset):
            sold_at = UNSET
        else:
            sold_at = self.sold_at

        price_sold: None | str | Unset
        if isinstance(self.price_sold, Unset):
            price_sold = UNSET
        else:
            price_sold = self.price_sold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "collectable_type": collectable_type,
                "collectable_id": collectable_id,
                "variant_id": variant_id,
                "condition": condition,
                "format": format_,
                "is_variant": is_variant,
                "variant_description": variant_description,
                "variant_type": variant_type,
                "graded": graded,
                "grade_score": grade_score,
                "grading_company": grading_company,
                "grading_number": grading_number,
                "label_type": label_type,
                "page_quality": page_quality,
                "comic_shop_id": comic_shop_id,
                "personal_rating": personal_rating,
                "is_signed": is_signed,
                "signed_by": signed_by,
                "signature_witness": signature_witness,
                "signature_authenticated": signature_authenticated,
                "is_cgc_ss": is_cgc_ss,
                "print_number": print_number,
                "status": status,
                "for_sale": for_sale,
                "for_trade": for_trade,
                "is_public": is_public,
                "cover_scan_url": cover_scan_url,
                "cover_scan_url_lg": cover_scan_url_lg,
                "cover_scan_uploaded_at": cover_scan_uploaded_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "collectable": collectable,
            }
        )
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if storage_location is not UNSET:
            field_dict["storage_location"] = storage_location
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
        if grader_notes is not UNSET:
            field_dict["grader_notes"] = grader_notes
        if purchase_source is not UNSET:
            field_dict["purchase_source"] = purchase_source
        if comic_shop is not UNSET:
            field_dict["comic_shop"] = comic_shop
        if acquisition_method is not UNSET:
            field_dict["acquisition_method"] = acquisition_method
        if purchase_store is not UNSET:
            field_dict["purchase_store"] = purchase_store
        if custom_label is not UNSET:
            field_dict["custom_label"] = custom_label
        if bagged_at is not UNSET:
            field_dict["bagged_at"] = bagged_at
        if tags is not UNSET:
            field_dict["tags"] = tags
        if loan is not UNSET:
            field_dict["loan"] = loan
        if estimated_value is not UNSET:
            field_dict["estimated_value"] = estimated_value
        if value_last_updated is not UNSET:
            field_dict["value_last_updated"] = value_last_updated
        if sold_at is not UNSET:
            field_dict["sold_at"] = sold_at
        if price_sold is not UNSET:
            field_dict["price_sold"] = price_sold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lend_a_copy_out_response_200_data_collectable_type_0 import (
            LendACopyOutResponse200DataCollectableType0,  # noqa: PLC0415
        )
        from ..models.lend_a_copy_out_response_200_data_comic_shop import LendACopyOutResponse200DataComicShop  # noqa: PLC0415
        from ..models.lend_a_copy_out_response_200_data_loan_type_0 import LendACopyOutResponse200DataLoanType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        collectable_type = d.pop("collectable_type")

        collectable_id = d.pop("collectable_id")

        def _parse_variant_id(data: object) -> int | None | str:
            if data is None:
                return data
            return cast(int | None | str, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        def _parse_condition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        condition = _parse_condition(d.pop("condition"))

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

        def _parse_is_variant(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_variant = _parse_is_variant(d.pop("is_variant"))

        def _parse_variant_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_description = _parse_variant_description(d.pop("variant_description"))

        def _parse_variant_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_type = _parse_variant_type(d.pop("variant_type"))

        def _parse_graded(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        graded = _parse_graded(d.pop("graded"))

        def _parse_grade_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grade_score = _parse_grade_score(d.pop("grade_score"))

        def _parse_grading_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grading_company = _parse_grading_company(d.pop("grading_company"))

        def _parse_grading_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grading_number = _parse_grading_number(d.pop("grading_number"))

        def _parse_label_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label_type = _parse_label_type(d.pop("label_type"))

        def _parse_page_quality(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        page_quality = _parse_page_quality(d.pop("page_quality"))

        def _parse_comic_shop_id(data: object) -> int | None | str:
            if data is None:
                return data
            return cast(int | None | str, data)

        comic_shop_id = _parse_comic_shop_id(d.pop("comic_shop_id"))

        def _parse_personal_rating(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        personal_rating = _parse_personal_rating(d.pop("personal_rating"))

        def _parse_is_signed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_signed = _parse_is_signed(d.pop("is_signed"))

        def _parse_signed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signed_by = _parse_signed_by(d.pop("signed_by"))

        def _parse_signature_witness(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature_witness = _parse_signature_witness(d.pop("signature_witness"))

        signature_authenticated = d.pop("signature_authenticated")

        is_cgc_ss = d.pop("is_cgc_ss")

        def _parse_print_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        print_number = _parse_print_number(d.pop("print_number"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_for_sale(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        for_sale = _parse_for_sale(d.pop("for_sale"))

        def _parse_for_trade(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        for_trade = _parse_for_trade(d.pop("for_trade"))

        def _parse_is_public(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_public = _parse_is_public(d.pop("is_public"))

        def _parse_cover_scan_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_scan_url = _parse_cover_scan_url(d.pop("cover_scan_url"))

        def _parse_cover_scan_url_lg(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_scan_url_lg = _parse_cover_scan_url_lg(d.pop("cover_scan_url_lg"))

        def _parse_cover_scan_uploaded_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_scan_uploaded_at = _parse_cover_scan_uploaded_at(d.pop("cover_scan_uploaded_at"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_collectable(data: object) -> LendACopyOutResponse200DataCollectableType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                collectable_type_0 = LendACopyOutResponse200DataCollectableType0.from_dict(data)

                return collectable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LendACopyOutResponse200DataCollectableType0 | None, data)

        collectable = _parse_collectable(d.pop("collectable"))

        def _parse_purchased_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purchased_at = _parse_purchased_at(d.pop("purchased_at", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_storage_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_location = _parse_storage_location(d.pop("storage_location", UNSET))

        def _parse_price_paid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_paid = _parse_price_paid(d.pop("price_paid", UNSET))

        def _parse_grader_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grader_notes = _parse_grader_notes(d.pop("grader_notes", UNSET))

        def _parse_purchase_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purchase_source = _parse_purchase_source(d.pop("purchase_source", UNSET))

        _comic_shop = d.pop("comic_shop", UNSET)
        comic_shop: LendACopyOutResponse200DataComicShop | Unset
        if isinstance(_comic_shop, Unset):
            comic_shop = UNSET
        else:
            comic_shop = LendACopyOutResponse200DataComicShop.from_dict(_comic_shop)

        def _parse_acquisition_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquisition_method = _parse_acquisition_method(d.pop("acquisition_method", UNSET))

        def _parse_purchase_store(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purchase_store = _parse_purchase_store(d.pop("purchase_store", UNSET))

        def _parse_custom_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_label = _parse_custom_label(d.pop("custom_label", UNSET))

        def _parse_bagged_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bagged_at = _parse_bagged_at(d.pop("bagged_at", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_loan(data: object) -> LendACopyOutResponse200DataLoanType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loan_type_0 = LendACopyOutResponse200DataLoanType0.from_dict(data)

                return loan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LendACopyOutResponse200DataLoanType0 | None | Unset, data)

        loan = _parse_loan(d.pop("loan", UNSET))

        def _parse_estimated_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_value = _parse_estimated_value(d.pop("estimated_value", UNSET))

        def _parse_value_last_updated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_last_updated = _parse_value_last_updated(d.pop("value_last_updated", UNSET))

        def _parse_sold_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sold_at = _parse_sold_at(d.pop("sold_at", UNSET))

        def _parse_price_sold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_sold = _parse_price_sold(d.pop("price_sold", UNSET))

        lend_a_copy_out_response_200_data = cls(
            id=id,
            user_id=user_id,
            collectable_type=collectable_type,
            collectable_id=collectable_id,
            variant_id=variant_id,
            condition=condition,
            format_=format_,
            is_variant=is_variant,
            variant_description=variant_description,
            variant_type=variant_type,
            graded=graded,
            grade_score=grade_score,
            grading_company=grading_company,
            grading_number=grading_number,
            label_type=label_type,
            page_quality=page_quality,
            comic_shop_id=comic_shop_id,
            personal_rating=personal_rating,
            is_signed=is_signed,
            signed_by=signed_by,
            signature_witness=signature_witness,
            signature_authenticated=signature_authenticated,
            is_cgc_ss=is_cgc_ss,
            print_number=print_number,
            status=status,
            for_sale=for_sale,
            for_trade=for_trade,
            is_public=is_public,
            cover_scan_url=cover_scan_url,
            cover_scan_url_lg=cover_scan_url_lg,
            cover_scan_uploaded_at=cover_scan_uploaded_at,
            created_at=created_at,
            updated_at=updated_at,
            collectable=collectable,
            purchased_at=purchased_at,
            notes=notes,
            storage_location=storage_location,
            price_paid=price_paid,
            grader_notes=grader_notes,
            purchase_source=purchase_source,
            comic_shop=comic_shop,
            acquisition_method=acquisition_method,
            purchase_store=purchase_store,
            custom_label=custom_label,
            bagged_at=bagged_at,
            tags=tags,
            loan=loan,
            estimated_value=estimated_value,
            value_last_updated=value_last_updated,
            sold_at=sold_at,
            price_sold=price_sold,
        )

        lend_a_copy_out_response_200_data.additional_properties = d
        return lend_a_copy_out_response_200_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
