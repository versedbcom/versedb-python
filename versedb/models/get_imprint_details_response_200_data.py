from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_imprint_details_response_200_data_aliases_i18n import GetImprintDetailsResponse200DataAliasesI18N
    from ..models.get_imprint_details_response_200_data_name_i18n import GetImprintDetailsResponse200DataNameI18N
    from ..models.get_imprint_details_response_200_data_publisher import GetImprintDetailsResponse200DataPublisher


T = TypeVar("T", bound="GetImprintDetailsResponse200Data")


@_attrs_define
class GetImprintDetailsResponse200Data:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        name_i18n (GetImprintDetailsResponse200DataNameI18N | Unset):
        aliases_i18n (GetImprintDetailsResponse200DataAliasesI18N | Unset):
        original_locale (str | Unset):
        slug (str | Unset):
        publisher (GetImprintDetailsResponse200DataPublisher | Unset):
        series_count (int | Unset):
        titles_count (int | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    name_i18n: GetImprintDetailsResponse200DataNameI18N | Unset = UNSET
    aliases_i18n: GetImprintDetailsResponse200DataAliasesI18N | Unset = UNSET
    original_locale: str | Unset = UNSET
    slug: str | Unset = UNSET
    publisher: GetImprintDetailsResponse200DataPublisher | Unset = UNSET
    series_count: int | Unset = UNSET
    titles_count: int | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_i18n, Unset):
            name_i18n = self.name_i18n.to_dict()

        aliases_i18n: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aliases_i18n, Unset):
            aliases_i18n = self.aliases_i18n.to_dict()

        original_locale = self.original_locale

        slug = self.slug

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        series_count = self.series_count

        titles_count = self.titles_count

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_i18n is not UNSET:
            field_dict["name_i18n"] = name_i18n
        if aliases_i18n is not UNSET:
            field_dict["aliases_i18n"] = aliases_i18n
        if original_locale is not UNSET:
            field_dict["original_locale"] = original_locale
        if slug is not UNSET:
            field_dict["slug"] = slug
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if series_count is not UNSET:
            field_dict["series_count"] = series_count
        if titles_count is not UNSET:
            field_dict["titles_count"] = titles_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_imprint_details_response_200_data_aliases_i18n import (
            GetImprintDetailsResponse200DataAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_imprint_details_response_200_data_name_i18n import GetImprintDetailsResponse200DataNameI18N  # noqa: PLC0415
        from ..models.get_imprint_details_response_200_data_publisher import GetImprintDetailsResponse200DataPublisher  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _name_i18n = d.pop("name_i18n", UNSET)
        name_i18n: GetImprintDetailsResponse200DataNameI18N | Unset
        if isinstance(_name_i18n, Unset):
            name_i18n = UNSET
        else:
            name_i18n = GetImprintDetailsResponse200DataNameI18N.from_dict(_name_i18n)

        _aliases_i18n = d.pop("aliases_i18n", UNSET)
        aliases_i18n: GetImprintDetailsResponse200DataAliasesI18N | Unset
        if isinstance(_aliases_i18n, Unset):
            aliases_i18n = UNSET
        else:
            aliases_i18n = GetImprintDetailsResponse200DataAliasesI18N.from_dict(_aliases_i18n)

        original_locale = d.pop("original_locale", UNSET)

        slug = d.pop("slug", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: GetImprintDetailsResponse200DataPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = GetImprintDetailsResponse200DataPublisher.from_dict(_publisher)

        series_count = d.pop("series_count", UNSET)

        titles_count = d.pop("titles_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        get_imprint_details_response_200_data = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            slug=slug,
            publisher=publisher,
            series_count=series_count,
            titles_count=titles_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_imprint_details_response_200_data.additional_properties = d
        return get_imprint_details_response_200_data

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
