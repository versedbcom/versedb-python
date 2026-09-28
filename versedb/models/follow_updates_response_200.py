from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.follow_updates_response_200_data_item import FollowUpdatesResponse200DataItem
    from ..models.follow_updates_response_200_follow_contexts import FollowUpdatesResponse200FollowContexts
    from ..models.follow_updates_response_200_follow_types import FollowUpdatesResponse200FollowTypes
    from ..models.follow_updates_response_200_meta import FollowUpdatesResponse200Meta


T = TypeVar("T", bound="FollowUpdatesResponse200")


@_attrs_define
class FollowUpdatesResponse200:
    """
    Attributes:
        data (list[FollowUpdatesResponse200DataItem] | Unset):
        follow_contexts (FollowUpdatesResponse200FollowContexts | Unset):
        follow_types (FollowUpdatesResponse200FollowTypes | Unset):
        meta (FollowUpdatesResponse200Meta | Unset):
    """

    data: list[FollowUpdatesResponse200DataItem] | Unset = UNSET
    follow_contexts: FollowUpdatesResponse200FollowContexts | Unset = UNSET
    follow_types: FollowUpdatesResponse200FollowTypes | Unset = UNSET
    meta: FollowUpdatesResponse200Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        follow_contexts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_contexts, Unset):
            follow_contexts = self.follow_contexts.to_dict()

        follow_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_types, Unset):
            follow_types = self.follow_types.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if follow_contexts is not UNSET:
            field_dict["follow_contexts"] = follow_contexts
        if follow_types is not UNSET:
            field_dict["follow_types"] = follow_types
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follow_updates_response_200_data_item import FollowUpdatesResponse200DataItem  # noqa: PLC0415
        from ..models.follow_updates_response_200_follow_contexts import (
            FollowUpdatesResponse200FollowContexts,  # noqa: PLC0415
        )
        from ..models.follow_updates_response_200_follow_types import (
            FollowUpdatesResponse200FollowTypes,  # noqa: PLC0415
        )
        from ..models.follow_updates_response_200_meta import FollowUpdatesResponse200Meta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[FollowUpdatesResponse200DataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = FollowUpdatesResponse200DataItem.from_dict(data_item_data)

                data.append(data_item)

        _follow_contexts = d.pop("follow_contexts", UNSET)
        follow_contexts: FollowUpdatesResponse200FollowContexts | Unset
        if isinstance(_follow_contexts, Unset):
            follow_contexts = UNSET
        else:
            follow_contexts = FollowUpdatesResponse200FollowContexts.from_dict(_follow_contexts)

        _follow_types = d.pop("follow_types", UNSET)
        follow_types: FollowUpdatesResponse200FollowTypes | Unset
        if isinstance(_follow_types, Unset):
            follow_types = UNSET
        else:
            follow_types = FollowUpdatesResponse200FollowTypes.from_dict(_follow_types)

        _meta = d.pop("meta", UNSET)
        meta: FollowUpdatesResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FollowUpdatesResponse200Meta.from_dict(_meta)

        follow_updates_response_200 = cls(
            data=data,
            follow_contexts=follow_contexts,
            follow_types=follow_types,
            meta=meta,
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
