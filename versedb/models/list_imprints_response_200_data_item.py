from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_imprints_response_200_data_item_publisher import ListImprintsResponse200DataItemPublisher


T = TypeVar("T", bound="ListImprintsResponse200DataItem")


@_attrs_define
class ListImprintsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        publisher (ListImprintsResponse200DataItemPublisher | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    publisher: ListImprintsResponse200DataItemPublisher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_imprints_response_200_data_item_publisher import (
            ListImprintsResponse200DataItemPublisher,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: ListImprintsResponse200DataItemPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = ListImprintsResponse200DataItemPublisher.from_dict(_publisher)

        list_imprints_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            publisher=publisher,
        )

        list_imprints_response_200_data_item.additional_properties = d
        return list_imprints_response_200_data_item

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
