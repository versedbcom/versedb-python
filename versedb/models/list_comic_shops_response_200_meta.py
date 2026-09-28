from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_comic_shops_response_200_meta_ip_location import ListComicShopsResponse200MetaIpLocation


T = TypeVar("T", bound="ListComicShopsResponse200Meta")


@_attrs_define
class ListComicShopsResponse200Meta:
    """
    Attributes:
        current_page (int | Unset):
        last_page (int | Unset):
        per_page (int | Unset):
        total (int | Unset):
        ip_location (ListComicShopsResponse200MetaIpLocation | Unset):
    """

    current_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    per_page: int | Unset = UNSET
    total: int | Unset = UNSET
    ip_location: ListComicShopsResponse200MetaIpLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        total = self.total

        ip_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_location, Unset):
            ip_location = self.ip_location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if total is not UNSET:
            field_dict["total"] = total
        if ip_location is not UNSET:
            field_dict["ip_location"] = ip_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_comic_shops_response_200_meta_ip_location import (
            ListComicShopsResponse200MetaIpLocation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        current_page = d.pop("current_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        per_page = d.pop("per_page", UNSET)

        total = d.pop("total", UNSET)

        _ip_location = d.pop("ip_location", UNSET)
        ip_location: ListComicShopsResponse200MetaIpLocation | Unset
        if isinstance(_ip_location, Unset):
            ip_location = UNSET
        else:
            ip_location = ListComicShopsResponse200MetaIpLocation.from_dict(_ip_location)

        list_comic_shops_response_200_meta = cls(
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            total=total,
            ip_location=ip_location,
        )

        list_comic_shops_response_200_meta.additional_properties = d
        return list_comic_shops_response_200_meta

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
