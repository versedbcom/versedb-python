from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.follow_updates_response_200_follow_types_type_0_additional_property import (
    FollowUpdatesResponse200FollowTypesType0AdditionalProperty,
    check_follow_updates_response_200_follow_types_type_0_additional_property,
)

T = TypeVar("T", bound="FollowUpdatesResponse200FollowTypesType0")


@_attrs_define
class FollowUpdatesResponse200FollowTypesType0:
    additional_properties: dict[str, FollowUpdatesResponse200FollowTypesType0AdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follow_updates_response_200_follow_types_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = check_follow_updates_response_200_follow_types_type_0_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        follow_updates_response_200_follow_types_type_0.additional_properties = additional_properties
        return follow_updates_response_200_follow_types_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FollowUpdatesResponse200FollowTypesType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FollowUpdatesResponse200FollowTypesType0AdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
