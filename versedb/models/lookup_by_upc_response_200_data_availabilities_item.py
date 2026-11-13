from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupByUpcResponse200DataAvailabilitiesItem")


@_attrs_define
class LookupByUpcResponse200DataAvailabilitiesItem:
    """
    Attributes:
        id (int | None):
        provider (str):
        provider_label (str):
        kind (str): buy, read or watch.
        store_name (None | str):
        custom_name (None | str):
        display_name (str):
        store_logo (None | str):
        url (str):
        external_id (None | str):
        price (float | None):
        formatted_price (None | str):
        currency (None | str):
        is_digital (bool | None):
        is_affiliate (bool):
        is_synthesized (bool):
        verified_at (None | str):
    """

    id: int | None
    provider: str
    provider_label: str
    kind: str
    store_name: None | str
    custom_name: None | str
    display_name: str
    store_logo: None | str
    url: str
    external_id: None | str
    price: float | None
    formatted_price: None | str
    currency: None | str
    is_digital: bool | None
    is_affiliate: bool
    is_synthesized: bool
    verified_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None
        id = self.id

        provider = self.provider

        provider_label = self.provider_label

        kind = self.kind

        store_name: None | str
        store_name = self.store_name

        custom_name: None | str
        custom_name = self.custom_name

        display_name = self.display_name

        store_logo: None | str
        store_logo = self.store_logo

        url = self.url

        external_id: None | str
        external_id = self.external_id

        price: float | None
        price = self.price

        formatted_price: None | str
        formatted_price = self.formatted_price

        currency: None | str
        currency = self.currency

        is_digital: bool | None
        is_digital = self.is_digital

        is_affiliate = self.is_affiliate

        is_synthesized = self.is_synthesized

        verified_at: None | str
        verified_at = self.verified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "provider": provider,
                "provider_label": provider_label,
                "kind": kind,
                "store_name": store_name,
                "custom_name": custom_name,
                "display_name": display_name,
                "store_logo": store_logo,
                "url": url,
                "external_id": external_id,
                "price": price,
                "formatted_price": formatted_price,
                "currency": currency,
                "is_digital": is_digital,
                "is_affiliate": is_affiliate,
                "is_synthesized": is_synthesized,
                "verified_at": verified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        id = _parse_id(d.pop("id"))

        provider = d.pop("provider")

        provider_label = d.pop("provider_label")

        kind = d.pop("kind")

        def _parse_store_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        store_name = _parse_store_name(d.pop("store_name"))

        def _parse_custom_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        custom_name = _parse_custom_name(d.pop("custom_name"))

        display_name = d.pop("display_name")

        def _parse_store_logo(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        store_logo = _parse_store_logo(d.pop("store_logo"))

        url = d.pop("url")

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("external_id"))

        def _parse_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price = _parse_price(d.pop("price"))

        def _parse_formatted_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formatted_price = _parse_formatted_price(d.pop("formatted_price"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_is_digital(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_digital = _parse_is_digital(d.pop("is_digital"))

        is_affiliate = d.pop("is_affiliate")

        is_synthesized = d.pop("is_synthesized")

        def _parse_verified_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verified_at = _parse_verified_at(d.pop("verified_at"))

        lookup_by_upc_response_200_data_availabilities_item = cls(
            id=id,
            provider=provider,
            provider_label=provider_label,
            kind=kind,
            store_name=store_name,
            custom_name=custom_name,
            display_name=display_name,
            store_logo=store_logo,
            url=url,
            external_id=external_id,
            price=price,
            formatted_price=formatted_price,
            currency=currency,
            is_digital=is_digital,
            is_affiliate=is_affiliate,
            is_synthesized=is_synthesized,
            verified_at=verified_at,
        )

        lookup_by_upc_response_200_data_availabilities_item.additional_properties = d
        return lookup_by_upc_response_200_data_availabilities_item

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
