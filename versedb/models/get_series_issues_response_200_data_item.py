from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_series_issues_response_200_data_item_name_i18n import GetSeriesIssuesResponse200DataItemNameI18N


T = TypeVar("T", bound="GetSeriesIssuesResponse200DataItem")


@_attrs_define
class GetSeriesIssuesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        number (str | Unset):
        name (str | Unset):
        name_i18n (GetSeriesIssuesResponse200DataItemNameI18N | Unset):
        release_date (str | Unset):
        cover_url (str | Unset):
        average_rating (float | Unset):
    """

    id: int | Unset = UNSET
    number: str | Unset = UNSET
    name: str | Unset = UNSET
    name_i18n: GetSeriesIssuesResponse200DataItemNameI18N | Unset = UNSET
    release_date: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    average_rating: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        name = self.name

        name_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_i18n, Unset):
            name_i18n = self.name_i18n.to_dict()

        release_date = self.release_date

        cover_url = self.cover_url

        average_rating = self.average_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if name_i18n is not UNSET:
            field_dict["name_i18n"] = name_i18n
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_issues_response_200_data_item_name_i18n import (
            GetSeriesIssuesResponse200DataItemNameI18N,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        _name_i18n = d.pop("name_i18n", UNSET)
        name_i18n: GetSeriesIssuesResponse200DataItemNameI18N | Unset
        if isinstance(_name_i18n, Unset):
            name_i18n = UNSET
        else:
            name_i18n = GetSeriesIssuesResponse200DataItemNameI18N.from_dict(_name_i18n)

        release_date = d.pop("release_date", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        get_series_issues_response_200_data_item = cls(
            id=id,
            number=number,
            name=name,
            name_i18n=name_i18n,
            release_date=release_date,
            cover_url=cover_url,
            average_rating=average_rating,
        )

        get_series_issues_response_200_data_item.additional_properties = d
        return get_series_issues_response_200_data_item

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
