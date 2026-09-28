from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_collection_response_200_data_item_collectable_images import (
        ListCollectionResponse200DataItemCollectableImages,
    )
    from ..models.list_collection_response_200_data_item_collectable_key_issue_reasons_item import (
        ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem,
    )
    from ..models.list_collection_response_200_data_item_collectable_series import (
        ListCollectionResponse200DataItemCollectableSeries,
    )


T = TypeVar("T", bound="ListCollectionResponse200DataItemCollectable")


@_attrs_define
class ListCollectionResponse200DataItemCollectable:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        series_id (int | Unset):
        issue_number (str | Unset):
        name (str | Unset):
        cover_date (str | Unset):
        release_date (str | Unset):
        foc_date (str | Unset):
        cover_url (str | Unset):
        images (ListCollectionResponse200DataItemCollectableImages | Unset):
        is_reprint (bool | Unset):
        content_rating_label (None | str | Unset):
        min_age (None | str | Unset):
        is_nsfw (bool | Unset):
        average_rating (float | Unset):
        series (ListCollectionResponse200DataItemCollectableSeries | Unset):
        key_issue_reasons (list[ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem] | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    series_id: int | Unset = UNSET
    issue_number: str | Unset = UNSET
    name: str | Unset = UNSET
    cover_date: str | Unset = UNSET
    release_date: str | Unset = UNSET
    foc_date: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    images: ListCollectionResponse200DataItemCollectableImages | Unset = UNSET
    is_reprint: bool | Unset = UNSET
    content_rating_label: None | str | Unset = UNSET
    min_age: None | str | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    average_rating: float | Unset = UNSET
    series: ListCollectionResponse200DataItemCollectableSeries | Unset = UNSET
    key_issue_reasons: list[ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        series_id = self.series_id

        issue_number = self.issue_number

        name = self.name

        cover_date = self.cover_date

        release_date = self.release_date

        foc_date = self.foc_date

        cover_url = self.cover_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        is_reprint = self.is_reprint

        content_rating_label: None | str | Unset
        if isinstance(self.content_rating_label, Unset):
            content_rating_label = UNSET
        else:
            content_rating_label = self.content_rating_label

        min_age: None | str | Unset
        if isinstance(self.min_age, Unset):
            min_age = UNSET
        else:
            min_age = self.min_age

        is_nsfw = self.is_nsfw

        average_rating = self.average_rating

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        key_issue_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_issue_reasons, Unset):
            key_issue_reasons = []
            for key_issue_reasons_item_data in self.key_issue_reasons:
                key_issue_reasons_item = key_issue_reasons_item_data.to_dict()
                key_issue_reasons.append(key_issue_reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if name is not UNSET:
            field_dict["name"] = name
        if cover_date is not UNSET:
            field_dict["cover_date"] = cover_date
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if foc_date is not UNSET:
            field_dict["foc_date"] = foc_date
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if images is not UNSET:
            field_dict["images"] = images
        if is_reprint is not UNSET:
            field_dict["is_reprint"] = is_reprint
        if content_rating_label is not UNSET:
            field_dict["content_rating_label"] = content_rating_label
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if series is not UNSET:
            field_dict["series"] = series
        if key_issue_reasons is not UNSET:
            field_dict["key_issue_reasons"] = key_issue_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collection_response_200_data_item_collectable_images import (
            ListCollectionResponse200DataItemCollectableImages,  # noqa: PLC0415
        )
        from ..models.list_collection_response_200_data_item_collectable_key_issue_reasons_item import (
            ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem,  # noqa: PLC0415
        )
        from ..models.list_collection_response_200_data_item_collectable_series import (
            ListCollectionResponse200DataItemCollectableSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        series_id = d.pop("series_id", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        name = d.pop("name", UNSET)

        cover_date = d.pop("cover_date", UNSET)

        release_date = d.pop("release_date", UNSET)

        foc_date = d.pop("foc_date", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        _images = d.pop("images", UNSET)
        images: ListCollectionResponse200DataItemCollectableImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ListCollectionResponse200DataItemCollectableImages.from_dict(_images)

        is_reprint = d.pop("is_reprint", UNSET)

        def _parse_content_rating_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_rating_label = _parse_content_rating_label(d.pop("content_rating_label", UNSET))

        def _parse_min_age(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_age = _parse_min_age(d.pop("min_age", UNSET))

        is_nsfw = d.pop("is_nsfw", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        _series = d.pop("series", UNSET)
        series: ListCollectionResponse200DataItemCollectableSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = ListCollectionResponse200DataItemCollectableSeries.from_dict(_series)

        _key_issue_reasons = d.pop("key_issue_reasons", UNSET)
        key_issue_reasons: list[ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem] | Unset = UNSET
        if _key_issue_reasons is not UNSET:
            key_issue_reasons = []
            for key_issue_reasons_item_data in _key_issue_reasons:
                key_issue_reasons_item = ListCollectionResponse200DataItemCollectableKeyIssueReasonsItem.from_dict(
                    key_issue_reasons_item_data
                )

                key_issue_reasons.append(key_issue_reasons_item)

        list_collection_response_200_data_item_collectable = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            issue_number=issue_number,
            name=name,
            cover_date=cover_date,
            release_date=release_date,
            foc_date=foc_date,
            cover_url=cover_url,
            images=images,
            is_reprint=is_reprint,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            average_rating=average_rating,
            series=series,
            key_issue_reasons=key_issue_reasons,
        )

        list_collection_response_200_data_item_collectable.additional_properties = d
        return list_collection_response_200_data_item_collectable

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
