from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_follows_response_200_data_item_followable_type_0 import (
        ListFollowsResponse200DataItemFollowableType0,
    )
    from ..models.list_follows_response_200_data_item_preferences_type_4 import (
        ListFollowsResponse200DataItemPreferencesType4,
    )


T = TypeVar("T", bound="ListFollowsResponse200DataItem")


@_attrs_define
class ListFollowsResponse200DataItem:
    """
    Attributes:
        id (int):
        user_id (int):
        followable_type (str): The morph alias of the followed entity.
        followable_id (int):
        preferences (bool | float | list[Any] | ListFollowsResponse200DataItemPreferencesType4 | None | str): The
            notification preferences given with the follow.
        created_at (None | str):
        updated_at (None | str):
        followable (ListFollowsResponse200DataItemFollowableType0 | None): The followed entity, or null when it is gone.
    """

    id: int
    user_id: int
    followable_type: str
    followable_id: int
    preferences: bool | float | list[Any] | ListFollowsResponse200DataItemPreferencesType4 | None | str
    created_at: None | str
    updated_at: None | str
    followable: ListFollowsResponse200DataItemFollowableType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_follows_response_200_data_item_followable_type_0 import (
            ListFollowsResponse200DataItemFollowableType0,  # noqa: PLC0415
        )
        from ..models.list_follows_response_200_data_item_preferences_type_4 import (
            ListFollowsResponse200DataItemPreferencesType4,  # noqa: PLC0415
        )

        id = self.id

        user_id = self.user_id

        followable_type = self.followable_type

        followable_id = self.followable_id

        preferences: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.preferences, list):
            preferences = self.preferences

        elif isinstance(self.preferences, ListFollowsResponse200DataItemPreferencesType4):
            preferences = self.preferences.to_dict()
        else:
            preferences = self.preferences

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        followable: dict[str, Any] | None
        if isinstance(self.followable, ListFollowsResponse200DataItemFollowableType0):
            followable = self.followable.to_dict()
        else:
            followable = self.followable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "followable_type": followable_type,
                "followable_id": followable_id,
                "preferences": preferences,
                "created_at": created_at,
                "updated_at": updated_at,
                "followable": followable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_follows_response_200_data_item_followable_type_0 import (
            ListFollowsResponse200DataItemFollowableType0,  # noqa: PLC0415
        )
        from ..models.list_follows_response_200_data_item_preferences_type_4 import (
            ListFollowsResponse200DataItemPreferencesType4,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        followable_type = d.pop("followable_type")

        followable_id = d.pop("followable_id")

        def _parse_preferences(
            data: object,
        ) -> bool | float | list[Any] | ListFollowsResponse200DataItemPreferencesType4 | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                preferences_type_3 = cast(list[Any], data)

                return preferences_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preferences_type_4 = ListFollowsResponse200DataItemPreferencesType4.from_dict(data)

                return preferences_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | list[Any] | ListFollowsResponse200DataItemPreferencesType4 | None | str, data)

        preferences = _parse_preferences(d.pop("preferences"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_followable(data: object) -> ListFollowsResponse200DataItemFollowableType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                followable_type_0 = ListFollowsResponse200DataItemFollowableType0.from_dict(data)

                return followable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListFollowsResponse200DataItemFollowableType0 | None, data)

        followable = _parse_followable(d.pop("followable"))

        list_follows_response_200_data_item = cls(
            id=id,
            user_id=user_id,
            followable_type=followable_type,
            followable_id=followable_id,
            preferences=preferences,
            created_at=created_at,
            updated_at=updated_at,
            followable=followable,
        )

        list_follows_response_200_data_item.additional_properties = d
        return list_follows_response_200_data_item

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
