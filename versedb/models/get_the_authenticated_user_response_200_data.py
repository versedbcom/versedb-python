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
        id (int | Unset):
        name (str | Unset):
        username (str | Unset):
        email (str | Unset):
        bio (str | Unset):
        profile_image_url (str | Unset):
        banner_url (None | str | Unset):
        country_code (str | Unset):
        city (str | Unset):
        region (str | Unset):
        postal_code (str | Unset):
        formatted_location (str | Unset):
        is_private (bool | Unset):
        is_wishlist_public (bool | Unset):
        show_nsfw_warnings (bool | Unset):
        can_view_nsfw (bool | Unset):
        show_reading_list (bool | Unset):
        show_collection (bool | Unset):
        show_activity (bool | Unset):
        show_spoilers (bool | Unset):
        preferred_mediums (list[str] | Unset):
        preferred_genres (list[Any] | Unset):
        preferred_languages (list[str] | Unset):
        locale (str | Unset):
        is_pro (bool | Unset):
        level (int | Unset):
        xp (int | Unset):
        xp_for_next_level (int | Unset):
        xp_progress_percent (float | Unset):
        contributions_count (int | Unset):
        level_name (str | Unset):
        has_password (bool | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    username: str | Unset = UNSET
    email: str | Unset = UNSET
    bio: str | Unset = UNSET
    profile_image_url: str | Unset = UNSET
    banner_url: None | str | Unset = UNSET
    country_code: str | Unset = UNSET
    city: str | Unset = UNSET
    region: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    formatted_location: str | Unset = UNSET
    is_private: bool | Unset = UNSET
    is_wishlist_public: bool | Unset = UNSET
    show_nsfw_warnings: bool | Unset = UNSET
    can_view_nsfw: bool | Unset = UNSET
    show_reading_list: bool | Unset = UNSET
    show_collection: bool | Unset = UNSET
    show_activity: bool | Unset = UNSET
    show_spoilers: bool | Unset = UNSET
    preferred_mediums: list[str] | Unset = UNSET
    preferred_genres: list[Any] | Unset = UNSET
    preferred_languages: list[str] | Unset = UNSET
    locale: str | Unset = UNSET
    is_pro: bool | Unset = UNSET
    level: int | Unset = UNSET
    xp: int | Unset = UNSET
    xp_for_next_level: int | Unset = UNSET
    xp_progress_percent: float | Unset = UNSET
    contributions_count: int | Unset = UNSET
    level_name: str | Unset = UNSET
    has_password: bool | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        username = self.username

        email = self.email

        bio = self.bio

        profile_image_url = self.profile_image_url

        banner_url: None | str | Unset
        if isinstance(self.banner_url, Unset):
            banner_url = UNSET
        else:
            banner_url = self.banner_url

        country_code = self.country_code

        city = self.city

        region = self.region

        postal_code = self.postal_code

        formatted_location = self.formatted_location

        is_private = self.is_private

        is_wishlist_public = self.is_wishlist_public

        show_nsfw_warnings = self.show_nsfw_warnings

        can_view_nsfw = self.can_view_nsfw

        show_reading_list = self.show_reading_list

        show_collection = self.show_collection

        show_activity = self.show_activity

        show_spoilers = self.show_spoilers

        preferred_mediums: list[str] | Unset = UNSET
        if not isinstance(self.preferred_mediums, Unset):
            preferred_mediums = self.preferred_mediums

        preferred_genres: list[Any] | Unset = UNSET
        if not isinstance(self.preferred_genres, Unset):
            preferred_genres = self.preferred_genres

        preferred_languages: list[str] | Unset = UNSET
        if not isinstance(self.preferred_languages, Unset):
            preferred_languages = self.preferred_languages

        locale = self.locale

        is_pro = self.is_pro

        level = self.level

        xp = self.xp

        xp_for_next_level = self.xp_for_next_level

        xp_progress_percent = self.xp_progress_percent

        contributions_count = self.contributions_count

        level_name = self.level_name

        has_password = self.has_password

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if bio is not UNSET:
            field_dict["bio"] = bio
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
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
        if show_nsfw_warnings is not UNSET:
            field_dict["show_nsfw_warnings"] = show_nsfw_warnings
        if can_view_nsfw is not UNSET:
            field_dict["can_view_nsfw"] = can_view_nsfw
        if show_reading_list is not UNSET:
            field_dict["show_reading_list"] = show_reading_list
        if show_collection is not UNSET:
            field_dict["show_collection"] = show_collection
        if show_activity is not UNSET:
            field_dict["show_activity"] = show_activity
        if show_spoilers is not UNSET:
            field_dict["show_spoilers"] = show_spoilers
        if preferred_mediums is not UNSET:
            field_dict["preferred_mediums"] = preferred_mediums
        if preferred_genres is not UNSET:
            field_dict["preferred_genres"] = preferred_genres
        if preferred_languages is not UNSET:
            field_dict["preferred_languages"] = preferred_languages
        if locale is not UNSET:
            field_dict["locale"] = locale
        if is_pro is not UNSET:
            field_dict["is_pro"] = is_pro
        if level is not UNSET:
            field_dict["level"] = level
        if xp is not UNSET:
            field_dict["xp"] = xp
        if xp_for_next_level is not UNSET:
            field_dict["xp_for_next_level"] = xp_for_next_level
        if xp_progress_percent is not UNSET:
            field_dict["xp_progress_percent"] = xp_progress_percent
        if contributions_count is not UNSET:
            field_dict["contributions_count"] = contributions_count
        if level_name is not UNSET:
            field_dict["level_name"] = level_name
        if has_password is not UNSET:
            field_dict["has_password"] = has_password
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        bio = d.pop("bio", UNSET)

        profile_image_url = d.pop("profile_image_url", UNSET)

        def _parse_banner_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banner_url = _parse_banner_url(d.pop("banner_url", UNSET))

        country_code = d.pop("country_code", UNSET)

        city = d.pop("city", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        formatted_location = d.pop("formatted_location", UNSET)

        is_private = d.pop("is_private", UNSET)

        is_wishlist_public = d.pop("is_wishlist_public", UNSET)

        show_nsfw_warnings = d.pop("show_nsfw_warnings", UNSET)

        can_view_nsfw = d.pop("can_view_nsfw", UNSET)

        show_reading_list = d.pop("show_reading_list", UNSET)

        show_collection = d.pop("show_collection", UNSET)

        show_activity = d.pop("show_activity", UNSET)

        show_spoilers = d.pop("show_spoilers", UNSET)

        preferred_mediums = cast(list[str], d.pop("preferred_mediums", UNSET))

        preferred_genres = cast(list[Any], d.pop("preferred_genres", UNSET))

        preferred_languages = cast(list[str], d.pop("preferred_languages", UNSET))

        locale = d.pop("locale", UNSET)

        is_pro = d.pop("is_pro", UNSET)

        level = d.pop("level", UNSET)

        xp = d.pop("xp", UNSET)

        xp_for_next_level = d.pop("xp_for_next_level", UNSET)

        xp_progress_percent = d.pop("xp_progress_percent", UNSET)

        contributions_count = d.pop("contributions_count", UNSET)

        level_name = d.pop("level_name", UNSET)

        has_password = d.pop("has_password", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        get_the_authenticated_user_response_200_data = cls(
            id=id,
            name=name,
            username=username,
            email=email,
            bio=bio,
            profile_image_url=profile_image_url,
            banner_url=banner_url,
            country_code=country_code,
            city=city,
            region=region,
            postal_code=postal_code,
            formatted_location=formatted_location,
            is_private=is_private,
            is_wishlist_public=is_wishlist_public,
            show_nsfw_warnings=show_nsfw_warnings,
            can_view_nsfw=can_view_nsfw,
            show_reading_list=show_reading_list,
            show_collection=show_collection,
            show_activity=show_activity,
            show_spoilers=show_spoilers,
            preferred_mediums=preferred_mediums,
            preferred_genres=preferred_genres,
            preferred_languages=preferred_languages,
            locale=locale,
            is_pro=is_pro,
            level=level,
            xp=xp,
            xp_for_next_level=xp_for_next_level,
            xp_progress_percent=xp_progress_percent,
            contributions_count=contributions_count,
            level_name=level_name,
            has_password=has_password,
            created_at=created_at,
            updated_at=updated_at,
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
