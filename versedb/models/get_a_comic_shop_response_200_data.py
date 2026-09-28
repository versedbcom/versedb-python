from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_a_comic_shop_response_200_data_images import GetAComicShopResponse200DataImages
    from ..models.get_a_comic_shop_response_200_data_operating_hours import GetAComicShopResponse200DataOperatingHours


T = TypeVar("T", bound="GetAComicShopResponse200Data")


@_attrs_define
class GetAComicShopResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        address (str | Unset):
        city (str | Unset):
        state_province (str | Unset):
        postal_code (str | Unset):
        country (str | Unset):
        website (str | Unset):
        full_address (str | Unset):
        logo_url (str | Unset):
        images (GetAComicShopResponse200DataImages | Unset):
        operating_hours (GetAComicShopResponse200DataOperatingHours | Unset):
        services (list[str] | Unset):
        events (list[Any] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    address: str | Unset = UNSET
    city: str | Unset = UNSET
    state_province: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    country: str | Unset = UNSET
    website: str | Unset = UNSET
    full_address: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: GetAComicShopResponse200DataImages | Unset = UNSET
    operating_hours: GetAComicShopResponse200DataOperatingHours | Unset = UNSET
    services: list[str] | Unset = UNSET
    events: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        address = self.address

        city = self.city

        state_province = self.state_province

        postal_code = self.postal_code

        country = self.country

        website = self.website

        full_address = self.full_address

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        operating_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operating_hours, Unset):
            operating_hours = self.operating_hours.to_dict()

        services: list[str] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        events: list[Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["state_province"] = state_province
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country
        if website is not UNSET:
            field_dict["website"] = website
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images
        if operating_hours is not UNSET:
            field_dict["operating_hours"] = operating_hours
        if services is not UNSET:
            field_dict["services"] = services
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_comic_shop_response_200_data_images import (
            GetAComicShopResponse200DataImages,  # noqa: PLC0415
        )
        from ..models.get_a_comic_shop_response_200_data_operating_hours import (
            GetAComicShopResponse200DataOperatingHours,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        state_province = d.pop("state_province", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        website = d.pop("website", UNSET)

        full_address = d.pop("full_address", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetAComicShopResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetAComicShopResponse200DataImages.from_dict(_images)

        _operating_hours = d.pop("operating_hours", UNSET)
        operating_hours: GetAComicShopResponse200DataOperatingHours | Unset
        if isinstance(_operating_hours, Unset):
            operating_hours = UNSET
        else:
            operating_hours = GetAComicShopResponse200DataOperatingHours.from_dict(_operating_hours)

        services = cast(list[str], d.pop("services", UNSET))

        events = cast(list[Any], d.pop("events", UNSET))

        get_a_comic_shop_response_200_data = cls(
            id=id,
            name=name,
            address=address,
            city=city,
            state_province=state_province,
            postal_code=postal_code,
            country=country,
            website=website,
            full_address=full_address,
            logo_url=logo_url,
            images=images,
            operating_hours=operating_hours,
            services=services,
            events=events,
        )

        get_a_comic_shop_response_200_data.additional_properties = d
        return get_a_comic_shop_response_200_data

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
