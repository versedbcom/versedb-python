from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_pull_list_response_200_data_item_next_issue_type_0 import (
        ListPullListResponse200DataItemNextIssueType0,
    )
    from ..models.list_pull_list_response_200_data_item_notification_settings_type_4 import (
        ListPullListResponse200DataItemNotificationSettingsType4,
    )
    from ..models.list_pull_list_response_200_data_item_pull_source_type_0 import (
        ListPullListResponse200DataItemPullSourceType0,
    )
    from ..models.list_pull_list_response_200_data_item_pull_sources_item import (
        ListPullListResponse200DataItemPullSourcesItem,
    )
    from ..models.list_pull_list_response_200_data_item_series_images_type_0 import (
        ListPullListResponse200DataItemSeriesImagesType0,
    )
    from ..models.list_pull_list_response_200_data_item_series_type_0 import ListPullListResponse200DataItemSeriesType0


T = TypeVar("T", bound="ListPullListResponse200DataItem")


@_attrs_define
class ListPullListResponse200DataItem:
    """
    Attributes:
        id (int):
        user_id (int):
        pullable_type (None | str):
        pullable_id (int | None):
        series_id (int | None):
        variant_id (int | None):
        status (str): `active`, `paused` or `canceled`.
        created_at (None | str):
        updated_at (None | str):
        series_name (None | str): Null once the series is gone.
        series_cover_url (None | str):
        series_images (ListPullListResponse200DataItemSeriesImagesType0 | None):
        publisher_name (None | str):
        is_nsfw (bool):
        next_issue (ListPullListResponse200DataItemNextIssueType0 | None): The series' next issue released today or
            later that the member hasn't skipped.
        series (ListPullListResponse200DataItemSeriesType0 | None): Null once the series is gone.
        auto_pull (bool | None | Unset): Left out for a `read:showcase` token.
        last_pulled_at (None | str | Unset): Left out for a `read:showcase` token.
        preferred_cover_type (None | str | Unset): Left out for a `read:showcase` token.
        pull_priority (int | None | Unset): Left out for a `read:showcase` token.
        notify_on_release (bool | None | Unset): Left out for a `read:showcase` token.
        notification_settings (bool | float | list[Any] | ListPullListResponse200DataItemNotificationSettingsType4 |
            None | str | Unset): Left out for a `read:showcase` token.
        personal_notes (None | str | Unset): Left out for a `read:showcase` token.
        pull_source_ids (list[int] | Unset): Left out for a `read:showcase` token.
        pull_sources (list[ListPullListResponse200DataItemPullSourcesItem] | Unset): Left out for a `read:showcase`
            token.
        pull_source_id (int | None | Unset): Left out for a `read:showcase` token.
        pull_source (ListPullListResponse200DataItemPullSourceType0 | None | Unset): Left out for a `read:showcase`
            token.
    """

    id: int
    user_id: int
    pullable_type: None | str
    pullable_id: int | None
    series_id: int | None
    variant_id: int | None
    status: str
    created_at: None | str
    updated_at: None | str
    series_name: None | str
    series_cover_url: None | str
    series_images: ListPullListResponse200DataItemSeriesImagesType0 | None
    publisher_name: None | str
    is_nsfw: bool
    next_issue: ListPullListResponse200DataItemNextIssueType0 | None
    series: ListPullListResponse200DataItemSeriesType0 | None
    auto_pull: bool | None | Unset = UNSET
    last_pulled_at: None | str | Unset = UNSET
    preferred_cover_type: None | str | Unset = UNSET
    pull_priority: int | None | Unset = UNSET
    notify_on_release: bool | None | Unset = UNSET
    notification_settings: (
        bool | float | list[Any] | ListPullListResponse200DataItemNotificationSettingsType4 | None | str | Unset
    ) = UNSET
    personal_notes: None | str | Unset = UNSET
    pull_source_ids: list[int] | Unset = UNSET
    pull_sources: list[ListPullListResponse200DataItemPullSourcesItem] | Unset = UNSET
    pull_source_id: int | None | Unset = UNSET
    pull_source: ListPullListResponse200DataItemPullSourceType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_pull_list_response_200_data_item_next_issue_type_0 import (
            ListPullListResponse200DataItemNextIssueType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_notification_settings_type_4 import (
            ListPullListResponse200DataItemNotificationSettingsType4,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_pull_source_type_0 import (
            ListPullListResponse200DataItemPullSourceType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_series_images_type_0 import (
            ListPullListResponse200DataItemSeriesImagesType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_series_type_0 import (
            ListPullListResponse200DataItemSeriesType0,  # noqa: PLC0415
        )

        id = self.id

        user_id = self.user_id

        pullable_type: None | str
        pullable_type = self.pullable_type

        pullable_id: int | None
        pullable_id = self.pullable_id

        series_id: int | None
        series_id = self.series_id

        variant_id: int | None
        variant_id = self.variant_id

        status = self.status

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        series_name: None | str
        series_name = self.series_name

        series_cover_url: None | str
        series_cover_url = self.series_cover_url

        series_images: dict[str, Any] | None
        if isinstance(self.series_images, ListPullListResponse200DataItemSeriesImagesType0):
            series_images = self.series_images.to_dict()
        else:
            series_images = self.series_images

        publisher_name: None | str
        publisher_name = self.publisher_name

        is_nsfw = self.is_nsfw

        next_issue: dict[str, Any] | None
        if isinstance(self.next_issue, ListPullListResponse200DataItemNextIssueType0):
            next_issue = self.next_issue.to_dict()
        else:
            next_issue = self.next_issue

        series: dict[str, Any] | None
        if isinstance(self.series, ListPullListResponse200DataItemSeriesType0):
            series = self.series.to_dict()
        else:
            series = self.series

        auto_pull: bool | None | Unset
        if isinstance(self.auto_pull, Unset):
            auto_pull = UNSET
        else:
            auto_pull = self.auto_pull

        last_pulled_at: None | str | Unset
        if isinstance(self.last_pulled_at, Unset):
            last_pulled_at = UNSET
        else:
            last_pulled_at = self.last_pulled_at

        preferred_cover_type: None | str | Unset
        if isinstance(self.preferred_cover_type, Unset):
            preferred_cover_type = UNSET
        else:
            preferred_cover_type = self.preferred_cover_type

        pull_priority: int | None | Unset
        if isinstance(self.pull_priority, Unset):
            pull_priority = UNSET
        else:
            pull_priority = self.pull_priority

        notify_on_release: bool | None | Unset
        if isinstance(self.notify_on_release, Unset):
            notify_on_release = UNSET
        else:
            notify_on_release = self.notify_on_release

        notification_settings: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.notification_settings, Unset):
            notification_settings = UNSET
        elif isinstance(self.notification_settings, list):
            notification_settings = self.notification_settings

        elif isinstance(self.notification_settings, ListPullListResponse200DataItemNotificationSettingsType4):
            notification_settings = self.notification_settings.to_dict()
        else:
            notification_settings = self.notification_settings

        personal_notes: None | str | Unset
        if isinstance(self.personal_notes, Unset):
            personal_notes = UNSET
        else:
            personal_notes = self.personal_notes

        pull_source_ids: list[int] | Unset = UNSET
        if not isinstance(self.pull_source_ids, Unset):
            pull_source_ids = self.pull_source_ids

        pull_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pull_sources, Unset):
            pull_sources = []
            for pull_sources_item_data in self.pull_sources:
                pull_sources_item = pull_sources_item_data.to_dict()
                pull_sources.append(pull_sources_item)

        pull_source_id: int | None | Unset
        if isinstance(self.pull_source_id, Unset):
            pull_source_id = UNSET
        else:
            pull_source_id = self.pull_source_id

        pull_source: dict[str, Any] | None | Unset
        if isinstance(self.pull_source, Unset):
            pull_source = UNSET
        elif isinstance(self.pull_source, ListPullListResponse200DataItemPullSourceType0):
            pull_source = self.pull_source.to_dict()
        else:
            pull_source = self.pull_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "pullable_type": pullable_type,
                "pullable_id": pullable_id,
                "series_id": series_id,
                "variant_id": variant_id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "series_name": series_name,
                "series_cover_url": series_cover_url,
                "series_images": series_images,
                "publisher_name": publisher_name,
                "is_nsfw": is_nsfw,
                "next_issue": next_issue,
                "series": series,
            }
        )
        if auto_pull is not UNSET:
            field_dict["auto_pull"] = auto_pull
        if last_pulled_at is not UNSET:
            field_dict["last_pulled_at"] = last_pulled_at
        if preferred_cover_type is not UNSET:
            field_dict["preferred_cover_type"] = preferred_cover_type
        if pull_priority is not UNSET:
            field_dict["pull_priority"] = pull_priority
        if notify_on_release is not UNSET:
            field_dict["notify_on_release"] = notify_on_release
        if notification_settings is not UNSET:
            field_dict["notification_settings"] = notification_settings
        if personal_notes is not UNSET:
            field_dict["personal_notes"] = personal_notes
        if pull_source_ids is not UNSET:
            field_dict["pull_source_ids"] = pull_source_ids
        if pull_sources is not UNSET:
            field_dict["pull_sources"] = pull_sources
        if pull_source_id is not UNSET:
            field_dict["pull_source_id"] = pull_source_id
        if pull_source is not UNSET:
            field_dict["pull_source"] = pull_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_pull_list_response_200_data_item_next_issue_type_0 import (
            ListPullListResponse200DataItemNextIssueType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_notification_settings_type_4 import (
            ListPullListResponse200DataItemNotificationSettingsType4,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_pull_source_type_0 import (
            ListPullListResponse200DataItemPullSourceType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_pull_sources_item import (
            ListPullListResponse200DataItemPullSourcesItem,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_series_images_type_0 import (
            ListPullListResponse200DataItemSeriesImagesType0,  # noqa: PLC0415
        )
        from ..models.list_pull_list_response_200_data_item_series_type_0 import (
            ListPullListResponse200DataItemSeriesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        def _parse_pullable_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pullable_type = _parse_pullable_type(d.pop("pullable_type"))

        def _parse_pullable_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pullable_id = _parse_pullable_id(d.pop("pullable_id"))

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_variant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        status = d.pop("status")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_series_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_name = _parse_series_name(d.pop("series_name"))

        def _parse_series_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_cover_url = _parse_series_cover_url(d.pop("series_cover_url"))

        def _parse_series_images(data: object) -> ListPullListResponse200DataItemSeriesImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_images_type_0 = ListPullListResponse200DataItemSeriesImagesType0.from_dict(data)

                return series_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPullListResponse200DataItemSeriesImagesType0 | None, data)

        series_images = _parse_series_images(d.pop("series_images"))

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisher_name"))

        is_nsfw = d.pop("is_nsfw")

        def _parse_next_issue(data: object) -> ListPullListResponse200DataItemNextIssueType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_issue_type_0 = ListPullListResponse200DataItemNextIssueType0.from_dict(data)

                return next_issue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPullListResponse200DataItemNextIssueType0 | None, data)

        next_issue = _parse_next_issue(d.pop("next_issue"))

        def _parse_series(data: object) -> ListPullListResponse200DataItemSeriesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_type_0 = ListPullListResponse200DataItemSeriesType0.from_dict(data)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPullListResponse200DataItemSeriesType0 | None, data)

        series = _parse_series(d.pop("series"))

        def _parse_auto_pull(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_pull = _parse_auto_pull(d.pop("auto_pull", UNSET))

        def _parse_last_pulled_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_pulled_at = _parse_last_pulled_at(d.pop("last_pulled_at", UNSET))

        def _parse_preferred_cover_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_cover_type = _parse_preferred_cover_type(d.pop("preferred_cover_type", UNSET))

        def _parse_pull_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pull_priority = _parse_pull_priority(d.pop("pull_priority", UNSET))

        def _parse_notify_on_release(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_release = _parse_notify_on_release(d.pop("notify_on_release", UNSET))

        def _parse_notification_settings(
            data: object,
        ) -> bool | float | list[Any] | ListPullListResponse200DataItemNotificationSettingsType4 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_settings_type_3 = cast(list[Any], data)

                return notification_settings_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                notification_settings_type_4 = ListPullListResponse200DataItemNotificationSettingsType4.from_dict(data)

                return notification_settings_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | list[Any]
                | ListPullListResponse200DataItemNotificationSettingsType4
                | None
                | str
                | Unset,
                data,
            )

        notification_settings = _parse_notification_settings(d.pop("notification_settings", UNSET))

        def _parse_personal_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        personal_notes = _parse_personal_notes(d.pop("personal_notes", UNSET))

        pull_source_ids = cast(list[int], d.pop("pull_source_ids", UNSET))

        _pull_sources = d.pop("pull_sources", UNSET)
        pull_sources: list[ListPullListResponse200DataItemPullSourcesItem] | Unset = UNSET
        if _pull_sources is not UNSET:
            pull_sources = []
            for pull_sources_item_data in _pull_sources:
                pull_sources_item = ListPullListResponse200DataItemPullSourcesItem.from_dict(pull_sources_item_data)

                pull_sources.append(pull_sources_item)

        def _parse_pull_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pull_source_id = _parse_pull_source_id(d.pop("pull_source_id", UNSET))

        def _parse_pull_source(data: object) -> ListPullListResponse200DataItemPullSourceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pull_source_type_0 = ListPullListResponse200DataItemPullSourceType0.from_dict(data)

                return pull_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPullListResponse200DataItemPullSourceType0 | None | Unset, data)

        pull_source = _parse_pull_source(d.pop("pull_source", UNSET))

        list_pull_list_response_200_data_item = cls(
            id=id,
            user_id=user_id,
            pullable_type=pullable_type,
            pullable_id=pullable_id,
            series_id=series_id,
            variant_id=variant_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            series_name=series_name,
            series_cover_url=series_cover_url,
            series_images=series_images,
            publisher_name=publisher_name,
            is_nsfw=is_nsfw,
            next_issue=next_issue,
            series=series,
            auto_pull=auto_pull,
            last_pulled_at=last_pulled_at,
            preferred_cover_type=preferred_cover_type,
            pull_priority=pull_priority,
            notify_on_release=notify_on_release,
            notification_settings=notification_settings,
            personal_notes=personal_notes,
            pull_source_ids=pull_source_ids,
            pull_sources=pull_sources,
            pull_source_id=pull_source_id,
            pull_source=pull_source,
        )

        list_pull_list_response_200_data_item.additional_properties = d
        return list_pull_list_response_200_data_item

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
