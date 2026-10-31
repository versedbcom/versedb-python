from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_events_response_200_data_item_images import ListEventsResponse200DataItemImages


T = TypeVar("T", bound="ListEventsResponse200DataItem")


@_attrs_define
class ListEventsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        start_time (None | str | Unset):
        end_time (None | str | Unset):
        timezone (str | Unset):
        is_online (bool | Unset):
        is_fcbd (bool | Unset):
        venue_name (str | Unset):
        city (str | Unset):
        region (str | Unset):
        country_code (str | Unset):
        full_location (str | Unset):
        logo_url (str | Unset):
        images (ListEventsResponse200DataItemImages | Unset):
        ticket_price (str | Unset):
        follower_count (int | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    start_time: None | str | Unset = UNSET
    end_time: None | str | Unset = UNSET
    timezone: str | Unset = UNSET
    is_online: bool | Unset = UNSET
    is_fcbd: bool | Unset = UNSET
    venue_name: str | Unset = UNSET
    city: str | Unset = UNSET
    region: str | Unset = UNSET
    country_code: str | Unset = UNSET
    full_location: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: ListEventsResponse200DataItemImages | Unset = UNSET
    ticket_price: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        type_ = self.type_

        status = self.status

        start_date = self.start_date

        end_date = self.end_date

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        timezone = self.timezone

        is_online = self.is_online

        is_fcbd = self.is_fcbd

        venue_name = self.venue_name

        city = self.city

        region = self.region

        country_code = self.country_code

        full_location = self.full_location

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        ticket_price = self.ticket_price

        follower_count = self.follower_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if is_fcbd is not UNSET:
            field_dict["is_fcbd"] = is_fcbd
        if venue_name is not UNSET:
            field_dict["venue_name"] = venue_name
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if full_location is not UNSET:
            field_dict["full_location"] = full_location
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images
        if ticket_price is not UNSET:
            field_dict["ticket_price"] = ticket_price
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_response_200_data_item_images import ListEventsResponse200DataItemImages  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        def _parse_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        timezone = d.pop("timezone", UNSET)

        is_online = d.pop("is_online", UNSET)

        is_fcbd = d.pop("is_fcbd", UNSET)

        venue_name = d.pop("venue_name", UNSET)

        city = d.pop("city", UNSET)

        region = d.pop("region", UNSET)

        country_code = d.pop("country_code", UNSET)

        full_location = d.pop("full_location", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListEventsResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListEventsResponse200DataItemImages.from_dict(_images)

        ticket_price = d.pop("ticket_price", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        list_events_response_200_data_item = cls(
            id=id,
            slug=slug,
            name=name,
            type_=type_,
            status=status,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            timezone=timezone,
            is_online=is_online,
            is_fcbd=is_fcbd,
            venue_name=venue_name,
            city=city,
            region=region,
            country_code=country_code,
            full_location=full_location,
            logo_url=logo_url,
            images=images,
            ticket_price=ticket_price,
            follower_count=follower_count,
        )

        list_events_response_200_data_item.additional_properties = d
        return list_events_response_200_data_item

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
