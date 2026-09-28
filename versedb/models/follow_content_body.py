from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.follow_content_body_preferences_type_0 import FollowContentBodyPreferencesType0


T = TypeVar("T", bound="FollowContentBody")


@_attrs_define
class FollowContentBody:
    """
    Attributes:
        type_ (str): The content type (title, character, podcast, creator, publisher, team, story_arc, comic_shop,
            event, event_franchise, user). An event_franchise is the recurring convention itself, so the follow covers every
            edition, including ones added later. Following an event that belongs to a franchise follows the franchise too,
            and unfollowing either clears both.
        id (int): The ID of the content to follow.
        preferences (FollowContentBodyPreferencesType0 | None | Unset): Notification preferences.
    """

    type_: str
    id: int
    preferences: FollowContentBodyPreferencesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.follow_content_body_preferences_type_0 import FollowContentBodyPreferencesType0  # noqa: PLC0415

        type_ = self.type_

        id = self.id

        preferences: dict[str, Any] | None | Unset
        if isinstance(self.preferences, Unset):
            preferences = UNSET
        elif isinstance(self.preferences, FollowContentBodyPreferencesType0):
            preferences = self.preferences.to_dict()
        else:
            preferences = self.preferences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follow_content_body_preferences_type_0 import FollowContentBodyPreferencesType0  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        def _parse_preferences(data: object) -> FollowContentBodyPreferencesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preferences_type_0 = FollowContentBodyPreferencesType0.from_dict(data)

                return preferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FollowContentBodyPreferencesType0 | None | Unset, data)

        preferences = _parse_preferences(d.pop("preferences", UNSET))

        follow_content_body = cls(
            type_=type_,
            id=id,
            preferences=preferences,
        )

        follow_content_body.additional_properties = d
        return follow_content_body

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
