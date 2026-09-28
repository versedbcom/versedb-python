from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_story_arc_detail_response_200_data_end_issue_images import (
        GetStoryArcDetailResponse200DataEndIssueImages,
    )
    from ..models.get_story_arc_detail_response_200_data_end_issue_series import (
        GetStoryArcDetailResponse200DataEndIssueSeries,
    )


T = TypeVar("T", bound="GetStoryArcDetailResponse200DataEndIssue")


@_attrs_define
class GetStoryArcDetailResponse200DataEndIssue:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        issue_number (str | Unset):
        series_id (int | Unset):
        cover_url (str | Unset):
        images (GetStoryArcDetailResponse200DataEndIssueImages | Unset):
        series (GetStoryArcDetailResponse200DataEndIssueSeries | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    issue_number: str | Unset = UNSET
    series_id: int | Unset = UNSET
    cover_url: str | Unset = UNSET
    images: GetStoryArcDetailResponse200DataEndIssueImages | Unset = UNSET
    series: GetStoryArcDetailResponse200DataEndIssueSeries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        issue_number = self.issue_number

        series_id = self.series_id

        cover_url = self.cover_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if images is not UNSET:
            field_dict["images"] = images
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arc_detail_response_200_data_end_issue_images import (
            GetStoryArcDetailResponse200DataEndIssueImages,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_end_issue_series import (
            GetStoryArcDetailResponse200DataEndIssueSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        series_id = d.pop("series_id", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetStoryArcDetailResponse200DataEndIssueImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetStoryArcDetailResponse200DataEndIssueImages.from_dict(_images)

        _series = d.pop("series", UNSET)
        series: GetStoryArcDetailResponse200DataEndIssueSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = GetStoryArcDetailResponse200DataEndIssueSeries.from_dict(_series)

        get_story_arc_detail_response_200_data_end_issue = cls(
            id=id,
            name=name,
            slug=slug,
            issue_number=issue_number,
            series_id=series_id,
            cover_url=cover_url,
            images=images,
            series=series,
        )

        get_story_arc_detail_response_200_data_end_issue.additional_properties = d
        return get_story_arc_detail_response_200_data_end_issue

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
