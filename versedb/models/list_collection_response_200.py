from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_collection_response_200_data_item import ListCollectionResponse200DataItem
    from ..models.list_collection_response_200_links import ListCollectionResponse200Links
    from ..models.list_collection_response_200_meta import ListCollectionResponse200Meta


T = TypeVar("T", bound="ListCollectionResponse200")


@_attrs_define
class ListCollectionResponse200:
    """
    Attributes:
        data (list[ListCollectionResponse200DataItem] | Unset):
        links (ListCollectionResponse200Links | Unset):
        meta (ListCollectionResponse200Meta | Unset):
    """

    data: list[ListCollectionResponse200DataItem] | Unset = UNSET
    links: ListCollectionResponse200Links | Unset = UNSET
    meta: ListCollectionResponse200Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collection_response_200_data_item import ListCollectionResponse200DataItem  # noqa: PLC0415
        from ..models.list_collection_response_200_links import ListCollectionResponse200Links  # noqa: PLC0415
        from ..models.list_collection_response_200_meta import ListCollectionResponse200Meta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ListCollectionResponse200DataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ListCollectionResponse200DataItem.from_dict(data_item_data)

                data.append(data_item)

        _links = d.pop("links", UNSET)
        links: ListCollectionResponse200Links | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListCollectionResponse200Links.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: ListCollectionResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ListCollectionResponse200Meta.from_dict(_meta)

        list_collection_response_200 = cls(
            data=data,
            links=links,
            meta=meta,
        )

        list_collection_response_200.additional_properties = d
        return list_collection_response_200

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
