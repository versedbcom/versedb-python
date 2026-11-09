from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_read_status_response_200_data_item_readable_type_0 import (
        ListReadStatusResponse200DataItemReadableType0,
    )


T = TypeVar("T", bound="ListReadStatusResponse200DataItem")


@_attrs_define
class ListReadStatusResponse200DataItem:
    """
    Attributes:
        id (int):
        user_id (int):
        readable_type (str):
        readable_id (int):
        variant_id (int | None):
        read_at (None | str):
        created_at (None | str):
        updated_at (None | str):
        readable (ListReadStatusResponse200DataItemReadableType0 | None): Null once the issue is gone.
    """

    id: int
    user_id: int
    readable_type: str
    readable_id: int
    variant_id: int | None
    read_at: None | str
    created_at: None | str
    updated_at: None | str
    readable: ListReadStatusResponse200DataItemReadableType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_read_status_response_200_data_item_readable_type_0 import (
            ListReadStatusResponse200DataItemReadableType0,  # noqa: PLC0415
        )

        id = self.id

        user_id = self.user_id

        readable_type = self.readable_type

        readable_id = self.readable_id

        variant_id: int | None
        variant_id = self.variant_id

        read_at: None | str
        read_at = self.read_at

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        readable: dict[str, Any] | None
        if isinstance(self.readable, ListReadStatusResponse200DataItemReadableType0):
            readable = self.readable.to_dict()
        else:
            readable = self.readable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "readable_type": readable_type,
                "readable_id": readable_id,
                "variant_id": variant_id,
                "read_at": read_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "readable": readable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_read_status_response_200_data_item_readable_type_0 import (
            ListReadStatusResponse200DataItemReadableType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        readable_type = d.pop("readable_type")

        readable_id = d.pop("readable_id")

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        def _parse_read_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        read_at = _parse_read_at(d.pop("read_at"))

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

        def _parse_readable(data: object) -> ListReadStatusResponse200DataItemReadableType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                readable_type_0 = ListReadStatusResponse200DataItemReadableType0.from_dict(data)

                return readable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListReadStatusResponse200DataItemReadableType0 | None, data)

        readable = _parse_readable(d.pop("readable"))

        list_read_status_response_200_data_item = cls(
            id=id,
            user_id=user_id,
            readable_type=readable_type,
            readable_id=readable_id,
            variant_id=variant_id,
            read_at=read_at,
            created_at=created_at,
            updated_at=updated_at,
            readable=readable,
        )

        list_read_status_response_200_data_item.additional_properties = d
        return list_read_status_response_200_data_item

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
