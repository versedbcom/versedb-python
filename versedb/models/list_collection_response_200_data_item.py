from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_collection_response_200_data_item_collectable import ListCollectionResponse200DataItemCollectable
    from ..models.list_collection_response_200_data_item_comic_shop import ListCollectionResponse200DataItemComicShop


T = TypeVar("T", bound="ListCollectionResponse200DataItem")


@_attrs_define
class ListCollectionResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        user_id (int | Unset):
        collectable_type (str | Unset):
        collectable_id (int | Unset):
        variant_id (None | str | Unset):
        condition (str | Unset):
        purchased_at (str | Unset):
        notes (str | Unset):
        format_ (str | Unset):
        storage_location (str | Unset):
        price_paid (float | Unset):
        is_variant (bool | Unset):
        variant_description (None | str | Unset):
        variant_type (None | str | Unset):
        graded (bool | Unset):
        grade_score (str | Unset):
        grading_company (str | Unset):
        grading_number (str | Unset):
        label_type (str | Unset):
        page_quality (str | Unset):
        grader_notes (None | str | Unset):
        purchase_source (str | Unset):
        comic_shop_id (int | Unset):
        comic_shop (ListCollectionResponse200DataItemComicShop | Unset):
        acquisition_method (str | Unset):
        is_signed (bool | Unset):
        signed_by (None | str | Unset):
        signature_witness (None | str | Unset):
        signature_authenticated (bool | Unset):
        is_cgc_ss (bool | Unset):
        print_number (int | Unset):
        estimated_value (float | Unset):
        value_last_updated (str | Unset):
        for_sale (bool | Unset):
        for_trade (bool | Unset):
        is_public (bool | Unset):
        cover_scan_url (None | str | Unset):
        cover_scan_url_lg (None | str | Unset):
        cover_scan_uploaded_at (None | str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
        collectable (ListCollectionResponse200DataItemCollectable | Unset):
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    collectable_type: str | Unset = UNSET
    collectable_id: int | Unset = UNSET
    variant_id: None | str | Unset = UNSET
    condition: str | Unset = UNSET
    purchased_at: str | Unset = UNSET
    notes: str | Unset = UNSET
    format_: str | Unset = UNSET
    storage_location: str | Unset = UNSET
    price_paid: float | Unset = UNSET
    is_variant: bool | Unset = UNSET
    variant_description: None | str | Unset = UNSET
    variant_type: None | str | Unset = UNSET
    graded: bool | Unset = UNSET
    grade_score: str | Unset = UNSET
    grading_company: str | Unset = UNSET
    grading_number: str | Unset = UNSET
    label_type: str | Unset = UNSET
    page_quality: str | Unset = UNSET
    grader_notes: None | str | Unset = UNSET
    purchase_source: str | Unset = UNSET
    comic_shop_id: int | Unset = UNSET
    comic_shop: ListCollectionResponse200DataItemComicShop | Unset = UNSET
    acquisition_method: str | Unset = UNSET
    is_signed: bool | Unset = UNSET
    signed_by: None | str | Unset = UNSET
    signature_witness: None | str | Unset = UNSET
    signature_authenticated: bool | Unset = UNSET
    is_cgc_ss: bool | Unset = UNSET
    print_number: int | Unset = UNSET
    estimated_value: float | Unset = UNSET
    value_last_updated: str | Unset = UNSET
    for_sale: bool | Unset = UNSET
    for_trade: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    cover_scan_url: None | str | Unset = UNSET
    cover_scan_url_lg: None | str | Unset = UNSET
    cover_scan_uploaded_at: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    collectable: ListCollectionResponse200DataItemCollectable | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        collectable_type = self.collectable_type

        collectable_id = self.collectable_id

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        condition = self.condition

        purchased_at = self.purchased_at

        notes = self.notes

        format_ = self.format_

        storage_location = self.storage_location

        price_paid = self.price_paid

        is_variant = self.is_variant

        variant_description: None | str | Unset
        if isinstance(self.variant_description, Unset):
            variant_description = UNSET
        else:
            variant_description = self.variant_description

        variant_type: None | str | Unset
        if isinstance(self.variant_type, Unset):
            variant_type = UNSET
        else:
            variant_type = self.variant_type

        graded = self.graded

        grade_score = self.grade_score

        grading_company = self.grading_company

        grading_number = self.grading_number

        label_type = self.label_type

        page_quality = self.page_quality

        grader_notes: None | str | Unset
        if isinstance(self.grader_notes, Unset):
            grader_notes = UNSET
        else:
            grader_notes = self.grader_notes

        purchase_source = self.purchase_source

        comic_shop_id = self.comic_shop_id

        comic_shop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comic_shop, Unset):
            comic_shop = self.comic_shop.to_dict()

        acquisition_method = self.acquisition_method

        is_signed = self.is_signed

        signed_by: None | str | Unset
        if isinstance(self.signed_by, Unset):
            signed_by = UNSET
        else:
            signed_by = self.signed_by

        signature_witness: None | str | Unset
        if isinstance(self.signature_witness, Unset):
            signature_witness = UNSET
        else:
            signature_witness = self.signature_witness

        signature_authenticated = self.signature_authenticated

        is_cgc_ss = self.is_cgc_ss

        print_number = self.print_number

        estimated_value = self.estimated_value

        value_last_updated = self.value_last_updated

        for_sale = self.for_sale

        for_trade = self.for_trade

        is_public = self.is_public

        cover_scan_url: None | str | Unset
        if isinstance(self.cover_scan_url, Unset):
            cover_scan_url = UNSET
        else:
            cover_scan_url = self.cover_scan_url

        cover_scan_url_lg: None | str | Unset
        if isinstance(self.cover_scan_url_lg, Unset):
            cover_scan_url_lg = UNSET
        else:
            cover_scan_url_lg = self.cover_scan_url_lg

        cover_scan_uploaded_at: None | str | Unset
        if isinstance(self.cover_scan_uploaded_at, Unset):
            cover_scan_uploaded_at = UNSET
        else:
            cover_scan_uploaded_at = self.cover_scan_uploaded_at

        created_at = self.created_at

        updated_at = self.updated_at

        collectable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collectable, Unset):
            collectable = self.collectable.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if collectable_type is not UNSET:
            field_dict["collectable_type"] = collectable_type
        if collectable_id is not UNSET:
            field_dict["collectable_id"] = collectable_id
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if format_ is not UNSET:
            field_dict["format"] = format_
        if storage_location is not UNSET:
            field_dict["storage_location"] = storage_location
        if price_paid is not UNSET:
            field_dict["price_paid"] = price_paid
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
        if purchase_source is not UNSET:
            field_dict["purchase_source"] = purchase_source
        if comic_shop_id is not UNSET:
            field_dict["comic_shop_id"] = comic_shop_id
        if comic_shop is not UNSET:
            field_dict["comic_shop"] = comic_shop
        if acquisition_method is not UNSET:
            field_dict["acquisition_method"] = acquisition_method
        if is_signed is not UNSET:
            field_dict["is_signed"] = is_signed
        if signed_by is not UNSET:
            field_dict["signed_by"] = signed_by
        if signature_witness is not UNSET:
            field_dict["signature_witness"] = signature_witness
        if signature_authenticated is not UNSET:
            field_dict["signature_authenticated"] = signature_authenticated
        if is_cgc_ss is not UNSET:
            field_dict["is_cgc_ss"] = is_cgc_ss
        if print_number is not UNSET:
            field_dict["print_number"] = print_number
        if estimated_value is not UNSET:
            field_dict["estimated_value"] = estimated_value
        if value_last_updated is not UNSET:
            field_dict["value_last_updated"] = value_last_updated
        if for_sale is not UNSET:
            field_dict["for_sale"] = for_sale
        if for_trade is not UNSET:
            field_dict["for_trade"] = for_trade
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if cover_scan_url is not UNSET:
            field_dict["cover_scan_url"] = cover_scan_url
        if cover_scan_url_lg is not UNSET:
            field_dict["cover_scan_url_lg"] = cover_scan_url_lg
        if cover_scan_uploaded_at is not UNSET:
            field_dict["cover_scan_uploaded_at"] = cover_scan_uploaded_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if collectable is not UNSET:
            field_dict["collectable"] = collectable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collection_response_200_data_item_collectable import (
            ListCollectionResponse200DataItemCollectable,  # noqa: PLC0415
        )
        from ..models.list_collection_response_200_data_item_comic_shop import (
            ListCollectionResponse200DataItemComicShop,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        collectable_type = d.pop("collectable_type", UNSET)

        collectable_id = d.pop("collectable_id", UNSET)

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variant_id", UNSET))

        condition = d.pop("condition", UNSET)

        purchased_at = d.pop("purchased_at", UNSET)

        notes = d.pop("notes", UNSET)

        format_ = d.pop("format", UNSET)

        storage_location = d.pop("storage_location", UNSET)

        price_paid = d.pop("price_paid", UNSET)

        is_variant = d.pop("is_variant", UNSET)

        def _parse_variant_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_description = _parse_variant_description(d.pop("variant_description", UNSET))

        def _parse_variant_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_type = _parse_variant_type(d.pop("variant_type", UNSET))

        graded = d.pop("graded", UNSET)

        grade_score = d.pop("grade_score", UNSET)

        grading_company = d.pop("grading_company", UNSET)

        grading_number = d.pop("grading_number", UNSET)

        label_type = d.pop("label_type", UNSET)

        page_quality = d.pop("page_quality", UNSET)

        def _parse_grader_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grader_notes = _parse_grader_notes(d.pop("grader_notes", UNSET))

        purchase_source = d.pop("purchase_source", UNSET)

        comic_shop_id = d.pop("comic_shop_id", UNSET)

        _comic_shop = d.pop("comic_shop", UNSET)
        comic_shop: ListCollectionResponse200DataItemComicShop | Unset
        if isinstance(_comic_shop, Unset):
            comic_shop = UNSET
        else:
            comic_shop = ListCollectionResponse200DataItemComicShop.from_dict(_comic_shop)

        acquisition_method = d.pop("acquisition_method", UNSET)

        is_signed = d.pop("is_signed", UNSET)

        def _parse_signed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signed_by = _parse_signed_by(d.pop("signed_by", UNSET))

        def _parse_signature_witness(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_witness = _parse_signature_witness(d.pop("signature_witness", UNSET))

        signature_authenticated = d.pop("signature_authenticated", UNSET)

        is_cgc_ss = d.pop("is_cgc_ss", UNSET)

        print_number = d.pop("print_number", UNSET)

        estimated_value = d.pop("estimated_value", UNSET)

        value_last_updated = d.pop("value_last_updated", UNSET)

        for_sale = d.pop("for_sale", UNSET)

        for_trade = d.pop("for_trade", UNSET)

        is_public = d.pop("is_public", UNSET)

        def _parse_cover_scan_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_scan_url = _parse_cover_scan_url(d.pop("cover_scan_url", UNSET))

        def _parse_cover_scan_url_lg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_scan_url_lg = _parse_cover_scan_url_lg(d.pop("cover_scan_url_lg", UNSET))

        def _parse_cover_scan_uploaded_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_scan_uploaded_at = _parse_cover_scan_uploaded_at(d.pop("cover_scan_uploaded_at", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _collectable = d.pop("collectable", UNSET)
        collectable: ListCollectionResponse200DataItemCollectable | Unset
        if isinstance(_collectable, Unset):
            collectable = UNSET
        else:
            collectable = ListCollectionResponse200DataItemCollectable.from_dict(_collectable)

        list_collection_response_200_data_item = cls(
            id=id,
            user_id=user_id,
            collectable_type=collectable_type,
            collectable_id=collectable_id,
            variant_id=variant_id,
            condition=condition,
            purchased_at=purchased_at,
            notes=notes,
            format_=format_,
            storage_location=storage_location,
            price_paid=price_paid,
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
            purchase_source=purchase_source,
            comic_shop_id=comic_shop_id,
            comic_shop=comic_shop,
            acquisition_method=acquisition_method,
            is_signed=is_signed,
            signed_by=signed_by,
            signature_witness=signature_witness,
            signature_authenticated=signature_authenticated,
            is_cgc_ss=is_cgc_ss,
            print_number=print_number,
            estimated_value=estimated_value,
            value_last_updated=value_last_updated,
            for_sale=for_sale,
            for_trade=for_trade,
            is_public=is_public,
            cover_scan_url=cover_scan_url,
            cover_scan_url_lg=cover_scan_url_lg,
            cover_scan_uploaded_at=cover_scan_uploaded_at,
            created_at=created_at,
            updated_at=updated_at,
            collectable=collectable,
        )

        list_collection_response_200_data_item.additional_properties = d
        return list_collection_response_200_data_item

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
