from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_pull_list_issue_covers_response_200_data_options_item_kind import (
    GetPullListIssueCoversResponse200DataOptionsItemKind,
    check_get_pull_list_issue_covers_response_200_data_options_item_kind,
)

if TYPE_CHECKING:
    from ..models.get_pull_list_issue_covers_response_200_data_options_item_images_type_0 import (
        GetPullListIssueCoversResponse200DataOptionsItemImagesType0,
    )


T = TypeVar("T", bound="GetPullListIssueCoversResponse200DataOptionsItem")


@_attrs_define
class GetPullListIssueCoversResponse200DataOptionsItem:
    """
    Attributes:
        variant_id (int | None): The variant's ID; null for the main cover, the issue's standard cover.
        code (None | str): The letter the variant's name starts with ("B" for "Cover B Jock Variant"); null for the main
            cover and unlettered variants.
        name (None | str): The variant's name; null for the main cover.
        type_ (None | str):
        ratio (None | str): The ratio a shop orders to get the cover, when the catalog has one.
        kind (GetPullListIssueCoversResponse200DataOptionsItemKind): `ratio` for an incentive or ratio variant, or any
            variant with a ratio; `exclusive` for a convention or retailer exclusive; `regular` for the rest and for the
            main cover.
        images (GetPullListIssueCoversResponse200DataOptionsItemImagesType0 | None):
        price (None | str): The cover's price. A regular variant with none listed carries the issue's; a ratio or
            exclusive cover with none has null, since the shop sets it.
        price_from_issue (bool): True when `price` is the issue's, for a regular variant with no price of its own.
        currency (None | str): The price's currency code; null for an untagged price.
        cover_nsfw (bool):
        selected (bool): The user is getting this cover.
    """

    variant_id: int | None
    code: None | str
    name: None | str
    type_: None | str
    ratio: None | str
    kind: GetPullListIssueCoversResponse200DataOptionsItemKind
    images: GetPullListIssueCoversResponse200DataOptionsItemImagesType0 | None
    price: None | str
    price_from_issue: bool
    currency: None | str
    cover_nsfw: bool
    selected: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_pull_list_issue_covers_response_200_data_options_item_images_type_0 import (
            GetPullListIssueCoversResponse200DataOptionsItemImagesType0,  # noqa: PLC0415
        )

        variant_id: int | None
        variant_id = self.variant_id

        code: None | str
        code = self.code

        name: None | str
        name = self.name

        type_: None | str
        type_ = self.type_

        ratio: None | str
        ratio = self.ratio

        kind: str = self.kind

        images: dict[str, Any] | None
        if isinstance(self.images, GetPullListIssueCoversResponse200DataOptionsItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        price: None | str
        price = self.price

        price_from_issue = self.price_from_issue

        currency: None | str
        currency = self.currency

        cover_nsfw = self.cover_nsfw

        selected = self.selected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant_id": variant_id,
                "code": code,
                "name": name,
                "type": type_,
                "ratio": ratio,
                "kind": kind,
                "images": images,
                "price": price,
                "price_from_issue": price_from_issue,
                "currency": currency,
                "cover_nsfw": cover_nsfw,
                "selected": selected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_pull_list_issue_covers_response_200_data_options_item_images_type_0 import (
            GetPullListIssueCoversResponse200DataOptionsItemImagesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_ratio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ratio = _parse_ratio(d.pop("ratio"))

        kind = check_get_pull_list_issue_covers_response_200_data_options_item_kind(d.pop("kind"))

        def _parse_images(data: object) -> GetPullListIssueCoversResponse200DataOptionsItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetPullListIssueCoversResponse200DataOptionsItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPullListIssueCoversResponse200DataOptionsItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        price = _parse_price(d.pop("price"))

        price_from_issue = d.pop("price_from_issue")

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        cover_nsfw = d.pop("cover_nsfw")

        selected = d.pop("selected")

        get_pull_list_issue_covers_response_200_data_options_item = cls(
            variant_id=variant_id,
            code=code,
            name=name,
            type_=type_,
            ratio=ratio,
            kind=kind,
            images=images,
            price=price,
            price_from_issue=price_from_issue,
            currency=currency,
            cover_nsfw=cover_nsfw,
            selected=selected,
        )

        get_pull_list_issue_covers_response_200_data_options_item.additional_properties = d
        return get_pull_list_issue_covers_response_200_data_options_item

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
