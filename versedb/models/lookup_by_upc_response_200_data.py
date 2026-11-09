from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_by_upc_response_200_data_publisher import LookupByUpcResponse200DataPublisher
    from ..models.lookup_by_upc_response_200_data_series import LookupByUpcResponse200DataSeries


T = TypeVar("T", bound="LookupByUpcResponse200Data")


@_attrs_define
class LookupByUpcResponse200Data:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        series_id (int | Unset):
        title_id (int | Unset):
        issue_number (str | Unset):
        name (str | Unset):
        solicitation (str | Unset):
        release_date (str | Unset):
        cover_date (str | Unset):
        cover_url (str | Unset):
        upc (str | Unset):
        lunar_code (str | Unset):
        universal_code (None | str | Unset):
        diamond_code (str | Unset):
        series (LookupByUpcResponse200DataSeries | Unset):
        publisher (LookupByUpcResponse200DataPublisher | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    series_id: int | Unset = UNSET
    title_id: int | Unset = UNSET
    issue_number: str | Unset = UNSET
    name: str | Unset = UNSET
    solicitation: str | Unset = UNSET
    release_date: str | Unset = UNSET
    cover_date: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    upc: str | Unset = UNSET
    lunar_code: str | Unset = UNSET
    universal_code: None | str | Unset = UNSET
    diamond_code: str | Unset = UNSET
    series: LookupByUpcResponse200DataSeries | Unset = UNSET
    publisher: LookupByUpcResponse200DataPublisher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        series_id = self.series_id

        title_id = self.title_id

        issue_number = self.issue_number

        name = self.name

        solicitation = self.solicitation

        release_date = self.release_date

        cover_date = self.cover_date

        cover_url = self.cover_url

        upc = self.upc

        lunar_code = self.lunar_code

        universal_code: None | str | Unset
        if isinstance(self.universal_code, Unset):
            universal_code = UNSET
        else:
            universal_code = self.universal_code

        diamond_code = self.diamond_code

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if title_id is not UNSET:
            field_dict["title_id"] = title_id
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if name is not UNSET:
            field_dict["name"] = name
        if solicitation is not UNSET:
            field_dict["solicitation"] = solicitation
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if cover_date is not UNSET:
            field_dict["cover_date"] = cover_date
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if upc is not UNSET:
            field_dict["upc"] = upc
        if lunar_code is not UNSET:
            field_dict["lunar_code"] = lunar_code
        if universal_code is not UNSET:
            field_dict["universal_code"] = universal_code
        if diamond_code is not UNSET:
            field_dict["diamond_code"] = diamond_code
        if series is not UNSET:
            field_dict["series"] = series
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_upc_response_200_data_publisher import LookupByUpcResponse200DataPublisher  # noqa: PLC0415
        from ..models.lookup_by_upc_response_200_data_series import LookupByUpcResponse200DataSeries  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        series_id = d.pop("series_id", UNSET)

        title_id = d.pop("title_id", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        name = d.pop("name", UNSET)

        solicitation = d.pop("solicitation", UNSET)

        release_date = d.pop("release_date", UNSET)

        cover_date = d.pop("cover_date", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        upc = d.pop("upc", UNSET)

        lunar_code = d.pop("lunar_code", UNSET)

        def _parse_universal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universal_code = _parse_universal_code(d.pop("universal_code", UNSET))

        diamond_code = d.pop("diamond_code", UNSET)

        _series = d.pop("series", UNSET)
        series: LookupByUpcResponse200DataSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = LookupByUpcResponse200DataSeries.from_dict(_series)

        _publisher = d.pop("publisher", UNSET)
        publisher: LookupByUpcResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = LookupByUpcResponse200DataPublisher.from_dict(_publisher)

        lookup_by_upc_response_200_data = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            title_id=title_id,
            issue_number=issue_number,
            name=name,
            solicitation=solicitation,
            release_date=release_date,
            cover_date=cover_date,
            cover_url=cover_url,
            upc=upc,
            lunar_code=lunar_code,
            universal_code=universal_code,
            diamond_code=diamond_code,
            series=series,
            publisher=publisher,
        )

        lookup_by_upc_response_200_data.additional_properties = d
        return lookup_by_upc_response_200_data

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
