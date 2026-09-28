from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_all_story_arcs_with_optional_search_response_200_data_item_images import (
        ListAllStoryArcsWithOptionalSearchResponse200DataItemImages,
    )
    from ..models.list_all_story_arcs_with_optional_search_response_200_data_item_primary_universe import (
        ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse,
    )


T = TypeVar("T", bound="ListAllStoryArcsWithOptionalSearchResponse200DataItem")


@_attrs_define
class ListAllStoryArcsWithOptionalSearchResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        image_url (str | Unset):
        images (ListAllStoryArcsWithOptionalSearchResponse200DataItemImages | Unset):
        issues_count (int | Unset):
        primary_universe (ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    image_url: str | Unset = UNSET
    images: ListAllStoryArcsWithOptionalSearchResponse200DataItemImages | Unset = UNSET
    issues_count: int | Unset = UNSET
    primary_universe: ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        type_ = self.type_

        status = self.status

        image_url = self.image_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        issues_count = self.issues_count

        primary_universe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_universe, Unset):
            primary_universe = self.primary_universe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if images is not UNSET:
            field_dict["images"] = images
        if issues_count is not UNSET:
            field_dict["issues_count"] = issues_count
        if primary_universe is not UNSET:
            field_dict["primary_universe"] = primary_universe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_story_arcs_with_optional_search_response_200_data_item_images import (
            ListAllStoryArcsWithOptionalSearchResponse200DataItemImages,  # noqa: PLC0415
        )
        from ..models.list_all_story_arcs_with_optional_search_response_200_data_item_primary_universe import (
            ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListAllStoryArcsWithOptionalSearchResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListAllStoryArcsWithOptionalSearchResponse200DataItemImages.from_dict(_images)

        issues_count = d.pop("issues_count", UNSET)

        _primary_universe = d.pop("primary_universe", UNSET)
        primary_universe: ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse | Unset
        if isinstance(_primary_universe, Unset):
            primary_universe = UNSET
        else:
            primary_universe = ListAllStoryArcsWithOptionalSearchResponse200DataItemPrimaryUniverse.from_dict(
                _primary_universe
            )

        list_all_story_arcs_with_optional_search_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            status=status,
            image_url=image_url,
            images=images,
            issues_count=issues_count,
            primary_universe=primary_universe,
        )

        list_all_story_arcs_with_optional_search_response_200_data_item.additional_properties = d
        return list_all_story_arcs_with_optional_search_response_200_data_item

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
