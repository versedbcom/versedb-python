from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_list_response_200_data_items_item_entity_series import GetListResponse200DataItemsItemEntitySeries


T = TypeVar("T", bound="GetListResponse200DataItemsItemEntity")


@_attrs_define
class GetListResponse200DataItemsItemEntity:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        name (str | Unset):
        issue_number (str | Unset):
        release_date (str | Unset):
        image_url (str | Unset):
        is_nsfw (bool | Unset):
        publisher (str | Unset):
        series (GetListResponse200DataItemsItemEntitySeries | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    issue_number: str | Unset = UNSET
    release_date: str | Unset = UNSET
    image_url: str | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    publisher: str | Unset = UNSET
    series: GetListResponse200DataItemsItemEntitySeries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        issue_number = self.issue_number

        release_date = self.release_date

        image_url = self.image_url

        is_nsfw = self.is_nsfw

        publisher = self.publisher

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_list_response_200_data_items_item_entity_series import (
            GetListResponse200DataItemsItemEntitySeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        release_date = d.pop("release_date", UNSET)

        image_url = d.pop("image_url", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        publisher = d.pop("publisher", UNSET)

        _series = d.pop("series", UNSET)
        series: GetListResponse200DataItemsItemEntitySeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = GetListResponse200DataItemsItemEntitySeries.from_dict(_series)

        get_list_response_200_data_items_item_entity = cls(
            id=id,
            slug=slug,
            name=name,
            issue_number=issue_number,
            release_date=release_date,
            image_url=image_url,
            is_nsfw=is_nsfw,
            publisher=publisher,
            series=series,
        )

        get_list_response_200_data_items_item_entity.additional_properties = d
        return get_list_response_200_data_items_item_entity

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
