from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_aliases_i18n import (
        GetStoryArcsForASpecificUniverseResponse200DataItemAliasesI18N,
    )
    from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_images_type_0 import (
        GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0,
    )
    from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_name_i18n import (
        GetStoryArcsForASpecificUniverseResponse200DataItemNameI18N,
    )


T = TypeVar("T", bound="GetStoryArcsForASpecificUniverseResponse200DataItem")


@_attrs_define
class GetStoryArcsForASpecificUniverseResponse200DataItem:
    """
    Attributes:
        id (int):
        name (None | str):
        slug (None | str):
        type_ (None | str): main_story, side_story, tie_in_arc, mini_series_arc, crossover_event, prelude, epilogue or
            other.
        status (None | str): active, ended, upcoming or cancelled.
        image_url (None | str):
        images (GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0 | None):
        issues_count (int | None):
        name_i18n (GetStoryArcsForASpecificUniverseResponse200DataItemNameI18N): One name per language, keyed by BCP 47
            tag.
        aliases_i18n (GetStoryArcsForASpecificUniverseResponse200DataItemAliasesI18N): Alternative names per language.
        original_locale (None | str): The language the story arc is from, a BCP 47 tag.
    """

    id: int
    name: None | str
    slug: None | str
    type_: None | str
    status: None | str
    image_url: None | str
    images: GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0 | None
    issues_count: int | None
    name_i18n: GetStoryArcsForASpecificUniverseResponse200DataItemNameI18N
    aliases_i18n: GetStoryArcsForASpecificUniverseResponse200DataItemAliasesI18N
    original_locale: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_images_type_0 import (
            GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0,  # noqa: PLC0415
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
        if isinstance(self.images, GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        issues_count: int | None
        issues_count = self.issues_count

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
                "issues_count": issues_count,
                "name_i18n": name_i18n,
                "aliases_i18n": aliases_i18n,
                "original_locale": original_locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_aliases_i18n import (
            GetStoryArcsForASpecificUniverseResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_images_type_0 import (
            GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0,  # noqa: PLC0415
        )
        from ..models.get_story_arcs_for_a_specific_universe_response_200_data_item_name_i18n import (
            GetStoryArcsForASpecificUniverseResponse200DataItemNameI18N,  # noqa: PLC0415
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

        def _parse_images(data: object) -> GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetStoryArcsForASpecificUniverseResponse200DataItemImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_issues_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        issues_count = _parse_issues_count(d.pop("issues_count"))

        name_i18n = GetStoryArcsForASpecificUniverseResponse200DataItemNameI18N.from_dict(d.pop("name_i18n"))

        aliases_i18n = GetStoryArcsForASpecificUniverseResponse200DataItemAliasesI18N.from_dict(d.pop("aliases_i18n"))

        def _parse_original_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_locale = _parse_original_locale(d.pop("original_locale"))

        get_story_arcs_for_a_specific_universe_response_200_data_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            status=status,
            image_url=image_url,
            images=images,
            issues_count=issues_count,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
        )

        get_story_arcs_for_a_specific_universe_response_200_data_item.additional_properties = d
        return get_story_arcs_for_a_specific_universe_response_200_data_item

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
