from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_events_response_200_data_item_aliases_i18n import ListEventsResponse200DataItemAliasesI18N
    from ..models.list_events_response_200_data_item_images_type_0 import ListEventsResponse200DataItemImagesType0
    from ..models.list_events_response_200_data_item_name_i18n import ListEventsResponse200DataItemNameI18N


T = TypeVar("T", bound="ListEventsResponse200DataItem")


@_attrs_define
class ListEventsResponse200DataItem:
    """
    Attributes:
        id (int):
        slug (None | str):
        name (None | str):
        name_i18n (ListEventsResponse200DataItemNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (ListEventsResponse200DataItemAliasesI18N): Alternative names per language.
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
        city (None | str):
        region (None | str):
        country_code (None | str):
        full_location (str): `Online Event` for an online event, `Location TBA` when nothing is known.
        logo_url (None | str):
        images (ListEventsResponse200DataItemImagesType0 | None):
        ticket_price (None | str):
        follower_count (int):
    """

    id: int
    slug: None | str
    name: None | str
    name_i18n: ListEventsResponse200DataItemNameI18N
    aliases_i18n: ListEventsResponse200DataItemAliasesI18N
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
    city: None | str
    region: None | str
    country_code: None | str
    full_location: str
    logo_url: None | str
    images: ListEventsResponse200DataItemImagesType0 | None
    ticket_price: None | str
    follower_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_events_response_200_data_item_images_type_0 import ListEventsResponse200DataItemImagesType0  # noqa: PLC0415

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

        city: None | str
        city = self.city

        region: None | str
        region = self.region

        country_code: None | str
        country_code = self.country_code

        full_location = self.full_location

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, ListEventsResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        ticket_price: None | str
        ticket_price = self.ticket_price

        follower_count = self.follower_count

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
                "city": city,
                "region": region,
                "country_code": country_code,
                "full_location": full_location,
                "logo_url": logo_url,
                "images": images,
                "ticket_price": ticket_price,
                "follower_count": follower_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_events_response_200_data_item_aliases_i18n import ListEventsResponse200DataItemAliasesI18N  # noqa: PLC0415
        from ..models.list_events_response_200_data_item_images_type_0 import ListEventsResponse200DataItemImagesType0  # noqa: PLC0415
        from ..models.list_events_response_200_data_item_name_i18n import ListEventsResponse200DataItemNameI18N  # noqa: PLC0415

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

        name_i18n = ListEventsResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = ListEventsResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

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

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        full_location = d.pop("full_location")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> ListEventsResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = ListEventsResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListEventsResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_ticket_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ticket_price = _parse_ticket_price(d.pop("ticket_price"))

        follower_count = d.pop("follower_count")

        list_events_response_200_data_item = cls(
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
