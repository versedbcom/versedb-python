from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTheAuthenticatedUserResponse200Data")


@_attrs_define
class GetTheAuthenticatedUserResponse200Data:
    """
    Attributes:
        id (int):
        name (None | str):
        username (None | str):
        bio (None | str):
        avatar (None | str):
        profile_image (None | str):
        profile_image_url (None | str):
        banner_path (None | str):
        banner_url (None | str):
        is_pro (bool | None):
        level (int):
        xp (int):
        xp_for_next_level (int | None):
        xp_progress_percent (float):
        contributions_count (int):
        level_name (None | str):
        created_at (None | str):
        updated_at (None | str):
        email (None | str | Unset):
        country_code (None | str | Unset):
        city (None | str | Unset):
        region (None | str | Unset):
        postal_code (None | str | Unset):
        formatted_location (None | str | Unset):
        is_private (bool | None | Unset):
        is_wishlist_public (bool | None | Unset):
        public_wishlist_id (None | str | Unset):
        email_notifications (bool | None | Unset):
        content_edit_notifications (bool | None | Unset):
        comment_reply_notifications (bool | None | Unset):
        show_nsfw_warnings (bool | None | Unset):
        birth_date (None | str | Unset):
        can_view_nsfw (bool | Unset):
        show_reading_list (bool | None | Unset):
        show_collection (bool | None | Unset):
        show_activity (bool | None | Unset):
        show_followers (bool | None | Unset):
        show_following (bool | None | Unset):
        show_spoilers (bool | None | Unset):
        prompt_review_on_collect (bool | Unset):
        preferred_mediums (list[str] | Unset):
        preferred_genres (list[Any] | Unset):
        preferred_languages (list[str] | Unset):
        locale (None | str | Unset):
        onboarding_completed_at (None | str | Unset):
        onboarding_step (int | Unset):
        ai_discovery_enabled (bool | None | Unset):
        can_change_username (bool | Unset):
        has_password (bool | Unset):
        deletion_requested_at (None | str | Unset):
        deletion_confirmed_at (None | str | Unset):
        deletion_scheduled_for (None | str | Unset):
    """

    id: int
    name: None | str
    username: None | str
    bio: None | str
    avatar: None | str
    profile_image: None | str
    profile_image_url: None | str
    banner_path: None | str
    banner_url: None | str
    is_pro: bool | None
    level: int
    xp: int
    xp_for_next_level: int | None
    xp_progress_percent: float
    contributions_count: int
    level_name: None | str
    created_at: None | str
    updated_at: None | str
    email: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    formatted_location: None | str | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    is_wishlist_public: bool | None | Unset = UNSET
    public_wishlist_id: None | str | Unset = UNSET
    email_notifications: bool | None | Unset = UNSET
    content_edit_notifications: bool | None | Unset = UNSET
    comment_reply_notifications: bool | None | Unset = UNSET
    show_nsfw_warnings: bool | None | Unset = UNSET
    birth_date: None | str | Unset = UNSET
    can_view_nsfw: bool | Unset = UNSET
    show_reading_list: bool | None | Unset = UNSET
    show_collection: bool | None | Unset = UNSET
    show_activity: bool | None | Unset = UNSET
    show_followers: bool | None | Unset = UNSET
    show_following: bool | None | Unset = UNSET
    show_spoilers: bool | None | Unset = UNSET
    prompt_review_on_collect: bool | Unset = UNSET
    preferred_mediums: list[str] | Unset = UNSET
    preferred_genres: list[Any] | Unset = UNSET
    preferred_languages: list[str] | Unset = UNSET
    locale: None | str | Unset = UNSET
    onboarding_completed_at: None | str | Unset = UNSET
    onboarding_step: int | Unset = UNSET
    ai_discovery_enabled: bool | None | Unset = UNSET
    can_change_username: bool | Unset = UNSET
    has_password: bool | Unset = UNSET
    deletion_requested_at: None | str | Unset = UNSET
    deletion_confirmed_at: None | str | Unset = UNSET
    deletion_scheduled_for: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        username: None | str
        username = self.username

        bio: None | str
        bio = self.bio

        avatar: None | str
        avatar = self.avatar

        profile_image: None | str
        profile_image = self.profile_image

        profile_image_url: None | str
        profile_image_url = self.profile_image_url

        banner_path: None | str
        banner_path = self.banner_path

        banner_url: None | str
        banner_url = self.banner_url

        is_pro: bool | None
        is_pro = self.is_pro

        level = self.level

        xp = self.xp

        xp_for_next_level: int | None
        xp_for_next_level = self.xp_for_next_level

        xp_progress_percent = self.xp_progress_percent

        contributions_count = self.contributions_count

        level_name: None | str
        level_name = self.level_name

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        formatted_location: None | str | Unset
        if isinstance(self.formatted_location, Unset):
            formatted_location = UNSET
        else:
            formatted_location = self.formatted_location

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        is_wishlist_public: bool | None | Unset
        if isinstance(self.is_wishlist_public, Unset):
            is_wishlist_public = UNSET
        else:
            is_wishlist_public = self.is_wishlist_public

        public_wishlist_id: None | str | Unset
        if isinstance(self.public_wishlist_id, Unset):
            public_wishlist_id = UNSET
        else:
            public_wishlist_id = self.public_wishlist_id

        email_notifications: bool | None | Unset
        if isinstance(self.email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = self.email_notifications

        content_edit_notifications: bool | None | Unset
        if isinstance(self.content_edit_notifications, Unset):
            content_edit_notifications = UNSET
        else:
            content_edit_notifications = self.content_edit_notifications

        comment_reply_notifications: bool | None | Unset
        if isinstance(self.comment_reply_notifications, Unset):
            comment_reply_notifications = UNSET
        else:
            comment_reply_notifications = self.comment_reply_notifications

        show_nsfw_warnings: bool | None | Unset
        if isinstance(self.show_nsfw_warnings, Unset):
            show_nsfw_warnings = UNSET
        else:
            show_nsfw_warnings = self.show_nsfw_warnings

        birth_date: None | str | Unset
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = self.birth_date

        can_view_nsfw = self.can_view_nsfw

        show_reading_list: bool | None | Unset
        if isinstance(self.show_reading_list, Unset):
            show_reading_list = UNSET
        else:
            show_reading_list = self.show_reading_list

        show_collection: bool | None | Unset
        if isinstance(self.show_collection, Unset):
            show_collection = UNSET
        else:
            show_collection = self.show_collection

        show_activity: bool | None | Unset
        if isinstance(self.show_activity, Unset):
            show_activity = UNSET
        else:
            show_activity = self.show_activity

        show_followers: bool | None | Unset
        if isinstance(self.show_followers, Unset):
            show_followers = UNSET
        else:
            show_followers = self.show_followers

        show_following: bool | None | Unset
        if isinstance(self.show_following, Unset):
            show_following = UNSET
        else:
            show_following = self.show_following

        show_spoilers: bool | None | Unset
        if isinstance(self.show_spoilers, Unset):
            show_spoilers = UNSET
        else:
            show_spoilers = self.show_spoilers

        prompt_review_on_collect = self.prompt_review_on_collect

        preferred_mediums: list[str] | Unset = UNSET
        if not isinstance(self.preferred_mediums, Unset):
            preferred_mediums = self.preferred_mediums

        preferred_genres: list[Any] | Unset = UNSET
        if not isinstance(self.preferred_genres, Unset):
            preferred_genres = self.preferred_genres

        preferred_languages: list[str] | Unset = UNSET
        if not isinstance(self.preferred_languages, Unset):
            preferred_languages = self.preferred_languages

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        onboarding_completed_at: None | str | Unset
        if isinstance(self.onboarding_completed_at, Unset):
            onboarding_completed_at = UNSET
        else:
            onboarding_completed_at = self.onboarding_completed_at

        onboarding_step = self.onboarding_step

        ai_discovery_enabled: bool | None | Unset
        if isinstance(self.ai_discovery_enabled, Unset):
            ai_discovery_enabled = UNSET
        else:
            ai_discovery_enabled = self.ai_discovery_enabled

        can_change_username = self.can_change_username

        has_password = self.has_password

        deletion_requested_at: None | str | Unset
        if isinstance(self.deletion_requested_at, Unset):
            deletion_requested_at = UNSET
        else:
            deletion_requested_at = self.deletion_requested_at

        deletion_confirmed_at: None | str | Unset
        if isinstance(self.deletion_confirmed_at, Unset):
            deletion_confirmed_at = UNSET
        else:
            deletion_confirmed_at = self.deletion_confirmed_at

        deletion_scheduled_for: None | str | Unset
        if isinstance(self.deletion_scheduled_for, Unset):
            deletion_scheduled_for = UNSET
        else:
            deletion_scheduled_for = self.deletion_scheduled_for

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "username": username,
                "bio": bio,
                "avatar": avatar,
                "profile_image": profile_image,
                "profile_image_url": profile_image_url,
                "banner_path": banner_path,
                "banner_url": banner_url,
                "is_pro": is_pro,
                "level": level,
                "xp": xp,
                "xp_for_next_level": xp_for_next_level,
                "xp_progress_percent": xp_progress_percent,
                "contributions_count": contributions_count,
                "level_name": level_name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if formatted_location is not UNSET:
            field_dict["formatted_location"] = formatted_location
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if is_wishlist_public is not UNSET:
            field_dict["is_wishlist_public"] = is_wishlist_public
        if public_wishlist_id is not UNSET:
            field_dict["public_wishlist_id"] = public_wishlist_id
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if content_edit_notifications is not UNSET:
            field_dict["content_edit_notifications"] = content_edit_notifications
        if comment_reply_notifications is not UNSET:
            field_dict["comment_reply_notifications"] = comment_reply_notifications
        if show_nsfw_warnings is not UNSET:
            field_dict["show_nsfw_warnings"] = show_nsfw_warnings
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if can_view_nsfw is not UNSET:
            field_dict["can_view_nsfw"] = can_view_nsfw
        if show_reading_list is not UNSET:
            field_dict["show_reading_list"] = show_reading_list
        if show_collection is not UNSET:
            field_dict["show_collection"] = show_collection
        if show_activity is not UNSET:
            field_dict["show_activity"] = show_activity
        if show_followers is not UNSET:
            field_dict["show_followers"] = show_followers
        if show_following is not UNSET:
            field_dict["show_following"] = show_following
        if show_spoilers is not UNSET:
            field_dict["show_spoilers"] = show_spoilers
        if prompt_review_on_collect is not UNSET:
            field_dict["prompt_review_on_collect"] = prompt_review_on_collect
        if preferred_mediums is not UNSET:
            field_dict["preferred_mediums"] = preferred_mediums
        if preferred_genres is not UNSET:
            field_dict["preferred_genres"] = preferred_genres
        if preferred_languages is not UNSET:
            field_dict["preferred_languages"] = preferred_languages
        if locale is not UNSET:
            field_dict["locale"] = locale
        if onboarding_completed_at is not UNSET:
            field_dict["onboarding_completed_at"] = onboarding_completed_at
        if onboarding_step is not UNSET:
            field_dict["onboarding_step"] = onboarding_step
        if ai_discovery_enabled is not UNSET:
            field_dict["ai_discovery_enabled"] = ai_discovery_enabled
        if can_change_username is not UNSET:
            field_dict["can_change_username"] = can_change_username
        if has_password is not UNSET:
            field_dict["has_password"] = has_password
        if deletion_requested_at is not UNSET:
            field_dict["deletion_requested_at"] = deletion_requested_at
        if deletion_confirmed_at is not UNSET:
            field_dict["deletion_confirmed_at"] = deletion_confirmed_at
        if deletion_scheduled_for is not UNSET:
            field_dict["deletion_scheduled_for"] = deletion_scheduled_for

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        def _parse_avatar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        def _parse_profile_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_image = _parse_profile_image(d.pop("profile_image"))

        def _parse_profile_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_image_url = _parse_profile_image_url(d.pop("profile_image_url"))

        def _parse_banner_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        banner_path = _parse_banner_path(d.pop("banner_path"))

        def _parse_banner_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        banner_url = _parse_banner_url(d.pop("banner_url"))

        def _parse_is_pro(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_pro = _parse_is_pro(d.pop("is_pro"))

        level = d.pop("level")

        xp = d.pop("xp")

        def _parse_xp_for_next_level(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        xp_for_next_level = _parse_xp_for_next_level(d.pop("xp_for_next_level"))

        xp_progress_percent = d.pop("xp_progress_percent")

        contributions_count = d.pop("contributions_count")

        def _parse_level_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        level_name = _parse_level_name(d.pop("level_name"))

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

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_formatted_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_location = _parse_formatted_location(d.pop("formatted_location", UNSET))

        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("is_private", UNSET))

        def _parse_is_wishlist_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_wishlist_public = _parse_is_wishlist_public(d.pop("is_wishlist_public", UNSET))

        def _parse_public_wishlist_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_wishlist_id = _parse_public_wishlist_id(d.pop("public_wishlist_id", UNSET))

        def _parse_email_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_notifications = _parse_email_notifications(d.pop("email_notifications", UNSET))

        def _parse_content_edit_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        content_edit_notifications = _parse_content_edit_notifications(d.pop("content_edit_notifications", UNSET))

        def _parse_comment_reply_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        comment_reply_notifications = _parse_comment_reply_notifications(d.pop("comment_reply_notifications", UNSET))

        def _parse_show_nsfw_warnings(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_nsfw_warnings = _parse_show_nsfw_warnings(d.pop("show_nsfw_warnings", UNSET))

        def _parse_birth_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birth_date = _parse_birth_date(d.pop("birth_date", UNSET))

        can_view_nsfw = d.pop("can_view_nsfw", UNSET)

        def _parse_show_reading_list(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_reading_list = _parse_show_reading_list(d.pop("show_reading_list", UNSET))

        def _parse_show_collection(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_collection = _parse_show_collection(d.pop("show_collection", UNSET))

        def _parse_show_activity(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_activity = _parse_show_activity(d.pop("show_activity", UNSET))

        def _parse_show_followers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_followers = _parse_show_followers(d.pop("show_followers", UNSET))

        def _parse_show_following(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_following = _parse_show_following(d.pop("show_following", UNSET))

        def _parse_show_spoilers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_spoilers = _parse_show_spoilers(d.pop("show_spoilers", UNSET))

        prompt_review_on_collect = d.pop("prompt_review_on_collect", UNSET)

        preferred_mediums = cast(list[str], d.pop("preferred_mediums", UNSET))

        preferred_genres = cast(list[Any], d.pop("preferred_genres", UNSET))

        preferred_languages = cast(list[str], d.pop("preferred_languages", UNSET))

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        def _parse_onboarding_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        onboarding_completed_at = _parse_onboarding_completed_at(d.pop("onboarding_completed_at", UNSET))

        onboarding_step = d.pop("onboarding_step", UNSET)

        def _parse_ai_discovery_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ai_discovery_enabled = _parse_ai_discovery_enabled(d.pop("ai_discovery_enabled", UNSET))

        can_change_username = d.pop("can_change_username", UNSET)

        has_password = d.pop("has_password", UNSET)

        def _parse_deletion_requested_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deletion_requested_at = _parse_deletion_requested_at(d.pop("deletion_requested_at", UNSET))

        def _parse_deletion_confirmed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deletion_confirmed_at = _parse_deletion_confirmed_at(d.pop("deletion_confirmed_at", UNSET))

        def _parse_deletion_scheduled_for(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deletion_scheduled_for = _parse_deletion_scheduled_for(d.pop("deletion_scheduled_for", UNSET))

        get_the_authenticated_user_response_200_data = cls(
            id=id,
            name=name,
            username=username,
            bio=bio,
            avatar=avatar,
            profile_image=profile_image,
            profile_image_url=profile_image_url,
            banner_path=banner_path,
            banner_url=banner_url,
            is_pro=is_pro,
            level=level,
            xp=xp,
            xp_for_next_level=xp_for_next_level,
            xp_progress_percent=xp_progress_percent,
            contributions_count=contributions_count,
            level_name=level_name,
            created_at=created_at,
            updated_at=updated_at,
            email=email,
            country_code=country_code,
            city=city,
            region=region,
            postal_code=postal_code,
            formatted_location=formatted_location,
            is_private=is_private,
            is_wishlist_public=is_wishlist_public,
            public_wishlist_id=public_wishlist_id,
            email_notifications=email_notifications,
            content_edit_notifications=content_edit_notifications,
            comment_reply_notifications=comment_reply_notifications,
            show_nsfw_warnings=show_nsfw_warnings,
            birth_date=birth_date,
            can_view_nsfw=can_view_nsfw,
            show_reading_list=show_reading_list,
            show_collection=show_collection,
            show_activity=show_activity,
            show_followers=show_followers,
            show_following=show_following,
            show_spoilers=show_spoilers,
            prompt_review_on_collect=prompt_review_on_collect,
            preferred_mediums=preferred_mediums,
            preferred_genres=preferred_genres,
            preferred_languages=preferred_languages,
            locale=locale,
            onboarding_completed_at=onboarding_completed_at,
            onboarding_step=onboarding_step,
            ai_discovery_enabled=ai_discovery_enabled,
            can_change_username=can_change_username,
            has_password=has_password,
            deletion_requested_at=deletion_requested_at,
            deletion_confirmed_at=deletion_confirmed_at,
            deletion_scheduled_for=deletion_scheduled_for,
        )

        get_the_authenticated_user_response_200_data.additional_properties = d
        return get_the_authenticated_user_response_200_data

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
