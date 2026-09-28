from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowContentBodyPreferencesType0")


@_attrs_define
class FollowContentBodyPreferencesType0:
    """Notification preferences.

    Attributes:
        email_notifications (bool | Unset): Receive email notifications.
        push_notifications (bool | Unset): Receive push notifications.
    """

    email_notifications: bool | Unset = UNSET
    push_notifications: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_notifications = self.email_notifications

        push_notifications = self.push_notifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if push_notifications is not UNSET:
            field_dict["push_notifications"] = push_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_notifications = d.pop("email_notifications", UNSET)

        push_notifications = d.pop("push_notifications", UNSET)

        follow_content_body_preferences_type_0 = cls(
            email_notifications=email_notifications,
            push_notifications=push_notifications,
        )

        follow_content_body_preferences_type_0.additional_properties = d
        return follow_content_body_preferences_type_0

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
