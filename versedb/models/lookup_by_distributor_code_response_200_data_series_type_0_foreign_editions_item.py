from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupByDistributorCodeResponse200DataSeriesType0ForeignEditionsItem")


@_attrs_define
class LookupByDistributorCodeResponse200DataSeriesType0ForeignEditionsItem:
    """
    Attributes:
        id (int):
        name (str):
        slug (None | str):
        language (None | str):
    """

    id: int
    name: str
    slug: None | str
    language: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug: None | str
        slug = self.slug

        language: None | str
        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        lookup_by_distributor_code_response_200_data_series_type_0_foreign_editions_item = cls(
            id=id,
            name=name,
            slug=slug,
            language=language,
        )

        lookup_by_distributor_code_response_200_data_series_type_0_foreign_editions_item.additional_properties = d
        return lookup_by_distributor_code_response_200_data_series_type_0_foreign_editions_item

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
