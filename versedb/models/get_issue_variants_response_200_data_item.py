from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_issue_variants_response_200_data_item_creators_item import (
        GetIssueVariantsResponse200DataItemCreatorsItem,
    )
    from ..models.get_issue_variants_response_200_data_item_images_type_0 import (
        GetIssueVariantsResponse200DataItemImagesType0,
    )
    from ..models.get_issue_variants_response_200_data_item_variant_name_i18n import (
        GetIssueVariantsResponse200DataItemVariantNameI18N,
    )


T = TypeVar("T", bound="GetIssueVariantsResponse200DataItem")


@_attrs_define
class GetIssueVariantsResponse200DataItem:
    """
    Attributes:
        id (int):
        issue_id (int | None):
        variant_name (None | str):
        cover_url (None | str):
        images (GetIssueVariantsResponse200DataItemImagesType0 | None):
        variant_type (None | str):
        ratio (None | str):
        price (None | str):
        currency_code (None | str):
        formatted_price (None | str):
        ean (None | str):
        release_date (None | str): This edition's own on-sale date (YYYY-MM-DD), for a later printing or an exclusive
            that ships apart from its issue. Null when it ships with the issue: use the issue's release_date.
        is_nsfw (bool):
        creators (list[GetIssueVariantsResponse200DataItemCreatorsItem]):
        variant_name_i18n (GetIssueVariantsResponse200DataItemVariantNameI18N): One name per language, keyed by BCP 47
            tag.
    """

    id: int
    issue_id: int | None
    variant_name: None | str
    cover_url: None | str
    images: GetIssueVariantsResponse200DataItemImagesType0 | None
    variant_type: None | str
    ratio: None | str
    price: None | str
    currency_code: None | str
    formatted_price: None | str
    ean: None | str
    release_date: None | str
    is_nsfw: bool
    creators: list[GetIssueVariantsResponse200DataItemCreatorsItem]
    variant_name_i18n: GetIssueVariantsResponse200DataItemVariantNameI18N
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_issue_variants_response_200_data_item_images_type_0 import (
            GetIssueVariantsResponse200DataItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        issue_id: int | None
        issue_id = self.issue_id

        variant_name: None | str
        variant_name = self.variant_name

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetIssueVariantsResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        variant_type: None | str
        variant_type = self.variant_type

        ratio: None | str
        ratio = self.ratio

        price: None | str
        price = self.price

        currency_code: None | str
        currency_code = self.currency_code

        formatted_price: None | str
        formatted_price = self.formatted_price

        ean: None | str
        ean = self.ean

        release_date: None | str
        release_date = self.release_date

        is_nsfw = self.is_nsfw

        creators = []
        for creators_item_data in self.creators:
            creators_item = creators_item_data.to_dict()
            creators.append(creators_item)

        variant_name_i18n = self.variant_name_i18n.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "issue_id": issue_id,
                "variant_name": variant_name,
                "cover_url": cover_url,
                "images": images,
                "variant_type": variant_type,
                "ratio": ratio,
                "price": price,
                "currency_code": currency_code,
                "formatted_price": formatted_price,
                "ean": ean,
                "release_date": release_date,
                "is_nsfw": is_nsfw,
                "creators": creators,
                "variant_name_i18n": variant_name_i18n,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_issue_variants_response_200_data_item_creators_item import (
            GetIssueVariantsResponse200DataItemCreatorsItem,  # noqa: PLC0415
        )
        from ..models.get_issue_variants_response_200_data_item_images_type_0 import (
            GetIssueVariantsResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.get_issue_variants_response_200_data_item_variant_name_i18n import (
            GetIssueVariantsResponse200DataItemVariantNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_issue_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issue_id = _parse_issue_id(d.pop("issue_id"))

        def _parse_variant_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_name = _parse_variant_name(d.pop("variant_name"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> GetIssueVariantsResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetIssueVariantsResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetIssueVariantsResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_variant_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_type = _parse_variant_type(d.pop("variant_type"))

        def _parse_ratio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ratio = _parse_ratio(d.pop("ratio"))

        def _parse_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        price = _parse_price(d.pop("price"))

        def _parse_currency_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency_code = _parse_currency_code(d.pop("currency_code"))

        def _parse_formatted_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formatted_price = _parse_formatted_price(d.pop("formatted_price"))

        def _parse_ean(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ean = _parse_ean(d.pop("ean"))

        def _parse_release_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        release_date = _parse_release_date(d.pop("release_date"))

        is_nsfw = d.pop("is_nsfw")

        creators = []
        _creators = d.pop("creators")
        for creators_item_data in _creators:
            creators_item = GetIssueVariantsResponse200DataItemCreatorsItem.from_dict(creators_item_data)

            creators.append(creators_item)

        variant_name_i18n = GetIssueVariantsResponse200DataItemVariantNameI18N.from_dict(d.pop("variant_name_i18n"))

        get_issue_variants_response_200_data_item = cls(
            id=id,
            issue_id=issue_id,
            variant_name=variant_name,
            cover_url=cover_url,
            images=images,
            variant_type=variant_type,
            ratio=ratio,
            price=price,
            currency_code=currency_code,
            formatted_price=formatted_price,
            ean=ean,
            release_date=release_date,
            is_nsfw=is_nsfw,
            creators=creators,
            variant_name_i18n=variant_name_i18n,
        )

        get_issue_variants_response_200_data_item.additional_properties = d
        return get_issue_variants_response_200_data_item

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
