from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeAConnectCodeForATokenResponse200")


@_attrs_define
class ExchangeAConnectCodeForATokenResponse200:
    """
    Attributes:
        access_token (str | Unset):
        token_type (str | Unset):
        expires_at (str | Unset):
        abilities (list[str] | Unset):
    """

    access_token: str | Unset = UNSET
    token_type: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    abilities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        expires_at = self.expires_at

        abilities: list[str] | Unset = UNSET
        if not isinstance(self.abilities, Unset):
            abilities = self.abilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if abilities is not UNSET:
            field_dict["abilities"] = abilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        abilities = cast(list[str], d.pop("abilities", UNSET))

        exchange_a_connect_code_for_a_token_response_200 = cls(
            access_token=access_token,
            token_type=token_type,
            expires_at=expires_at,
            abilities=abilities,
        )

        exchange_a_connect_code_for_a_token_response_200.additional_properties = d
        return exchange_a_connect_code_for_a_token_response_200

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
