from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_pull_list_response_200_data_item_series_publisher import (
        ListPullListResponse200DataItemSeriesPublisher,
    )


T = TypeVar("T", bound="ListPullListResponse200DataItemSeries")


@_attrs_define
class ListPullListResponse200DataItemSeries:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        publisher (ListPullListResponse200DataItemSeriesPublisher | Unset):
        cover_url (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    publisher: ListPullListResponse200DataItemSeriesPublisher | Unset = UNSET
    cover_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_pull_list_response_200_data_item_series_publisher import (
            ListPullListResponse200DataItemSeriesPublisher,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: ListPullListResponse200DataItemSeriesPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = ListPullListResponse200DataItemSeriesPublisher.from_dict(_publisher)

        cover_url = d.pop("cover_url", UNSET)

        list_pull_list_response_200_data_item_series = cls(
            id=id,
            name=name,
            publisher=publisher,
            cover_url=cover_url,
        )

        list_pull_list_response_200_data_item_series.additional_properties = d
        return list_pull_list_response_200_data_item_series

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
