from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_a_comic_shop_response_200_data_aliases_i18n import GetAComicShopResponse200DataAliasesI18N
    from ..models.get_a_comic_shop_response_200_data_events_item import GetAComicShopResponse200DataEventsItem
    from ..models.get_a_comic_shop_response_200_data_images_type_0 import GetAComicShopResponse200DataImagesType0
    from ..models.get_a_comic_shop_response_200_data_name_i18n import GetAComicShopResponse200DataNameI18N
    from ..models.get_a_comic_shop_response_200_data_operating_hours_type_0 import (
        GetAComicShopResponse200DataOperatingHoursType0,
    )
    from ..models.get_a_comic_shop_response_200_data_related_shops_item import (
        GetAComicShopResponse200DataRelatedShopsItem,
    )
    from ..models.get_a_comic_shop_response_200_data_special_hours_item import (
        GetAComicShopResponse200DataSpecialHoursItem,
    )


T = TypeVar("T", bound="GetAComicShopResponse200Data")


@_attrs_define
class GetAComicShopResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        name_i18n (GetAComicShopResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetAComicShopResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the entity is from, a BCP 47 tag.
        address (None | str):
        city (None | str):
        state_province (None | str):
        postal_code (None | str):
        country (None | str):
        country_code (None | str):
        website (None | str):
        full_address (str):
        logo_url (None | str):
        images (GetAComicShopResponse200DataImagesType0 | None):
        operating_hours (GetAComicShopResponse200DataOperatingHoursType0 | list[Any] | None): Monday first, by lowercase
            day name; `closed` or 24-hour ranges joined by commas. A missing day has unknown hours.
        special_hours (list[GetAComicShopResponse200DataSpecialHoursItem]): Dated exceptions that have not ended, by
            start date.
        related_shops (list[GetAComicShopResponse200DataRelatedShopsItem]):
        services (list[str]):
        events (list[GetAComicShopResponse200DataEventsItem]):
    """

    id: int
    name: None | str
    name_i18n: GetAComicShopResponse200DataNameI18N
    aliases_i18n: GetAComicShopResponse200DataAliasesI18N
    original_locale: None | str
    address: None | str
    city: None | str
    state_province: None | str
    postal_code: None | str
    country: None | str
    country_code: None | str
    website: None | str
    full_address: str
    logo_url: None | str
    images: GetAComicShopResponse200DataImagesType0 | None
    operating_hours: GetAComicShopResponse200DataOperatingHoursType0 | list[Any] | None
    special_hours: list[GetAComicShopResponse200DataSpecialHoursItem]
    related_shops: list[GetAComicShopResponse200DataRelatedShopsItem]
    services: list[str]
    events: list[GetAComicShopResponse200DataEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_a_comic_shop_response_200_data_images_type_0 import GetAComicShopResponse200DataImagesType0  # noqa: PLC0415
        from ..models.get_a_comic_shop_response_200_data_operating_hours_type_0 import (
            GetAComicShopResponse200DataOperatingHoursType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        address: None | str
        address = self.address

        city: None | str
        city = self.city

        state_province: None | str
        state_province = self.state_province

        postal_code: None | str
        postal_code = self.postal_code

        country: None | str
        country = self.country

        country_code: None | str
        country_code = self.country_code

        website: None | str
        website = self.website

        full_address = self.full_address

        logo_url: None | str
        logo_url = self.logo_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetAComicShopResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        operating_hours: dict[str, Any] | list[Any] | None
        if isinstance(self.operating_hours, GetAComicShopResponse200DataOperatingHoursType0):
            operating_hours = self.operating_hours.to_dict()
        elif isinstance(self.operating_hours, list):
            operating_hours = self.operating_hours

        else:
            operating_hours = self.operating_hours

        special_hours = []
        for special_hours_item_data in self.special_hours:
            special_hours_item = special_hours_item_data.to_dict()
            special_hours.append(special_hours_item)

        related_shops = []
        for related_shops_item_data in self.related_shops:
            related_shops_item = related_shops_item_data.to_dict()
            related_shops.append(related_shops_item)

        services = self.services

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
                "address": address,
                "city": city,
                "state_province": state_province,
                "postal_code": postal_code,
                "country": country,
                "country_code": country_code,
                "website": website,
                "full_address": full_address,
                "logo_url": logo_url,
                "images": images,
                "operating_hours": operating_hours,
                "special_hours": special_hours,
                "related_shops": related_shops,
                "services": services,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_a_comic_shop_response_200_data_aliases_i18n import GetAComicShopResponse200DataAliasesI18N  # noqa: PLC0415
        from ..models.get_a_comic_shop_response_200_data_events_item import GetAComicShopResponse200DataEventsItem  # noqa: PLC0415
        from ..models.get_a_comic_shop_response_200_data_images_type_0 import GetAComicShopResponse200DataImagesType0  # noqa: PLC0415
        from ..models.get_a_comic_shop_response_200_data_name_i18n import GetAComicShopResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_a_comic_shop_response_200_data_operating_hours_type_0 import (
            GetAComicShopResponse200DataOperatingHoursType0,  # noqa: PLC0415
        )
        from ..models.get_a_comic_shop_response_200_data_related_shops_item import (
            GetAComicShopResponse200DataRelatedShopsItem,  # noqa: PLC0415
        )
        from ..models.get_a_comic_shop_response_200_data_special_hours_item import (
            GetAComicShopResponse200DataSpecialHoursItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_i18n = GetAComicShopResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetAComicShopResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state_province(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_province = _parse_state_province(d.pop("state_province"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postal_code"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        full_address = d.pop("full_address")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_images(data: object) -> GetAComicShopResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetAComicShopResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAComicShopResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_operating_hours(data: object) -> GetAComicShopResponse200DataOperatingHoursType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operating_hours_type_0 = GetAComicShopResponse200DataOperatingHoursType0.from_dict(data)

                return operating_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operating_hours_type_1 = cast(list[Any], data)

                return operating_hours_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAComicShopResponse200DataOperatingHoursType0 | list[Any] | None, data)

        operating_hours = _parse_operating_hours(d.pop("operating_hours"))

        special_hours = []
        _special_hours = d.pop("special_hours")
        for special_hours_item_data in _special_hours:
            special_hours_item = GetAComicShopResponse200DataSpecialHoursItem.from_dict(special_hours_item_data)

            special_hours.append(special_hours_item)

        related_shops = []
        _related_shops = d.pop("related_shops")
        for related_shops_item_data in _related_shops:
            related_shops_item = GetAComicShopResponse200DataRelatedShopsItem.from_dict(related_shops_item_data)

            related_shops.append(related_shops_item)

        services = cast(list[str], d.pop("services"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = GetAComicShopResponse200DataEventsItem.from_dict(events_item_data)

            events.append(events_item)

        get_a_comic_shop_response_200_data = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            address=address,
            city=city,
            state_province=state_province,
            postal_code=postal_code,
            country=country,
            country_code=country_code,
            website=website,
            full_address=full_address,
            logo_url=logo_url,
            images=images,
            operating_hours=operating_hours,
            special_hours=special_hours,
            related_shops=related_shops,
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
