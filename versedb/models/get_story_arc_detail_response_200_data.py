from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_story_arc_detail_response_200_data_aliases_i18n import GetStoryArcDetailResponse200DataAliasesI18N
    from ..models.get_story_arc_detail_response_200_data_end_issue_type_0 import (
        GetStoryArcDetailResponse200DataEndIssueType0,
    )
    from ..models.get_story_arc_detail_response_200_data_images_type_0 import (
        GetStoryArcDetailResponse200DataImagesType0,
    )
    from ..models.get_story_arc_detail_response_200_data_name_i18n import GetStoryArcDetailResponse200DataNameI18N
    from ..models.get_story_arc_detail_response_200_data_primary_universe_type_0 import (
        GetStoryArcDetailResponse200DataPrimaryUniverseType0,
    )
    from ..models.get_story_arc_detail_response_200_data_start_issue_type_0 import (
        GetStoryArcDetailResponse200DataStartIssueType0,
    )
    from ..models.get_story_arc_detail_response_200_data_universes_item import (
        GetStoryArcDetailResponse200DataUniversesItem,
    )


T = TypeVar("T", bound="GetStoryArcDetailResponse200Data")


@_attrs_define
class GetStoryArcDetailResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        type_ (None | str): main_story, side_story, tie_in_arc, mini_series_arc, crossover_event, prelude, epilogue or
            other.
        status (None | str): active, ended, upcoming or cancelled.
        image_url (None | str):
        images (GetStoryArcDetailResponse200DataImagesType0 | None):
        primary_universe_id (int | None):
        issues_count (int | None):
        characters_count (int):
        primary_universe (GetStoryArcDetailResponse200DataPrimaryUniverseType0 | None):
        universes (list[GetStoryArcDetailResponse200DataUniversesItem]):
        start_issue (GetStoryArcDetailResponse200DataStartIssueType0 | None):
        end_issue (GetStoryArcDetailResponse200DataEndIssueType0 | None):
        name_i18n (GetStoryArcDetailResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        aliases_i18n (GetStoryArcDetailResponse200DataAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the story arc is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    type_: None | str
    status: None | str
    image_url: None | str
    images: GetStoryArcDetailResponse200DataImagesType0 | None
    primary_universe_id: int | None
    issues_count: int | None
    characters_count: int
    primary_universe: GetStoryArcDetailResponse200DataPrimaryUniverseType0 | None
    universes: list[GetStoryArcDetailResponse200DataUniversesItem]
    start_issue: GetStoryArcDetailResponse200DataStartIssueType0 | None
    end_issue: GetStoryArcDetailResponse200DataEndIssueType0 | None
    name_i18n: GetStoryArcDetailResponse200DataNameI18N
    aliases_i18n: GetStoryArcDetailResponse200DataAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_story_arc_detail_response_200_data_end_issue_type_0 import (
            GetStoryArcDetailResponse200DataEndIssueType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_images_type_0 import (
            GetStoryArcDetailResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_primary_universe_type_0 import (
            GetStoryArcDetailResponse200DataPrimaryUniverseType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0,  # noqa: PLC0415
        )

        id = self.id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        type_: None | str
        type_ = self.type_

        status: None | str
        status = self.status

        image_url: None | str
        image_url = self.image_url

        images: dict[str, Any] | None
        if isinstance(self.images, GetStoryArcDetailResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        primary_universe_id: int | None
        primary_universe_id = self.primary_universe_id

        issues_count: int | None
        issues_count = self.issues_count

        characters_count = self.characters_count

        primary_universe: dict[str, Any] | None
        if isinstance(self.primary_universe, GetStoryArcDetailResponse200DataPrimaryUniverseType0):
            primary_universe = self.primary_universe.to_dict()
        else:
            primary_universe = self.primary_universe

        universes = []
        for universes_item_data in self.universes:
            universes_item = universes_item_data.to_dict()
            universes.append(universes_item)

        start_issue: dict[str, Any] | None
        if isinstance(self.start_issue, GetStoryArcDetailResponse200DataStartIssueType0):
            start_issue = self.start_issue.to_dict()
        else:
            start_issue = self.start_issue

        end_issue: dict[str, Any] | None
        if isinstance(self.end_issue, GetStoryArcDetailResponse200DataEndIssueType0):
            end_issue = self.end_issue.to_dict()
        else:
            end_issue = self.end_issue

        name_i18n = self.name_i18n.to_dict()

        aliases_i18n = self.aliases_i18n.to_dict()

        original_locale: None | str
        original_locale = self.original_locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "status": status,
                "image_url": image_url,
                "images": images,
                "primary_universe_id": primary_universe_id,
                "issues_count": issues_count,
                "characters_count": characters_count,
                "primary_universe": primary_universe,
                "universes": universes,
                "start_issue": start_issue,
                "end_issue": end_issue,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arc_detail_response_200_data_aliases_i18n import (
            GetStoryArcDetailResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_end_issue_type_0 import (
            GetStoryArcDetailResponse200DataEndIssueType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_images_type_0 import (
            GetStoryArcDetailResponse200DataImagesType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_name_i18n import GetStoryArcDetailResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_story_arc_detail_response_200_data_primary_universe_type_0 import (
            GetStoryArcDetailResponse200DataPrimaryUniverseType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_start_issue_type_0 import (
            GetStoryArcDetailResponse200DataStartIssueType0,  # noqa: PLC0415
        )
        from ..models.get_story_arc_detail_response_200_data_universes_item import (
            GetStoryArcDetailResponse200DataUniversesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_images(data: object) -> GetStoryArcDetailResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetStoryArcDetailResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_primary_universe_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        primary_universe_id = _parse_primary_universe_id(d.pop("primary_universe_id"))

        def _parse_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issues_count = _parse_issues_count(d.pop("issues_count"))

        characters_count = d.pop("characters_count")

        def _parse_primary_universe(data: object) -> GetStoryArcDetailResponse200DataPrimaryUniverseType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_universe_type_0 = GetStoryArcDetailResponse200DataPrimaryUniverseType0.from_dict(data)

                return primary_universe_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataPrimaryUniverseType0 | None, data)

        primary_universe = _parse_primary_universe(d.pop("primary_universe"))

        universes = []
        _universes = d.pop("universes")
        for universes_item_data in _universes:
            universes_item = GetStoryArcDetailResponse200DataUniversesItem.from_dict(universes_item_data)

            universes.append(universes_item)

        def _parse_start_issue(data: object) -> GetStoryArcDetailResponse200DataStartIssueType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                start_issue_type_0 = GetStoryArcDetailResponse200DataStartIssueType0.from_dict(data)

                return start_issue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataStartIssueType0 | None, data)

        start_issue = _parse_start_issue(d.pop("start_issue"))

        def _parse_end_issue(data: object) -> GetStoryArcDetailResponse200DataEndIssueType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                end_issue_type_0 = GetStoryArcDetailResponse200DataEndIssueType0.from_dict(data)

                return end_issue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcDetailResponse200DataEndIssueType0 | None, data)

        end_issue = _parse_end_issue(d.pop("end_issue"))

        name_i18n = GetStoryArcDetailResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetStoryArcDetailResponse200DataAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

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
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
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
