from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_publisher_details_response_200_data_images import GetPublisherDetailsResponse200DataImages


T = TypeVar("T", bound="GetPublisherDetailsResponse200Data")


@_attrs_define
class GetPublisherDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        founded_year (int | Unset):
        website (str | Unset):
        headquarters (str | Unset):
        parent_company (str | Unset):
        status (str | Unset):
        logo_url (str | Unset):
        images (GetPublisherDetailsResponse200DataImages | Unset):
        first_published_year (int | Unset):
        aliases (list[str] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    founded_year: int | Unset = UNSET
    website: str | Unset = UNSET
    headquarters: str | Unset = UNSET
    parent_company: str | Unset = UNSET
    status: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    images: GetPublisherDetailsResponse200DataImages | Unset = UNSET
    first_published_year: int | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        founded_year = self.founded_year

        website = self.website

        headquarters = self.headquarters

        parent_company = self.parent_company

        status = self.status

        logo_url = self.logo_url

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        first_published_year = self.first_published_year

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if website is not UNSET:
            field_dict["website"] = website
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if parent_company is not UNSET:
            field_dict["parent_company"] = parent_company
        if status is not UNSET:
            field_dict["status"] = status
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if images is not UNSET:
            field_dict["images"] = images
        if first_published_year is not UNSET:
            field_dict["first_published_year"] = first_published_year
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_publisher_details_response_200_data_images import (
            GetPublisherDetailsResponse200DataImages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        founded_year = d.pop("founded_year", UNSET)

        website = d.pop("website", UNSET)

        headquarters = d.pop("headquarters", UNSET)

        parent_company = d.pop("parent_company", UNSET)

        status = d.pop("status", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _images = d.pop("images", UNSET)
        images: GetPublisherDetailsResponse200DataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = GetPublisherDetailsResponse200DataImages.from_dict(_images)

        first_published_year = d.pop("first_published_year", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        get_publisher_details_response_200_data = cls(
            id=id,
            name=name,
            founded_year=founded_year,
            website=website,
            headquarters=headquarters,
            parent_company=parent_company,
            status=status,
            logo_url=logo_url,
            images=images,
            first_published_year=first_published_year,
            aliases=aliases,
        )

        get_publisher_details_response_200_data.additional_properties = d
        return get_publisher_details_response_200_data

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
