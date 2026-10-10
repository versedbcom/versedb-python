from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_attendees_preview import GetAnEventResponse200DataAttendeesPreview
    from ..models.get_an_event_response_200_data_creators_item import GetAnEventResponse200DataCreatorsItem
    from ..models.get_an_event_response_200_data_images import GetAnEventResponse200DataImages


T = TypeVar("T", bound="GetAnEventResponse200Data")


@_attrs_define
class GetAnEventResponse200Data:
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
        street_address (str | Unset):
        city (str | Unset):
        region (str | Unset):
        postal_code (str | Unset):
        country_code (str | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        full_location (str | Unset):
        google_maps_url (str | Unset):
        logo_url (str | Unset):
        images (GetAnEventResponse200DataImages | Unset):
        static_map_url (str | Unset):
        event_url (str | Unset):
        ticket_price_min (int | Unset):
        ticket_price_max (int | Unset):
        ticket_currency (str | Unset):
        ticket_price (str | Unset):
        follower_count (int | Unset):
        event_franchise_id (int | Unset):
        creators (list[GetAnEventResponse200DataCreatorsItem] | Unset):
        issues (list[Any] | Unset):
        issue_variants (list[Any] | Unset):
        attendees_preview (GetAnEventResponse200DataAttendeesPreview | Unset):
        related_events (list[Any] | Unset):
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
    street_address: str | Unset = UNSET
    city: str | Unset = UNSET
    region: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    country_code: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    full_location: str | Unset = UNSET
    google_maps_url: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: GetAnEventResponse200DataImages | Unset = UNSET
    static_map_url: str | Unset = UNSET
    event_url: str | Unset = UNSET
    ticket_price_min: int | Unset = UNSET
    ticket_price_max: int | Unset = UNSET
    ticket_currency: str | Unset = UNSET
    ticket_price: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    event_franchise_id: int | Unset = UNSET
    creators: list[GetAnEventResponse200DataCreatorsItem] | Unset = UNSET
    issues: list[Any] | Unset = UNSET
    issue_variants: list[Any] | Unset = UNSET
    attendees_preview: GetAnEventResponse200DataAttendeesPreview | Unset = UNSET
    related_events: list[Any] | Unset = UNSET
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

        street_address = self.street_address

        city = self.city

        region = self.region

        postal_code = self.postal_code

        country_code = self.country_code

        latitude = self.latitude

        longitude = self.longitude

        full_location = self.full_location

        google_maps_url = self.google_maps_url

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        static_map_url = self.static_map_url

        event_url = self.event_url

        ticket_price_min = self.ticket_price_min

        ticket_price_max = self.ticket_price_max

        ticket_currency = self.ticket_currency

        ticket_price = self.ticket_price

        follower_count = self.follower_count

        event_franchise_id = self.event_franchise_id

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        issues: list[Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues

        issue_variants: list[Any] | Unset = UNSET
        if not isinstance(self.issue_variants, Unset):
            issue_variants = self.issue_variants

        attendees_preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attendees_preview, Unset):
            attendees_preview = self.attendees_preview.to_dict()

        related_events: list[Any] | Unset = UNSET
        if not isinstance(self.related_events, Unset):
            related_events = self.related_events

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
        if street_address is not UNSET:
            field_dict["street_address"] = street_address
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if full_location is not UNSET:
            field_dict["full_location"] = full_location
        if google_maps_url is not UNSET:
            field_dict["google_maps_url"] = google_maps_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images
        if static_map_url is not UNSET:
            field_dict["static_map_url"] = static_map_url
        if event_url is not UNSET:
            field_dict["event_url"] = event_url
        if ticket_price_min is not UNSET:
            field_dict["ticket_price_min"] = ticket_price_min
        if ticket_price_max is not UNSET:
            field_dict["ticket_price_max"] = ticket_price_max
        if ticket_currency is not UNSET:
            field_dict["ticket_currency"] = ticket_currency
        if ticket_price is not UNSET:
            field_dict["ticket_price"] = ticket_price
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if event_franchise_id is not UNSET:
            field_dict["event_franchise_id"] = event_franchise_id
        if creators is not UNSET:
            field_dict["creators"] = creators
        if issues is not UNSET:
            field_dict["issues"] = issues
        if issue_variants is not UNSET:
            field_dict["issue_variants"] = issue_variants
        if attendees_preview is not UNSET:
            field_dict["attendees_preview"] = attendees_preview
        if related_events is not UNSET:
            field_dict["related_events"] = related_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_attendees_preview import GetAnEventResponse200DataAttendeesPreview  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_creators_item import GetAnEventResponse200DataCreatorsItem  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_images import GetAnEventResponse200DataImages  # noqa: PLC0415

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

        street_address = d.pop("street_address", UNSET)

        city = d.pop("city", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        full_location = d.pop("full_location", UNSET)

        google_maps_url = d.pop("google_maps_url", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetAnEventResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetAnEventResponse200DataImages.from_dict(_images)

        static_map_url = d.pop("static_map_url", UNSET)

        event_url = d.pop("event_url", UNSET)

        ticket_price_min = d.pop("ticket_price_min", UNSET)

        ticket_price_max = d.pop("ticket_price_max", UNSET)

        ticket_currency = d.pop("ticket_currency", UNSET)

        ticket_price = d.pop("ticket_price", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        event_franchise_id = d.pop("event_franchise_id", UNSET)

        _creators = d.pop("creators", UNSET)
        creators: list[GetAnEventResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetAnEventResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

        issues = cast(list[Any], d.pop("issues", UNSET))

        issue_variants = cast(list[Any], d.pop("issue_variants", UNSET))

        _attendees_preview = d.pop("attendees_preview", UNSET)
        attendees_preview: GetAnEventResponse200DataAttendeesPreview | Unset
        if isinstance(_attendees_preview, Unset):
            attendees_preview = UNSET
        else:
            attendees_preview = GetAnEventResponse200DataAttendeesPreview.from_dict(_attendees_preview)

        related_events = cast(list[Any], d.pop("related_events", UNSET))

        get_an_event_response_200_data = cls(
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
            street_address=street_address,
            city=city,
            region=region,
            postal_code=postal_code,
            country_code=country_code,
            latitude=latitude,
            longitude=longitude,
            full_location=full_location,
            google_maps_url=google_maps_url,
            logo_url=logo_url,
            images=images,
            static_map_url=static_map_url,
            event_url=event_url,
            ticket_price_min=ticket_price_min,
            ticket_price_max=ticket_price_max,
            ticket_currency=ticket_currency,
            ticket_price=ticket_price,
            follower_count=follower_count,
            event_franchise_id=event_franchise_id,
            creators=creators,
            issues=issues,
            issue_variants=issue_variants,
            attendees_preview=attendees_preview,
            related_events=related_events,
        )

        get_an_event_response_200_data.additional_properties = d
        return get_an_event_response_200_data

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
