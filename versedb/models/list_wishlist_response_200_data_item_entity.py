from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_wishlist_response_200_data_item_entity_series import ListWishlistResponse200DataItemEntitySeries


T = TypeVar("T", bound="ListWishlistResponse200DataItemEntity")


@_attrs_define
class ListWishlistResponse200DataItemEntity:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        issue_number (str | Unset):
        image_url (str | Unset):
        publisher (str | Unset):
        series (ListWishlistResponse200DataItemEntitySeries | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    issue_number: str | Unset = UNSET
    image_url: str | Unset = UNSET
    publisher: str | Unset = UNSET
    series: ListWishlistResponse200DataItemEntitySeries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        issue_number = self.issue_number

        image_url = self.image_url

        publisher = self.publisher

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_wishlist_response_200_data_item_entity_series import (
            ListWishlistResponse200DataItemEntitySeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        image_url = d.pop("image_url", UNSET)

        publisher = d.pop("publisher", UNSET)

        _series = d.pop("series", UNSET)
        series: ListWishlistResponse200DataItemEntitySeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = ListWishlistResponse200DataItemEntitySeries.from_dict(_series)

        list_wishlist_response_200_data_item_entity = cls(
            id=id,
            name=name,
            issue_number=issue_number,
            image_url=image_url,
            publisher=publisher,
            series=series,
        )

        list_wishlist_response_200_data_item_entity.additional_properties = d
        return list_wishlist_response_200_data_item_entity

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
