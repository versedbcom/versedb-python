from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_series_creators_response_200_data_item_role import GetSeriesCreatorsResponse200DataItemRole


T = TypeVar("T", bound="GetSeriesCreatorsResponse200DataItem")


@_attrs_define
class GetSeriesCreatorsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        role (GetSeriesCreatorsResponse200DataItemRole | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    role: GetSeriesCreatorsResponse200DataItemRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_creators_response_200_data_item_role import GetSeriesCreatorsResponse200DataItemRole  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _role = d.pop("role", UNSET)
        role: GetSeriesCreatorsResponse200DataItemRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = GetSeriesCreatorsResponse200DataItemRole.from_dict(_role)

        get_series_creators_response_200_data_item = cls(
            id=id,
            name=name,
            role=role,
        )

        get_series_creators_response_200_data_item.additional_properties = d
        return get_series_creators_response_200_data_item

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
