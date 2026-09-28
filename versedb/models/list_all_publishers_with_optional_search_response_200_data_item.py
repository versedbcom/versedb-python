from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_all_publishers_with_optional_search_response_200_data_item_images import (
        ListAllPublishersWithOptionalSearchResponse200DataItemImages,
    )


T = TypeVar("T", bound="ListAllPublishersWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllPublishersWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        founded_year (int | Unset):
        headquarters (str | Unset):
        status (str | Unset):
        series_count (int | Unset):
        logo_url (str | Unset):
        images (ListAllPublishersWithOptionalSearchResponse200DataItemImages | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    founded_year: int | Unset = UNSET
    headquarters: str | Unset = UNSET
    status: str | Unset = UNSET
    series_count: int | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: ListAllPublishersWithOptionalSearchResponse200DataItemImages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        founded_year = self.founded_year

        headquarters = self.headquarters

        status = self.status

        series_count = self.series_count

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if status is not UNSET:
            field_dict["status"] = status
        if series_count is not UNSET:
            field_dict["series_count"] = series_count
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_publishers_with_optional_search_response_200_data_item_images import (
            ListAllPublishersWithOptionalSearchResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        founded_year = d.pop("founded_year", UNSET)

        headquarters = d.pop("headquarters", UNSET)

        status = d.pop("status", UNSET)

        series_count = d.pop("series_count", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListAllPublishersWithOptionalSearchResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListAllPublishersWithOptionalSearchResponse200DataItemImages.from_dict(_images)

        list_all_publishers_with_optional_search_response_200_data_item = cls(
            id=id,
            name=name,
            founded_year=founded_year,
            headquarters=headquarters,
            status=status,
            series_count=series_count,
            logo_url=logo_url,
            images=images,
        )

        list_all_publishers_with_optional_search_response_200_data_item.additional_properties = d
        return list_all_publishers_with_optional_search_response_200_data_item

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
