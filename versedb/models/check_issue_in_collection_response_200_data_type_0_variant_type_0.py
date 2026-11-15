from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckIssueInCollectionResponse200DataType0VariantType0")


@_attrs_define
class CheckIssueInCollectionResponse200DataType0VariantType0:
    """The catalog variant `variant_id` names, while it is a live variant of the copy's issue; null for any other copy.

    Attributes:
        id (int):
        name (None | str):
        type_ (None | str): The variant's `variant_type`.
        cover_url (None | str):
        cover_url_lg (None | str):
        ratio (None | str):
        printing (int | None):
        is_nsfw (bool): The variant cover's own flag, or the issue's when the variant has no cover.
    """

    id: int
    name: None | str
    type_: None | str
    cover_url: None | str
    cover_url_lg: None | str
    ratio: None | str
    printing: int | None
    is_nsfw: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        type_: None | str
        type_ = self.type_

        cover_url: None | str
        cover_url = self.cover_url

        cover_url_lg: None | str
        cover_url_lg = self.cover_url_lg

        ratio: None | str
        ratio = self.ratio

        printing: int | None
        printing = self.printing

        is_nsfw = self.is_nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "cover_url": cover_url,
                "cover_url_lg": cover_url_lg,
                "ratio": ratio,
                "printing": printing,
                "is_nsfw": is_nsfw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_cover_url_lg(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url_lg = _parse_cover_url_lg(d.pop("cover_url_lg"))

        def _parse_ratio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ratio = _parse_ratio(d.pop("ratio"))

        def _parse_printing(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        printing = _parse_printing(d.pop("printing"))

        is_nsfw = d.pop("is_nsfw")

        check_issue_in_collection_response_200_data_type_0_variant_type_0 = cls(
            id=id,
            name=name,
            type_=type_,
            cover_url=cover_url,
            cover_url_lg=cover_url_lg,
            ratio=ratio,
            printing=printing,
            is_nsfw=is_nsfw,
        )

        check_issue_in_collection_response_200_data_type_0_variant_type_0.additional_properties = d
        return check_issue_in_collection_response_200_data_type_0_variant_type_0

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
