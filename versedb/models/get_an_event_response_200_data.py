from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_an_event_response_200_data_aliases_i18n import GetAnEventResponse200DataAliasesI18N
    from ..models.get_an_event_response_200_data_attendees_preview import GetAnEventResponse200DataAttendeesPreview
    from ..models.get_an_event_response_200_data_creators_item import GetAnEventResponse200DataCreatorsItem
    from ..models.get_an_event_response_200_data_images_type_0 import GetAnEventResponse200DataImagesType0
    from ..models.get_an_event_response_200_data_issue_variants_item import GetAnEventResponse200DataIssueVariantsItem
    from ..models.get_an_event_response_200_data_issues_item import GetAnEventResponse200DataIssuesItem
    from ..models.get_an_event_response_200_data_name_i18n import GetAnEventResponse200DataNameI18N
    from ..models.get_an_event_response_200_data_related_events_item import GetAnEventResponse200DataRelatedEventsItem
    from ..models.get_an_event_response_200_data_store import GetAnEventResponse200DataStore


T = TypeVar("T", bound="GetAnEventResponse200Data")


@_attrs_define
class GetAnEventResponse200Data:
    """
    Attributes:
        id (int):
        slug (None | str):
        name (None | str):
        name_i18n (GetAnEventResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetAnEventResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        type_ (None | str): convention or store_event.
        start_date (None | str):
        end_date (None | str):
        start_time (None | str):
        end_time (None | str):
        timezone (None | str):
        is_online (bool):
        is_fcbd (bool):
        status (str): scheduled, cancelled, postponed or moved_online.
        venue_name (None | str):
        street_address (None | str):
        city (None | str):
        region (None | str):
        postal_code (None | str):
        country_code (None | str):
        latitude (None | str):
        longitude (None | str):
        full_location (str): `Online Event` for an online event, `Location TBA` when nothing is known.
        google_maps_url (None | str):
        logo_url (None | str):
        images (GetAnEventResponse200DataImagesType0 | None):
        event_url (None | str):
        ticket_price_min (int | None):
        ticket_price_max (int | None):
        ticket_currency (None | str):
        ticket_price (None | str):
        follower_count (int):
        event_franchise_id (int | None):
        creators (list[GetAnEventResponse200DataCreatorsItem]):
        issues (list[GetAnEventResponse200DataIssuesItem]):
        issue_variants (list[GetAnEventResponse200DataIssueVariantsItem]):
        attendees_preview (GetAnEventResponse200DataAttendeesPreview):
        related_events (list[GetAnEventResponse200DataRelatedEventsItem]):
        static_map_url (None | str | Unset): Left out for an online event.
        store (GetAnEventResponse200DataStore | Unset): The hosting shop, for a store event; null fields once the shop
            is gone.
    """

    id: int
    slug: None | str
    name: None | str
    name_i18n: GetAnEventResponse200DataNameI18N
    aliases_i18n: GetAnEventResponse200DataAliasesI18N
    original_locale: None | str
    type_: None | str
    start_date: None | str
    end_date: None | str
    start_time: None | str
    end_time: None | str
    timezone: None | str
    is_online: bool
    is_fcbd: bool
    status: str
    venue_name: None | str
    street_address: None | str
    city: None | str
    region: None | str
    postal_code: None | str
    country_code: None | str
    latitude: None | str
    longitude: None | str
    full_location: str
    google_maps_url: None | str
    logo_url: None | str
    images: GetAnEventResponse200DataImagesType0 | None
    event_url: None | str
    ticket_price_min: int | None
    ticket_price_max: int | None
    ticket_currency: None | str
    ticket_price: None | str
    follower_count: int
    event_franchise_id: int | None
    creators: list[GetAnEventResponse200DataCreatorsItem]
    issues: list[GetAnEventResponse200DataIssuesItem]
    issue_variants: list[GetAnEventResponse200DataIssueVariantsItem]
    attendees_preview: GetAnEventResponse200DataAttendeesPreview
    related_events: list[GetAnEventResponse200DataRelatedEventsItem]
    static_map_url: None | str | Unset = UNSET
    store: GetAnEventResponse200DataStore | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_an_event_response_200_data_images_type_0 import GetAnEventResponse200DataImagesType0  # noqa: PLC0415

        id = self.id

        slug: None | str
        slug = self.slug

        name: None | str
        name = self.name

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        type_: None | str
        type_ = self.type_

        start_date: None | str
        start_date = self.start_date

        end_date: None | str
        end_date = self.end_date

        start_time: None | str
        start_time = self.start_time

        end_time: None | str
        end_time = self.end_time

        timezone: None | str
        timezone = self.timezone

        is_online = self.is_online

        is_fcbd = self.is_fcbd

        status = self.status

        venue_name: None | str
        venue_name = self.venue_name

        street_address: None | str
        street_address = self.street_address

        city: None | str
        city = self.city

        region: None | str
        region = self.region

        postal_code: None | str
        postal_code = self.postal_code

        country_code: None | str
        country_code = self.country_code

        latitude: None | str
        latitude = self.latitude

        longitude: None | str
        longitude = self.longitude

        full_location = self.full_location

        google_maps_url: None | str
        google_maps_url = self.google_maps_url

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetAnEventResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        event_url: None | str
        event_url = self.event_url

        ticket_price_min: int | None
        ticket_price_min = self.ticket_price_min

        ticket_price_max: int | None
        ticket_price_max = self.ticket_price_max

        ticket_currency: None | str
        ticket_currency = self.ticket_currency

        ticket_price: None | str
        ticket_price = self.ticket_price

        follower_count = self.follower_count

        event_franchise_id: int | None
        event_franchise_id = self.event_franchise_id

        creators = []
        for creators_item_data in self.creators:
            creators_item = creators_item_data.to_dict()
            creators.append(creators_item)

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        issue_variants = []
        for issue_variants_item_data in self.issue_variants:
            issue_variants_item = issue_variants_item_data.to_dict()
            issue_variants.append(issue_variants_item)

        attendees_preview = self.attendees_preview.to_dict()

        related_events = []
        for related_events_item_data in self.related_events:
            related_events_item = related_events_item_data.to_dict()
            related_events.append(related_events_item)

        static_map_url: None | str | Unset
        if isinstance(self.static_map_url, Unset):
            static_map_url = UNSET
        else:
            static_map_url = self.static_map_url

        store: dict[str, Any] | Unset = UNSET
        if not isinstance(self.store, Unset):
            store = self.store.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "type": type_,
                "start_date": start_date,
                "end_date": end_date,
                "start_time": start_time,
                "end_time": end_time,
                "timezone": timezone,
                "is_online": is_online,
                "is_fcbd": is_fcbd,
                "status": status,
                "venue_name": venue_name,
                "street_address": street_address,
                "city": city,
                "region": region,
                "postal_code": postal_code,
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "full_location": full_location,
                "google_maps_url": google_maps_url,
                "logo_url": logo_url,
                "images": images,
                "event_url": event_url,
                "ticket_price_min": ticket_price_min,
                "ticket_price_max": ticket_price_max,
                "ticket_currency": ticket_currency,
                "ticket_price": ticket_price,
                "follower_count": follower_count,
                "event_franchise_id": event_franchise_id,
                "creators": creators,
                "issues": issues,
                "issue_variants": issue_variants,
                "attendees_preview": attendees_preview,
                "related_events": related_events,
            }
        )
        if static_map_url is not UNSET:
            field_dict["static_map_url"] = static_map_url
        if store is not UNSET:
            field_dict["store"] = store

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_an_event_response_200_data_aliases_i18n import GetAnEventResponse200DataAliasesI18N  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_attendees_preview import GetAnEventResponse200DataAttendeesPreview  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_creators_item import GetAnEventResponse200DataCreatorsItem  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_images_type_0 import GetAnEventResponse200DataImagesType0  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_issue_variants_item import (
            GetAnEventResponse200DataIssueVariantsItem,  # noqa: PLC0415
        )
        from ..models.get_an_event_response_200_data_issues_item import GetAnEventResponse200DataIssuesItem  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_name_i18n import GetAnEventResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_an_event_response_200_data_related_events_item import (
            GetAnEventResponse200DataRelatedEventsItem,  # noqa: PLC0415
        )
        from ..models.get_an_event_response_200_data_store import GetAnEventResponse200DataStore  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_i18n = GetAnEventResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetAnEventResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_start_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("end_date"))

        def _parse_start_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start_time = _parse_start_time(d.pop("start_time"))

        def _parse_end_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_time = _parse_end_time(d.pop("end_time"))

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        is_online = d.pop("is_online")

        is_fcbd = d.pop("is_fcbd")

        status = d.pop("status")

        def _parse_venue_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        venue_name = _parse_venue_name(d.pop("venue_name"))

        def _parse_street_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        street_address = _parse_street_address(d.pop("street_address"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postal_code"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        def _parse_latitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        longitude = _parse_longitude(d.pop("longitude"))

        full_location = d.pop("full_location")

        def _parse_google_maps_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        google_maps_url = _parse_google_maps_url(d.pop("google_maps_url"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> GetAnEventResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetAnEventResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAnEventResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_event_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_url = _parse_event_url(d.pop("event_url"))

        def _parse_ticket_price_min(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ticket_price_min = _parse_ticket_price_min(d.pop("ticket_price_min"))

        def _parse_ticket_price_max(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ticket_price_max = _parse_ticket_price_max(d.pop("ticket_price_max"))

        def _parse_ticket_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ticket_currency = _parse_ticket_currency(d.pop("ticket_currency"))

        def _parse_ticket_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ticket_price = _parse_ticket_price(d.pop("ticket_price"))

        follower_count = d.pop("follower_count")

        def _parse_event_franchise_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        event_franchise_id = _parse_event_franchise_id(d.pop("event_franchise_id"))

        creators = []
        _creators = d.pop("creators")
        for creators_item_data in _creators:
            creators_item = GetAnEventResponse200DataCreatorsItem.from_dict(creators_item_data)

            creators.append(creators_item)

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = GetAnEventResponse200DataIssuesItem.from_dict(issues_item_data)

            issues.append(issues_item)

        issue_variants = []
        _issue_variants = d.pop("issue_variants")
        for issue_variants_item_data in _issue_variants:
            issue_variants_item = GetAnEventResponse200DataIssueVariantsItem.from_dict(issue_variants_item_data)

            issue_variants.append(issue_variants_item)

        attendees_preview = GetAnEventResponse200DataAttendeesPreview.from_dict(d.pop("attendees_preview"))

        related_events = []
        _related_events = d.pop("related_events")
        for related_events_item_data in _related_events:
            related_events_item = GetAnEventResponse200DataRelatedEventsItem.from_dict(related_events_item_data)

            related_events.append(related_events_item)

        def _parse_static_map_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        static_map_url = _parse_static_map_url(d.pop("static_map_url", UNSET))

        _store = d.pop("store", UNSET)
        store: GetAnEventResponse200DataStore | Unset
        if isinstance(_store, Unset):
            store = UNSET
        else:
            store = GetAnEventResponse200DataStore.from_dict(_store)

        get_an_event_response_200_data = cls(
            id=id,
            slug=slug,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            type_=type_,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            timezone=timezone,
            is_online=is_online,
            is_fcbd=is_fcbd,
            status=status,
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
            static_map_url=static_map_url,
            store=store,
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
