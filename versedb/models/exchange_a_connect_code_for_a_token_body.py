from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangeAConnectCodeForATokenBody")


@_attrs_define
class ExchangeAConnectCodeForATokenBody:
    """
    Attributes:
        grant_type (str): Must be `authorization_code`.
        code (str): The code from the redirect.
        redirect_uri (str): Exactly the redirect_uri sent to /connect.
        code_verifier (str): The verifier the code_challenge was made from.
    """

    grant_type: str
    code: str
    redirect_uri: str
    code_verifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        code = self.code

        redirect_uri = self.redirect_uri

        code_verifier = self.code_verifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = d.pop("grant_type")

        code = d.pop("code")

        redirect_uri = d.pop("redirect_uri")

        code_verifier = d.pop("code_verifier")

        exchange_a_connect_code_for_a_token_body = cls(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
        )

        exchange_a_connect_code_for_a_token_body.additional_properties = d
        return exchange_a_connect_code_for_a_token_body

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
