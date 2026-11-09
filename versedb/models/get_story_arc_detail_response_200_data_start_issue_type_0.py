from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_images_type_0 import (
        GetStoryArcDetailResponse200DataStartIssueType0ImagesType0,
    )
    from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_series_type_0 import (
        GetStoryArcDetailResponse200DataStartIssueType0SeriesType0,
    )


T = TypeVar("T", bound="GetStoryArcDetailResponse200DataStartIssueType0")


@_attrs_define
class GetStoryArcDetailResponse200DataStartIssueType0:
    """
    Attributes:
        id (int):
        name (str):
        slug (None | str):
        issue_number (None | str):
        series_id (int | None):
        cover_url (None | str):
        images (GetStoryArcDetailResponse200DataStartIssueType0ImagesType0 | None):
        series (GetStoryArcDetailResponse200DataStartIssueType0SeriesType0 | None):
    """

    id: int
    name: str
    slug: None | str
    issue_number: None | str
    series_id: int | None
    cover_url: None | str
    images: GetStoryArcDetailResponse200DataStartIssueType0ImagesType0 | None
    series: GetStoryArcDetailResponse200DataStartIssueType0SeriesType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_images_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0ImagesType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_series_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0SeriesType0,  # noqa: PLC0415
        )

        id = self.id

        name = self.name

        slug: None | str
        slug = self.slug

        issue_number: None | str
        issue_number = self.issue_number

        series_id: int | None
        series_id = self.series_id

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetStoryArcDetailResponse200DataStartIssueType0ImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        series: dict[str, Any] | None
        if isinstance(self.series, GetStoryArcDetailResponse200DataStartIssueType0SeriesType0):
            series = self.series.to_dict()
        else:
            series = self.series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "issue_number": issue_number,
                "series_id": series_id,
                "cover_url": cover_url,
                "images": images,
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_images_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0ImagesType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0_series_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0SeriesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> GetStoryArcDetailResponse200DataStartIssueType0ImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetStoryArcDetailResponse200DataStartIssueType0ImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataStartIssueType0ImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_series(data: object) -> GetStoryArcDetailResponse200DataStartIssueType0SeriesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_type_0 = GetStoryArcDetailResponse200DataStartIssueType0SeriesType0.from_dict(data)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataStartIssueType0SeriesType0 | None, data)

        series = _parse_series(d.pop("series"))

        get_story_arc_detail_response_200_data_start_issue_type_0 = cls(
            id=id,
            name=name,
            slug=slug,
            issue_number=issue_number,
            series_id=series_id,
            cover_url=cover_url,
            images=images,
            series=series,
        )

        get_story_arc_detail_response_200_data_start_issue_type_0.additional_properties = d
        return get_story_arc_detail_response_200_data_start_issue_type_0

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
