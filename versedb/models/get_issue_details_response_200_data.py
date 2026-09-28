from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_issue_details_response_200_data_characters_item import (
        GetIssueDetailsResponse200DataCharactersItem,
    )
    from ..models.get_issue_details_response_200_data_creators_item import GetIssueDetailsResponse200DataCreatorsItem
    from ..models.get_issue_details_response_200_data_publisher import GetIssueDetailsResponse200DataPublisher
    from ..models.get_issue_details_response_200_data_series import GetIssueDetailsResponse200DataSeries
    from ..models.get_issue_details_response_200_data_title import GetIssueDetailsResponse200DataTitle


T = TypeVar("T", bound="GetIssueDetailsResponse200Data")


@_attrs_define
class GetIssueDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        slug (str | Unset):
        series_id (int | Unset):
        issue_number (str | Unset):
        name (str | Unset):
        solicitation (str | Unset):
        release_date (str | Unset):
        cover_date (str | Unset):
        cover_url (str | Unset):
        is_reprint (bool | Unset):
        content_rating_label (str | Unset):
        min_age (int | Unset):
        is_nsfw (bool | Unset):
        page_count (int | Unset):
        price (str | Unset):
        upc (str | Unset):
        series (GetIssueDetailsResponse200DataSeries | Unset):
        title (GetIssueDetailsResponse200DataTitle | Unset):
        publisher (GetIssueDetailsResponse200DataPublisher | Unset):
        creators (list[GetIssueDetailsResponse200DataCreatorsItem] | Unset):
        characters (list[GetIssueDetailsResponse200DataCharactersItem] | Unset):
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    series_id: int | Unset = UNSET
    issue_number: str | Unset = UNSET
    name: str | Unset = UNSET
    solicitation: str | Unset = UNSET
    release_date: str | Unset = UNSET
    cover_date: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    is_reprint: bool | Unset = UNSET
    content_rating_label: str | Unset = UNSET
    min_age: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    page_count: int | Unset = UNSET
    price: str | Unset = UNSET
    upc: str | Unset = UNSET
    series: GetIssueDetailsResponse200DataSeries | Unset = UNSET
    title: GetIssueDetailsResponse200DataTitle | Unset = UNSET
    publisher: GetIssueDetailsResponse200DataPublisher | Unset = UNSET
    creators: list[GetIssueDetailsResponse200DataCreatorsItem] | Unset = UNSET
    characters: list[GetIssueDetailsResponse200DataCharactersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        series_id = self.series_id

        issue_number = self.issue_number

        name = self.name

        solicitation = self.solicitation

        release_date = self.release_date

        cover_date = self.cover_date

        cover_url = self.cover_url

        is_reprint = self.is_reprint

        content_rating_label = self.content_rating_label

        min_age = self.min_age

        is_nsfw = self.is_nsfw

        page_count = self.page_count

        price = self.price

        upc = self.upc

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

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
        if solicitation is not UNSET:
            field_dict["solicitation"] = solicitation
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if cover_date is not UNSET:
            field_dict["cover_date"] = cover_date
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if is_reprint is not UNSET:
            field_dict["is_reprint"] = is_reprint
        if content_rating_label is not UNSET:
            field_dict["content_rating_label"] = content_rating_label
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if price is not UNSET:
            field_dict["price"] = price
        if upc is not UNSET:
            field_dict["upc"] = upc
        if series is not UNSET:
            field_dict["series"] = series
        if title is not UNSET:
            field_dict["title"] = title
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if creators is not UNSET:
            field_dict["creators"] = creators
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_issue_details_response_200_data_characters_item import (
            GetIssueDetailsResponse200DataCharactersItem,  # noqa: PLC0415
        )
        from ..models.get_issue_details_response_200_data_creators_item import (
            GetIssueDetailsResponse200DataCreatorsItem,  # noqa: PLC0415
        )
        from ..models.get_issue_details_response_200_data_publisher import (
            GetIssueDetailsResponse200DataPublisher,  # noqa: PLC0415
        )
        from ..models.get_issue_details_response_200_data_series import (
            GetIssueDetailsResponse200DataSeries,  # noqa: PLC0415
        )
        from ..models.get_issue_details_response_200_data_title import (
            GetIssueDetailsResponse200DataTitle,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        series_id = d.pop("series_id", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        name = d.pop("name", UNSET)

        solicitation = d.pop("solicitation", UNSET)

        release_date = d.pop("release_date", UNSET)

        cover_date = d.pop("cover_date", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        is_reprint = d.pop("is_reprint", UNSET)

        content_rating_label = d.pop("content_rating_label", UNSET)

        min_age = d.pop("min_age", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        page_count = d.pop("page_count", UNSET)

        price = d.pop("price", UNSET)

        upc = d.pop("upc", UNSET)

        _series = d.pop("series", UNSET)
        series: GetIssueDetailsResponse200DataSeries | Unset
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = GetIssueDetailsResponse200DataSeries.from_dict(_series)

        _title = d.pop("title", UNSET)
        title: GetIssueDetailsResponse200DataTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = GetIssueDetailsResponse200DataTitle.from_dict(_title)

        _publisher = d.pop("publisher", UNSET)
        publisher: GetIssueDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetIssueDetailsResponse200DataPublisher.from_dict(_publisher)

        _creators = d.pop("creators", UNSET)
        creators: list[GetIssueDetailsResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetIssueDetailsResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

        _characters = d.pop("characters", UNSET)
        characters: list[GetIssueDetailsResponse200DataCharactersItem] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = GetIssueDetailsResponse200DataCharactersItem.from_dict(characters_item_data)

                characters.append(characters_item)

        get_issue_details_response_200_data = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            issue_number=issue_number,
            name=name,
            solicitation=solicitation,
            release_date=release_date,
            cover_date=cover_date,
            cover_url=cover_url,
            is_reprint=is_reprint,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            page_count=page_count,
            price=price,
            upc=upc,
            series=series,
            title=title,
            publisher=publisher,
            creators=creators,
            characters=characters,
        )

        get_issue_details_response_200_data.additional_properties = d
        return get_issue_details_response_200_data

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
