from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.follow_updates_response_200_data_item import FollowUpdatesResponse200DataItem
    from ..models.follow_updates_response_200_follow_contexts_type_0 import FollowUpdatesResponse200FollowContextsType0
    from ..models.follow_updates_response_200_follow_types_type_0 import FollowUpdatesResponse200FollowTypesType0
    from ..models.follow_updates_response_200_meta import FollowUpdatesResponse200Meta


T = TypeVar("T", bound="FollowUpdatesResponse200")


@_attrs_define
class FollowUpdatesResponse200:
    """
    Attributes:
        data (list[FollowUpdatesResponse200DataItem]):
        meta (FollowUpdatesResponse200Meta):
        follow_contexts (FollowUpdatesResponse200FollowContextsType0 | list[Any] | Unset):
        follow_types (FollowUpdatesResponse200FollowTypesType0 | list[Any] | Unset):
    """

    data: list[FollowUpdatesResponse200DataItem]
    meta: FollowUpdatesResponse200Meta
    follow_contexts: FollowUpdatesResponse200FollowContextsType0 | list[Any] | Unset = UNSET
    follow_types: FollowUpdatesResponse200FollowTypesType0 | list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.follow_updates_response_200_follow_contexts_type_0 import (
            FollowUpdatesResponse200FollowContextsType0,  # noqa: PLC0415
        )
        from ..models.follow_updates_response_200_follow_types_type_0 import FollowUpdatesResponse200FollowTypesType0  # noqa: PLC0415

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        follow_contexts: dict[str, Any] | list[Any] | Unset
        if isinstance(self.follow_contexts, Unset):
            follow_contexts = UNSET
        elif isinstance(self.follow_contexts, FollowUpdatesResponse200FollowContextsType0):
            follow_contexts = self.follow_contexts.to_dict()
        else:
            follow_contexts = self.follow_contexts

        follow_types: dict[str, Any] | list[Any] | Unset
        if isinstance(self.follow_types, Unset):
            follow_types = UNSET
        elif isinstance(self.follow_types, FollowUpdatesResponse200FollowTypesType0):
            follow_types = self.follow_types.to_dict()
        else:
            follow_types = self.follow_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )
        if follow_contexts is not UNSET:
            field_dict["follow_contexts"] = follow_contexts
        if follow_types is not UNSET:
            field_dict["follow_types"] = follow_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follow_updates_response_200_data_item import FollowUpdatesResponse200DataItem  # noqa: PLC0415
        from ..models.follow_updates_response_200_follow_contexts_type_0 import (
            FollowUpdatesResponse200FollowContextsType0,  # noqa: PLC0415
        )
        from ..models.follow_updates_response_200_follow_types_type_0 import FollowUpdatesResponse200FollowTypesType0  # noqa: PLC0415
        from ..models.follow_updates_response_200_meta import FollowUpdatesResponse200Meta  # noqa: PLC0415

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = FollowUpdatesResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        meta = FollowUpdatesResponse200Meta.from_dict(d.pop("meta"))

        def _parse_follow_contexts(data: object) -> FollowUpdatesResponse200FollowContextsType0 | list[Any] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                follow_contexts_type_0 = FollowUpdatesResponse200FollowContextsType0.from_dict(data)

                return follow_contexts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            follow_contexts_type_1 = cast(list[Any], data)

            return follow_contexts_type_1

        follow_contexts = _parse_follow_contexts(d.pop("follow_contexts", UNSET))

        def _parse_follow_types(data: object) -> FollowUpdatesResponse200FollowTypesType0 | list[Any] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                follow_types_type_0 = FollowUpdatesResponse200FollowTypesType0.from_dict(data)

                return follow_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            follow_types_type_1 = cast(list[Any], data)

            return follow_types_type_1

        follow_types = _parse_follow_types(d.pop("follow_types", UNSET))

        follow_updates_response_200 = cls(
            data=data,
            meta=meta,
            follow_contexts=follow_contexts,
            follow_types=follow_types,
        )

        follow_updates_response_200.additional_properties = d
        return follow_updates_response_200

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
