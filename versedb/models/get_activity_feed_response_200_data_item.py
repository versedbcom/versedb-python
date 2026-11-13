from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_activity_feed_response_200_data_item_action import (
    GetActivityFeedResponse200DataItemAction,
    check_get_activity_feed_response_200_data_item_action,
)
from ..models.get_activity_feed_response_200_data_item_type import (
    GetActivityFeedResponse200DataItemType,
    check_get_activity_feed_response_200_data_item_type,
)

if TYPE_CHECKING:
    from ..models.get_activity_feed_response_200_data_item_data_type_0 import (
        GetActivityFeedResponse200DataItemDataType0,
    )
    from ..models.get_activity_feed_response_200_data_item_data_type_1 import (
        GetActivityFeedResponse200DataItemDataType1,
    )
    from ..models.get_activity_feed_response_200_data_item_data_type_2 import (
        GetActivityFeedResponse200DataItemDataType2,
    )


T = TypeVar("T", bound="GetActivityFeedResponse200DataItem")


@_attrs_define
class GetActivityFeedResponse200DataItem:
    """
    Attributes:
        id (str): The source and its row id.
        type_ (GetActivityFeedResponse200DataItemType):
        action (GetActivityFeedResponse200DataItemAction):
        created_at (None | str):
        data (GetActivityFeedResponse200DataItemDataType0 | GetActivityFeedResponse200DataItemDataType1 |
            GetActivityFeedResponse200DataItemDataType2): The issue, review or followed entity the entry is about.
    """

    id: str
    type_: GetActivityFeedResponse200DataItemType
    action: GetActivityFeedResponse200DataItemAction
    created_at: None | str
    data: (
        GetActivityFeedResponse200DataItemDataType0
        | GetActivityFeedResponse200DataItemDataType1
        | GetActivityFeedResponse200DataItemDataType2
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_activity_feed_response_200_data_item_data_type_0 import (
            GetActivityFeedResponse200DataItemDataType0,  # noqa: PLC0415
        )
        from ..models.get_activity_feed_response_200_data_item_data_type_1 import (
            GetActivityFeedResponse200DataItemDataType1,  # noqa: PLC0415
        )

        id = self.id

        type_: str = self.type_

        action: str = self.action

        created_at: None | str
        created_at = self.created_at

        data: dict[str, Any]
        if isinstance(self.data, GetActivityFeedResponse200DataItemDataType0):
            data = self.data.to_dict()
        elif isinstance(self.data, GetActivityFeedResponse200DataItemDataType1):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "action": action,
                "created_at": created_at,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_feed_response_200_data_item_data_type_0 import (
            GetActivityFeedResponse200DataItemDataType0,  # noqa: PLC0415
        )
        from ..models.get_activity_feed_response_200_data_item_data_type_1 import (
            GetActivityFeedResponse200DataItemDataType1,  # noqa: PLC0415
        )
        from ..models.get_activity_feed_response_200_data_item_data_type_2 import (
            GetActivityFeedResponse200DataItemDataType2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_get_activity_feed_response_200_data_item_type(d.pop("type"))

        action = check_get_activity_feed_response_200_data_item_action(d.pop("action"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_data(
            data: object,
        ) -> (
            GetActivityFeedResponse200DataItemDataType0
            | GetActivityFeedResponse200DataItemDataType1
            | GetActivityFeedResponse200DataItemDataType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GetActivityFeedResponse200DataItemDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = GetActivityFeedResponse200DataItemDataType1.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_2 = GetActivityFeedResponse200DataItemDataType2.from_dict(data)

            return data_type_2

        data = _parse_data(d.pop("data"))

        get_activity_feed_response_200_data_item = cls(
            id=id,
            type_=type_,
            action=action,
            created_at=created_at,
            data=data,
        )

        get_activity_feed_response_200_data_item.additional_properties = d
        return get_activity_feed_response_200_data_item

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
