from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_story_arcs_for_a_specific_issue_response_200_data_item_images import (
        GetStoryArcsForASpecificIssueResponse200DataItemImages,
    )


T = TypeVar("T", bound="GetStoryArcsForASpecificIssueResponse200DataItem")


@_attrs_define
class GetStoryArcsForASpecificIssueResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        image_url (str | Unset):
        images (GetStoryArcsForASpecificIssueResponse200DataItemImages | Unset):
        issues_count (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetStoryArcsForASpecificIssueResponse200DataItemImages | Unset = UNSET
    issues_count: int | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arcs_for_a_specific_issue_response_200_data_item_images import (
            GetStoryArcsForASpecificIssueResponse200DataItemImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetStoryArcsForASpecificIssueResponse200DataItemImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetStoryArcsForASpecificIssueResponse200DataItemImages.from_dict(_images)

        issues_count = d.pop("issues_count", UNSET)

        get_story_arcs_for_a_specific_issue_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            status=status,
            image_url=image_url,
            images=images,
            issues_count=issues_count,
        )

        get_story_arcs_for_a_specific_issue_response_200_data_item.additional_properties = d
        return get_story_arcs_for_a_specific_issue_response_200_data_item

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
