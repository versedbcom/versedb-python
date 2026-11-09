from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenAListToAnyTypeResponse200DataItemsItemEntityType1")


@_attrs_define
class OpenAListToAnyTypeResponse200DataItemsItemEntityType1:
    """A series.

    Attributes:
        id (int):
        slug (None | str):
        name (None | str):
        start_year (int | None):
        end_year (int | None):
        status (None | str):
        publication_type (None | str):
        image_url (None | str):
        is_nsfw (bool | None):
        issues_count (int | None):
        publisher (None | str):
    """

    id: int
    slug: None | str
    name: None | str
    start_year: int | None
    end_year: int | None
    status: None | str
    publication_type: None | str
    image_url: None | str
    is_nsfw: bool | None
    issues_count: int | None
    publisher: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug: None | str
        slug = self.slug

        name: None | str
        name = self.name

        start_year: int | None
        start_year = self.start_year

        end_year: int | None
        end_year = self.end_year

        status: None | str
        status = self.status

        publication_type: None | str
        publication_type = self.publication_type

        image_url: None | str
        image_url = self.image_url

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        issues_count: int | None
        issues_count = self.issues_count

        publisher: None | str
        publisher = self.publisher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "start_year": start_year,
                "end_year": end_year,
                "status": status,
                "publication_type": publication_type,
                "image_url": image_url,
                "is_nsfw": is_nsfw,
                "issues_count": issues_count,
                "publisher": publisher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_start_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        start_year = _parse_start_year(d.pop("start_year"))

        def _parse_end_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        end_year = _parse_end_year(d.pop("end_year"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_publication_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publication_type = _parse_publication_type(d.pop("publication_type"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issues_count = _parse_issues_count(d.pop("issues_count"))

        def _parse_publisher(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher = _parse_publisher(d.pop("publisher"))

        open_a_list_to_any_type_response_200_data_items_item_entity_type_1 = cls(
            id=id,
            slug=slug,
            name=name,
            start_year=start_year,
            end_year=end_year,
            status=status,
            publication_type=publication_type,
            image_url=image_url,
            is_nsfw=is_nsfw,
            issues_count=issues_count,
            publisher=publisher,
        )

        open_a_list_to_any_type_response_200_data_items_item_entity_type_1.additional_properties = d
        return open_a_list_to_any_type_response_200_data_items_item_entity_type_1

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
