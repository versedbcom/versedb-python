from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_collection_item_body_acquisition_method import (
    UpdateCollectionItemBodyAcquisitionMethod,
    check_update_collection_item_body_acquisition_method,
)
from ..models.update_collection_item_body_condition import (
    UpdateCollectionItemBodyCondition,
    check_update_collection_item_body_condition,
)
from ..models.update_collection_item_body_format import (
    UpdateCollectionItemBodyFormat,
    check_update_collection_item_body_format,
)
from ..models.update_collection_item_body_grading_company import (
    UpdateCollectionItemBodyGradingCompany,
    check_update_collection_item_body_grading_company,
)
from ..models.update_collection_item_body_label_type import (
    UpdateCollectionItemBodyLabelType,
    check_update_collection_item_body_label_type,
)
from ..models.update_collection_item_body_page_quality import (
    UpdateCollectionItemBodyPageQuality,
    check_update_collection_item_body_page_quality,
)
from ..models.update_collection_item_body_print_number import (
    UpdateCollectionItemBodyPrintNumber,
    check_update_collection_item_body_print_number,
)
from ..models.update_collection_item_body_purchase_source import (
    UpdateCollectionItemBodyPurchaseSource,
    check_update_collection_item_body_purchase_source,
)
from ..models.update_collection_item_body_signature_witness import (
    UpdateCollectionItemBodySignatureWitness,
    check_update_collection_item_body_signature_witness,
)
from ..models.update_collection_item_body_status import (
    UpdateCollectionItemBodyStatus,
    check_update_collection_item_body_status,
)
from ..models.update_collection_item_body_variant_type import (
    UpdateCollectionItemBodyVariantType,
    check_update_collection_item_body_variant_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCollectionItemBody")


@_attrs_define
class UpdateCollectionItemBody:
    """
    Attributes:
        variant_id (int | None | Unset): Link to a specific issue variant. Must belong to the issue. Must match an
            existing stored value.
        condition (UpdateCollectionItemBodyCondition | Unset): Comic condition grade (CGC scale).
        notes (None | str | Unset): User notes about this copy. Must not be greater than 1000 characters.
        price_paid (float | None | Unset): Purchase price in dollars. Must be at least 0. Must not be greater than
            999999.99.
        format_ (UpdateCollectionItemBodyFormat | Unset): Physical format of the copy.
        purchase_source (UpdateCollectionItemBodyPurchaseSource | Unset): Where the comic was purchased.
        purchase_store (None | str | Unset): Name of the store the copy was bought from, as free text. Use comic_shop_id
            instead where the shop is one VerseDB catalogs. Must not be greater than 255 characters.
        custom_label (None | str | Unset): The collector's own label for this copy. Free-text and unrelated to a slab
            label. Must not be greater than 255 characters.
        bagged_at (None | str | Unset): Date the copy was bagged and boarded (YYYY-MM-DD). Must be a valid date.
        personal_rating (float | None | Unset): The collector's own rating of this copy, in half stars from 0.5 to 5.
            Private to the copy: it is not a review and feeds no community average.
        tags (list[str] | Unset): The collector's own labels for this copy. Private to the account — one user's tags are
            never visible to another. Must not be greater than 100 characters.
        comic_shop_id (int | None | Unset): ID of the specific comic shop the copy was purchased from. Self-reported;
            independent of purchase_source. Must match an existing stored value.
        acquisition_method (UpdateCollectionItemBodyAcquisitionMethod | Unset): How the comic was acquired.
        purchased_at (None | str | Unset): Date of purchase (YYYY-MM-DD). Must be a valid date.
        storage_location (None | str | Unset): Where the comic is stored. Must not be greater than 255 characters.
        is_signed (bool | Unset): Whether the comic is signed.
        signed_by (None | str | Unset): Name(s) of the creator(s) who signed the comic. Free-text. Comma-separate
            multiple signers. Must not be greater than 255 characters.
        is_variant (bool | Unset): Whether this copy is a variant cover.
        variant_description (None | str | Unset): Free-text description of the variant cover. Must not be greater than
            500 characters.
        variant_type (UpdateCollectionItemBodyVariantType | Unset): Variant classification (standard, cover_variant,
            retailer_exclusive, incentive_variant, ratio_variant, virgin_variant, etc.).
        graded (bool | Unset): Whether the comic is professionally graded.
        grade_score (None | str | Unset): Numeric grade score (e.g. 9.8). Must not be greater than 10 characters.
        grading_company (UpdateCollectionItemBodyGradingCompany | Unset): Grading company (CGC, CBCS, PGX, other,
            self_graded).
        grading_number (None | str | Unset): Grading certification number. Must not be greater than 50 characters.
        label_type (UpdateCollectionItemBodyLabelType | Unset): Slab label tier (e.g. universal, signature_series,
            restored, qualified).
        page_quality (UpdateCollectionItemBodyPageQuality | Unset): Interior page color quality from the slab label.
        grader_notes (None | str | Unset): Free-text notes printed on the slab label. Must not be greater than 2000
            characters.
        print_number (UpdateCollectionItemBodyPrintNumber | Unset): Which print this copy is (1st, 2nd, 3rd, … or
            other).
        signature_witness (UpdateCollectionItemBodySignatureWitness | Unset): Authentication of the signature (CGC,
            CBCS, JSA, PSA/DNA, witnessed_in_person, unwitnessed, other).
        estimated_value (float | None | Unset): Current estimated value in dollars. Must be at least 0. Must not be
            greater than 999999.99.
        for_sale (bool | Unset): Whether the item is for sale.
        status (UpdateCollectionItemBodyStatus | Unset): Whether the copy is owned, for_sale, or sold. A sold copy keeps
            its record but leaves the collection totals.
        sold_at (None | str | Unset): Date the copy was sold. Must be a valid date.
        price_sold (float | None | Unset): What the copy sold for, in dollars. Must be at least 0. Must not be greater
            than 99999999.99.
        for_trade (bool | Unset): Whether the item is available for trade.
        is_public (bool | Unset): Whether this collection item is publicly visible.
        is_read (bool | Unset): Whether the issue has been read.
        read_at (None | str | Unset): When the issue was read (YYYY-MM-DD). Cannot be in the future. Must be a valid
            date. Must be a date before or equal to <code>today</code>.
    """

    variant_id: int | None | Unset = UNSET
    condition: UpdateCollectionItemBodyCondition | Unset = UNSET
    notes: None | str | Unset = UNSET
    price_paid: float | None | Unset = UNSET
    format_: UpdateCollectionItemBodyFormat | Unset = UNSET
    purchase_source: UpdateCollectionItemBodyPurchaseSource | Unset = UNSET
    purchase_store: None | str | Unset = UNSET
    custom_label: None | str | Unset = UNSET
    bagged_at: None | str | Unset = UNSET
    personal_rating: float | None | Unset = UNSET
    tags: list[str] | Unset = UNSET
    comic_shop_id: int | None | Unset = UNSET
    acquisition_method: UpdateCollectionItemBodyAcquisitionMethod | Unset = UNSET
    purchased_at: None | str | Unset = UNSET
    storage_location: None | str | Unset = UNSET
    is_signed: bool | Unset = UNSET
    signed_by: None | str | Unset = UNSET
    is_variant: bool | Unset = UNSET
    variant_description: None | str | Unset = UNSET
    variant_type: UpdateCollectionItemBodyVariantType | Unset = UNSET
    graded: bool | Unset = UNSET
    grade_score: None | str | Unset = UNSET
    grading_company: UpdateCollectionItemBodyGradingCompany | Unset = UNSET
    grading_number: None | str | Unset = UNSET
    label_type: UpdateCollectionItemBodyLabelType | Unset = UNSET
    page_quality: UpdateCollectionItemBodyPageQuality | Unset = UNSET
    grader_notes: None | str | Unset = UNSET
    print_number: UpdateCollectionItemBodyPrintNumber | Unset = UNSET
    signature_witness: UpdateCollectionItemBodySignatureWitness | Unset = UNSET
    estimated_value: float | None | Unset = UNSET
    for_sale: bool | Unset = UNSET
    status: UpdateCollectionItemBodyStatus | Unset = UNSET
    sold_at: None | str | Unset = UNSET
    price_sold: float | None | Unset = UNSET
    for_trade: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    is_read: bool | Unset = UNSET
    read_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id: int | None | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        condition: str | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        price_paid: float | None | Unset
        if isinstance(self.price_paid, Unset):
            price_paid = UNSET
        else:
            price_paid = self.price_paid

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        purchase_source: str | Unset = UNSET
        if not isinstance(self.purchase_source, Unset):
            purchase_source = self.purchase_source

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

        personal_rating: float | None | Unset
        if isinstance(self.personal_rating, Unset):
            personal_rating = UNSET
        else:
            personal_rating = self.personal_rating

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        comic_shop_id: int | None | Unset
        if isinstance(self.comic_shop_id, Unset):
            comic_shop_id = UNSET
        else:
            comic_shop_id = self.comic_shop_id

        acquisition_method: str | Unset = UNSET
        if not isinstance(self.acquisition_method, Unset):
            acquisition_method = self.acquisition_method

        purchased_at: None | str | Unset
        if isinstance(self.purchased_at, Unset):
            purchased_at = UNSET
        else:
            purchased_at = self.purchased_at

        storage_location: None | str | Unset
        if isinstance(self.storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = self.storage_location

        is_signed = self.is_signed

        signed_by: None | str | Unset
        if isinstance(self.signed_by, Unset):
            signed_by = UNSET
        else:
            signed_by = self.signed_by

        is_variant = self.is_variant

        variant_description: None | str | Unset
        if isinstance(self.variant_description, Unset):
            variant_description = UNSET
        else:
            variant_description = self.variant_description

        variant_type: str | Unset = UNSET
        if not isinstance(self.variant_type, Unset):
            variant_type = self.variant_type

        graded = self.graded

        grade_score: None | str | Unset
        if isinstance(self.grade_score, Unset):
            grade_score = UNSET
        else:
            grade_score = self.grade_score

        grading_company: str | Unset = UNSET
        if not isinstance(self.grading_company, Unset):
            grading_company = self.grading_company

        grading_number: None | str | Unset
        if isinstance(self.grading_number, Unset):
            grading_number = UNSET
        else:
            grading_number = self.grading_number

        label_type: str | Unset = UNSET
        if not isinstance(self.label_type, Unset):
            label_type = self.label_type

        page_quality: str | Unset = UNSET
        if not isinstance(self.page_quality, Unset):
            page_quality = self.page_quality

        grader_notes: None | str | Unset
        if isinstance(self.grader_notes, Unset):
            grader_notes = UNSET
        else:
            grader_notes = self.grader_notes

        print_number: str | Unset = UNSET
        if not isinstance(self.print_number, Unset):
            print_number = self.print_number

        signature_witness: str | Unset = UNSET
        if not isinstance(self.signature_witness, Unset):
            signature_witness = self.signature_witness

        estimated_value: float | None | Unset
        if isinstance(self.estimated_value, Unset):
            estimated_value = UNSET
        else:
            estimated_value = self.estimated_value

        for_sale = self.for_sale

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        sold_at: None | str | Unset
        if isinstance(self.sold_at, Unset):
            sold_at = UNSET
        else:
            sold_at = self.sold_at

        price_sold: float | None | Unset
        if isinstance(self.price_sold, Unset):
            price_sold = UNSET
        else:
            price_sold = self.price_sold

        for_trade = self.for_trade

        is_public = self.is_public

        is_read = self.is_read

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        else:
            read_at = self.read_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if notes is not UNSET:
            field_dict["notes"] = notes
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
        if format_ is not UNSET:
            field_dict["format"] = format_
        if purchase_source is not UNSET:
            field_dict["purchase_source"] = purchase_source
        if purchase_store is not UNSET:
            field_dict["purchase_store"] = purchase_store
        if custom_label is not UNSET:
            field_dict["custom_label"] = custom_label
        if bagged_at is not UNSET:
            field_dict["bagged_at"] = bagged_at
        if personal_rating is not UNSET:
            field_dict["personal_rating"] = personal_rating
        if tags is not UNSET:
            field_dict["tags"] = tags
        if comic_shop_id is not UNSET:
            field_dict["comic_shop_id"] = comic_shop_id
        if acquisition_method is not UNSET:
            field_dict["acquisition_method"] = acquisition_method
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if storage_location is not UNSET:
            field_dict["storage_location"] = storage_location
        if is_signed is not UNSET:
            field_dict["is_signed"] = is_signed
        if signed_by is not UNSET:
            field_dict["signed_by"] = signed_by
        if is_variant is not UNSET:
            field_dict["is_variant"] = is_variant
        if variant_description is not UNSET:
            field_dict["variant_description"] = variant_description
        if variant_type is not UNSET:
            field_dict["variant_type"] = variant_type
        if graded is not UNSET:
            field_dict["graded"] = graded
        if grade_score is not UNSET:
            field_dict["grade_score"] = grade_score
        if grading_company is not UNSET:
            field_dict["grading_company"] = grading_company
        if grading_number is not UNSET:
            field_dict["grading_number"] = grading_number
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if page_quality is not UNSET:
            field_dict["page_quality"] = page_quality
        if grader_notes is not UNSET:
            field_dict["grader_notes"] = grader_notes
        if print_number is not UNSET:
            field_dict["print_number"] = print_number
        if signature_witness is not UNSET:
            field_dict["signature_witness"] = signature_witness
        if estimated_value is not UNSET:
            field_dict["estimated_value"] = estimated_value
        if for_sale is not UNSET:
            field_dict["for_sale"] = for_sale
        if status is not UNSET:
            field_dict["status"] = status
        if sold_at is not UNSET:
            field_dict["sold_at"] = sold_at
        if price_sold is not UNSET:
            field_dict["price_sold"] = price_sold
        if for_trade is not UNSET:
            field_dict["for_trade"] = for_trade
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_read is not UNSET:
            field_dict["is_read"] = is_read
        if read_at is not UNSET:
            field_dict["read_at"] = read_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_variant_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        _condition = d.pop("condition", UNSET)
        condition: UpdateCollectionItemBodyCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = check_update_collection_item_body_condition(_condition)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_price_paid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_paid = _parse_price_paid(d.pop("price_paid", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: UpdateCollectionItemBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_update_collection_item_body_format(_format_)

        _purchase_source = d.pop("purchase_source", UNSET)
        purchase_source: UpdateCollectionItemBodyPurchaseSource | Unset
        if isinstance(_purchase_source, Unset):
            purchase_source = UNSET
        else:
            purchase_source = check_update_collection_item_body_purchase_source(_purchase_source)

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

        def _parse_personal_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        personal_rating = _parse_personal_rating(d.pop("personal_rating", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_comic_shop_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comic_shop_id = _parse_comic_shop_id(d.pop("comic_shop_id", UNSET))

        _acquisition_method = d.pop("acquisition_method", UNSET)
        acquisition_method: UpdateCollectionItemBodyAcquisitionMethod | Unset
        if isinstance(_acquisition_method, Unset):
            acquisition_method = UNSET
        else:
            acquisition_method = check_update_collection_item_body_acquisition_method(_acquisition_method)

        def _parse_purchased_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purchased_at = _parse_purchased_at(d.pop("purchased_at", UNSET))

        def _parse_storage_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_location = _parse_storage_location(d.pop("storage_location", UNSET))

        is_signed = d.pop("is_signed", UNSET)

        def _parse_signed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signed_by = _parse_signed_by(d.pop("signed_by", UNSET))

        is_variant = d.pop("is_variant", UNSET)

        def _parse_variant_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_description = _parse_variant_description(d.pop("variant_description", UNSET))

        _variant_type = d.pop("variant_type", UNSET)
        variant_type: UpdateCollectionItemBodyVariantType | Unset
        if isinstance(_variant_type, Unset):
            variant_type = UNSET
        else:
            variant_type = check_update_collection_item_body_variant_type(_variant_type)

        graded = d.pop("graded", UNSET)

        def _parse_grade_score(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade_score = _parse_grade_score(d.pop("grade_score", UNSET))

        _grading_company = d.pop("grading_company", UNSET)
        grading_company: UpdateCollectionItemBodyGradingCompany | Unset
        if isinstance(_grading_company, Unset):
            grading_company = UNSET
        else:
            grading_company = check_update_collection_item_body_grading_company(_grading_company)

        def _parse_grading_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grading_number = _parse_grading_number(d.pop("grading_number", UNSET))

        _label_type = d.pop("label_type", UNSET)
        label_type: UpdateCollectionItemBodyLabelType | Unset
        if isinstance(_label_type, Unset):
            label_type = UNSET
        else:
            label_type = check_update_collection_item_body_label_type(_label_type)

        _page_quality = d.pop("page_quality", UNSET)
        page_quality: UpdateCollectionItemBodyPageQuality | Unset
        if isinstance(_page_quality, Unset):
            page_quality = UNSET
        else:
            page_quality = check_update_collection_item_body_page_quality(_page_quality)

        def _parse_grader_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grader_notes = _parse_grader_notes(d.pop("grader_notes", UNSET))

        _print_number = d.pop("print_number", UNSET)
        print_number: UpdateCollectionItemBodyPrintNumber | Unset
        if isinstance(_print_number, Unset):
            print_number = UNSET
        else:
            print_number = check_update_collection_item_body_print_number(_print_number)

        _signature_witness = d.pop("signature_witness", UNSET)
        signature_witness: UpdateCollectionItemBodySignatureWitness | Unset
        if isinstance(_signature_witness, Unset):
            signature_witness = UNSET
        else:
            signature_witness = check_update_collection_item_body_signature_witness(_signature_witness)

        def _parse_estimated_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_value = _parse_estimated_value(d.pop("estimated_value", UNSET))

        for_sale = d.pop("for_sale", UNSET)

        _status = d.pop("status", UNSET)
        status: UpdateCollectionItemBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_collection_item_body_status(_status)

        def _parse_sold_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sold_at = _parse_sold_at(d.pop("sold_at", UNSET))

        def _parse_price_sold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_sold = _parse_price_sold(d.pop("price_sold", UNSET))

        for_trade = d.pop("for_trade", UNSET)

        is_public = d.pop("is_public", UNSET)

        is_read = d.pop("is_read", UNSET)

        def _parse_read_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))

        update_collection_item_body = cls(
            variant_id=variant_id,
            condition=condition,
            notes=notes,
            price_paid=price_paid,
            format_=format_,
            purchase_source=purchase_source,
            purchase_store=purchase_store,
            custom_label=custom_label,
            bagged_at=bagged_at,
            personal_rating=personal_rating,
            tags=tags,
            comic_shop_id=comic_shop_id,
            acquisition_method=acquisition_method,
            purchased_at=purchased_at,
            storage_location=storage_location,
            is_signed=is_signed,
            signed_by=signed_by,
            is_variant=is_variant,
            variant_description=variant_description,
            variant_type=variant_type,
            graded=graded,
            grade_score=grade_score,
            grading_company=grading_company,
            grading_number=grading_number,
            label_type=label_type,
            page_quality=page_quality,
            grader_notes=grader_notes,
            print_number=print_number,
            signature_witness=signature_witness,
            estimated_value=estimated_value,
            for_sale=for_sale,
            status=status,
            sold_at=sold_at,
            price_sold=price_sold,
            for_trade=for_trade,
            is_public=is_public,
            is_read=is_read,
            read_at=read_at,
        )

        update_collection_item_body.additional_properties = d
        return update_collection_item_body

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
