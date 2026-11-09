from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_issue_variants_item_images_type_0 import (
        GetAnEventResponse200DataIssueVariantsItemImagesType0,
    )
    from ..models.get_an_event_response_200_data_issue_variants_item_variant_name_i18n import (
        GetAnEventResponse200DataIssueVariantsItemVariantNameI18N,
    )


T = TypeVar("T", bound="GetAnEventResponse200DataIssueVariantsItem")


@_attrs_define
class GetAnEventResponse200DataIssueVariantsItem:
    """
    Attributes:
        id (int):
        issue_id (int | None):
        variant_name (None | str):
        cover_url (None | str):
        images (GetAnEventResponse200DataIssueVariantsItemImagesType0 | None):
        variant_type (None | str):
        ratio (None | str):
        price (None | str):
        currency_code (None | str):
        formatted_price (None | str):
        ean (None | str):
        is_nsfw (bool | None):
        variant_name_i18n (GetAnEventResponse200DataIssueVariantsItemVariantNameI18N): One name per language, keyed by
            BCP 47 tag.
    """

    id: int
    issue_id: int | None
    variant_name: None | str
    cover_url: None | str
    images: GetAnEventResponse200DataIssueVariantsItemImagesType0 | None
    variant_type: None | str
    ratio: None | str
    price: None | str
    currency_code: None | str
    formatted_price: None | str
    ean: None | str
    is_nsfw: bool | None
    variant_name_i18n: GetAnEventResponse200DataIssueVariantsItemVariantNameI18N
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_an_event_response_200_data_issue_variants_item_images_type_0 import (
            GetAnEventResponse200DataIssueVariantsItemImagesType0,  # noqa: PLC0415
        )

        id = self.id

        issue_id: int | None
        issue_id = self.issue_id

        variant_name: None | str
        variant_name = self.variant_name

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetAnEventResponse200DataIssueVariantsItemImagesType0):
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

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

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
                "is_nsfw": is_nsfw,
                "variant_name_i18n": variant_name_i18n,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_issue_variants_item_images_type_0 import (
            GetAnEventResponse200DataIssueVariantsItemImagesType0,  # noqa: PLC0415
        )
        from ..models.get_an_event_response_200_data_issue_variants_item_variant_name_i18n import (
            GetAnEventResponse200DataIssueVariantsItemVariantNameI18N,  # noqa: PLC0415
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

        def _parse_images(data: object) -> GetAnEventResponse200DataIssueVariantsItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetAnEventResponse200DataIssueVariantsItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAnEventResponse200DataIssueVariantsItemImagesType0 | None, data)

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

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        variant_name_i18n = GetAnEventResponse200DataIssueVariantsItemVariantNameI18N.from_dict(
            d.pop("variant_name_i18n")
        )

        get_an_event_response_200_data_issue_variants_item = cls(
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
            is_nsfw=is_nsfw,
            variant_name_i18n=variant_name_i18n,
        )

        get_an_event_response_200_data_issue_variants_item.additional_properties = d
        return get_an_event_response_200_data_issue_variants_item

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
