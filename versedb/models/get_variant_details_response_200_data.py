from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_variant_details_response_200_data_creators_item import (
        GetVariantDetailsResponse200DataCreatorsItem,
    )


T = TypeVar("T", bound="GetVariantDetailsResponse200Data")


@_attrs_define
class GetVariantDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        issue_id (int | Unset):
        variant_name (str | Unset):
        variant_type (str | Unset):
        ratio (str | Unset):
        cover_url (str | Unset):
        price (str | Unset):
        currency_code (str | Unset):
        formatted_price (str | Unset):
        ean (str | Unset):
        creators (list[GetVariantDetailsResponse200DataCreatorsItem] | Unset):
    """

    id: int | Unset = UNSET
    issue_id: int | Unset = UNSET
    variant_name: str | Unset = UNSET
    variant_type: str | Unset = UNSET
    ratio: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    price: str | Unset = UNSET
    currency_code: str | Unset = UNSET
    formatted_price: str | Unset = UNSET
    ean: str | Unset = UNSET
    creators: list[GetVariantDetailsResponse200DataCreatorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        issue_id = self.issue_id

        variant_name = self.variant_name

        variant_type = self.variant_type

        ratio = self.ratio

        cover_url = self.cover_url

        price = self.price

        currency_code = self.currency_code

        formatted_price = self.formatted_price

        ean = self.ean

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if variant_name is not UNSET:
            field_dict["variant_name"] = variant_name
        if variant_type is not UNSET:
            field_dict["variant_type"] = variant_type
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if price is not UNSET:
            field_dict["price"] = price
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if formatted_price is not UNSET:
            field_dict["formatted_price"] = formatted_price
        if ean is not UNSET:
            field_dict["ean"] = ean
        if creators is not UNSET:
            field_dict["creators"] = creators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_variant_details_response_200_data_creators_item import (
            GetVariantDetailsResponse200DataCreatorsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        issue_id = d.pop("issue_id", UNSET)

        variant_name = d.pop("variant_name", UNSET)

        variant_type = d.pop("variant_type", UNSET)

        ratio = d.pop("ratio", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        price = d.pop("price", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        formatted_price = d.pop("formatted_price", UNSET)

        ean = d.pop("ean", UNSET)

        _creators = d.pop("creators", UNSET)
        creators: list[GetVariantDetailsResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetVariantDetailsResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

        get_variant_details_response_200_data = cls(
            id=id,
            issue_id=issue_id,
            variant_name=variant_name,
            variant_type=variant_type,
            ratio=ratio,
            cover_url=cover_url,
            price=price,
            currency_code=currency_code,
            formatted_price=formatted_price,
            ean=ean,
            creators=creators,
        )

        get_variant_details_response_200_data.additional_properties = d
        return get_variant_details_response_200_data

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
