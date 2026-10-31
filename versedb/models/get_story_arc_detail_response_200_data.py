from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_story_arc_detail_response_200_data_end_issue import GetStoryArcDetailResponse200DataEndIssue
    from ..models.get_story_arc_detail_response_200_data_images import GetStoryArcDetailResponse200DataImages
    from ..models.get_story_arc_detail_response_200_data_last_edited_by import (
        GetStoryArcDetailResponse200DataLastEditedBy,
    )
    from ..models.get_story_arc_detail_response_200_data_primary_universe import (
        GetStoryArcDetailResponse200DataPrimaryUniverse,
    )
    from ..models.get_story_arc_detail_response_200_data_start_issue import GetStoryArcDetailResponse200DataStartIssue
    from ..models.get_story_arc_detail_response_200_data_universes_item import (
        GetStoryArcDetailResponse200DataUniversesItem,
    )


T = TypeVar("T", bound="GetStoryArcDetailResponse200Data")


@_attrs_define
class GetStoryArcDetailResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        image_url (str | Unset):
        images (GetStoryArcDetailResponse200DataImages | Unset):
        primary_universe_id (int | Unset):
        issues_count (int | Unset):
        characters_count (int | Unset):
        primary_universe (GetStoryArcDetailResponse200DataPrimaryUniverse | Unset):
        universes (list[GetStoryArcDetailResponse200DataUniversesItem] | Unset):
        start_issue (GetStoryArcDetailResponse200DataStartIssue | Unset):
        end_issue (GetStoryArcDetailResponse200DataEndIssue | Unset):
        last_edited_by (GetStoryArcDetailResponse200DataLastEditedBy | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    image_url: str | Unset = UNSET
    images: GetStoryArcDetailResponse200DataImages | Unset = UNSET
    primary_universe_id: int | Unset = UNSET
    issues_count: int | Unset = UNSET
    characters_count: int | Unset = UNSET
    primary_universe: GetStoryArcDetailResponse200DataPrimaryUniverse | Unset = UNSET
    universes: list[GetStoryArcDetailResponse200DataUniversesItem] | Unset = UNSET
    start_issue: GetStoryArcDetailResponse200DataStartIssue | Unset = UNSET
    end_issue: GetStoryArcDetailResponse200DataEndIssue | Unset = UNSET
    last_edited_by: GetStoryArcDetailResponse200DataLastEditedBy | Unset = UNSET
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

        primary_universe_id = self.primary_universe_id

        issues_count = self.issues_count

        characters_count = self.characters_count

        primary_universe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_universe, Unset):
            primary_universe = self.primary_universe.to_dict()

        universes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.universes, Unset):
            universes = []
            for universes_item_data in self.universes:
                universes_item = universes_item_data.to_dict()
                universes.append(universes_item)

        start_issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_issue, Unset):
            start_issue = self.start_issue.to_dict()

        end_issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_issue, Unset):
            end_issue = self.end_issue.to_dict()

        last_edited_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_edited_by, Unset):
            last_edited_by = self.last_edited_by.to_dict()

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
        if primary_universe_id is not UNSET:
            field_dict["primary_universe_id"] = primary_universe_id
        if issues_count is not UNSET:
            field_dict["issues_count"] = issues_count
        if characters_count is not UNSET:
            field_dict["characters_count"] = characters_count
        if primary_universe is not UNSET:
            field_dict["primary_universe"] = primary_universe
        if universes is not UNSET:
            field_dict["universes"] = universes
        if start_issue is not UNSET:
            field_dict["start_issue"] = start_issue
        if end_issue is not UNSET:
            field_dict["end_issue"] = end_issue
        if last_edited_by is not UNSET:
            field_dict["last_edited_by"] = last_edited_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arc_detail_response_200_data_end_issue import GetStoryArcDetailResponse200DataEndIssue  # noqa: PLC0415
        from ..models.get_story_arc_detail_response_200_data_images import GetStoryArcDetailResponse200DataImages  # noqa: PLC0415
        from ..models.get_story_arc_detail_response_200_data_last_edited_by import (
            GetStoryArcDetailResponse200DataLastEditedBy,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_primary_universe import (
            GetStoryArcDetailResponse200DataPrimaryUniverse,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_start_issue import (
            GetStoryArcDetailResponse200DataStartIssue,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_universes_item import (
            GetStoryArcDetailResponse200DataUniversesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        image_url = d.pop("image_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetStoryArcDetailResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetStoryArcDetailResponse200DataImages.from_dict(_images)

        primary_universe_id = d.pop("primary_universe_id", UNSET)

        issues_count = d.pop("issues_count", UNSET)

        characters_count = d.pop("characters_count", UNSET)

        _primary_universe = d.pop("primary_universe", UNSET)
        primary_universe: GetStoryArcDetailResponse200DataPrimaryUniverse | Unset
        if isinstance(_primary_universe, Unset):
            primary_universe = UNSET
        else:
            primary_universe = GetStoryArcDetailResponse200DataPrimaryUniverse.from_dict(_primary_universe)

        _universes = d.pop("universes", UNSET)
        universes: list[GetStoryArcDetailResponse200DataUniversesItem] | Unset = UNSET
        if _universes is not UNSET:
            universes = []
            for universes_item_data in _universes:
                universes_item = GetStoryArcDetailResponse200DataUniversesItem.from_dict(universes_item_data)

                universes.append(universes_item)

        _start_issue = d.pop("start_issue", UNSET)
        start_issue: GetStoryArcDetailResponse200DataStartIssue | Unset
        if isinstance(_start_issue, Unset):
            start_issue = UNSET
        else:
            start_issue = GetStoryArcDetailResponse200DataStartIssue.from_dict(_start_issue)

        _end_issue = d.pop("end_issue", UNSET)
        end_issue: GetStoryArcDetailResponse200DataEndIssue | Unset
        if isinstance(_end_issue, Unset):
            end_issue = UNSET
        else:
            end_issue = GetStoryArcDetailResponse200DataEndIssue.from_dict(_end_issue)

        _last_edited_by = d.pop("last_edited_by", UNSET)
        last_edited_by: GetStoryArcDetailResponse200DataLastEditedBy | Unset
        if isinstance(_last_edited_by, Unset):
            last_edited_by = UNSET
        else:
            last_edited_by = GetStoryArcDetailResponse200DataLastEditedBy.from_dict(_last_edited_by)

        get_story_arc_detail_response_200_data = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            status=status,
            image_url=image_url,
            images=images,
            primary_universe_id=primary_universe_id,
            issues_count=issues_count,
            characters_count=characters_count,
            primary_universe=primary_universe,
            universes=universes,
            start_issue=start_issue,
            end_issue=end_issue,
            last_edited_by=last_edited_by,
        )

        get_story_arc_detail_response_200_data.additional_properties = d
        return get_story_arc_detail_response_200_data

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
