from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_issue_creators_response_200_data_item_aliases_i18n import (
        GetIssueCreatorsResponse200DataItemAliasesI18N,
    )
    from ..models.get_issue_creators_response_200_data_item_name_i18n import GetIssueCreatorsResponse200DataItemNameI18N
    from ..models.get_issue_creators_response_200_data_item_role import GetIssueCreatorsResponse200DataItemRole


T = TypeVar("T", bound="GetIssueCreatorsResponse200DataItem")


@_attrs_define
class GetIssueCreatorsResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        name_i18n (GetIssueCreatorsResponse200DataItemNameI18N | Unset):
        aliases_i18n (GetIssueCreatorsResponse200DataItemAliasesI18N | Unset):
        original_locale (str | Unset):
        role (GetIssueCreatorsResponse200DataItemRole | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    name_i18n: GetIssueCreatorsResponse200DataItemNameI18N | Unset = UNSET
    aliases_i18n: GetIssueCreatorsResponse200DataItemAliasesI18N | Unset = UNSET
    original_locale: str | Unset = UNSET
    role: GetIssueCreatorsResponse200DataItemRole | Unset = UNSET
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

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

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
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_issue_creators_response_200_data_item_aliases_i18n import (
            GetIssueCreatorsResponse200DataItemAliasesI18N,  # noqa: PLC0415
        )
        from ..models.get_issue_creators_response_200_data_item_name_i18n import (
            GetIssueCreatorsResponse200DataItemNameI18N,  # noqa: PLC0415
        )
        from ..models.get_issue_creators_response_200_data_item_role import GetIssueCreatorsResponse200DataItemRole  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _name_i18n = d.pop("name_i18n", UNSET)
        name_i18n: GetIssueCreatorsResponse200DataItemNameI18N | Unset
        if isinstance(_name_i18n, Unset):
            name_i18n = UNSET
        else:
            name_i18n = GetIssueCreatorsResponse200DataItemNameI18N.from_dict(_name_i18n)

        _aliases_i18n = d.pop("aliases_i18n", UNSET)
        aliases_i18n: GetIssueCreatorsResponse200DataItemAliasesI18N | Unset
        if isinstance(_aliases_i18n, Unset):
            aliases_i18n = UNSET
        else:
            aliases_i18n = GetIssueCreatorsResponse200DataItemAliasesI18N.from_dict(_aliases_i18n)

        original_locale = d.pop("original_locale", UNSET)

        _role = d.pop("role", UNSET)
        role: GetIssueCreatorsResponse200DataItemRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = GetIssueCreatorsResponse200DataItemRole.from_dict(_role)

        get_issue_creators_response_200_data_item = cls(
            id=id,
            name=name,
            name_i18n=name_i18n,
            aliases_i18n=aliases_i18n,
            original_locale=original_locale,
            role=role,
        )

        get_issue_creators_response_200_data_item.additional_properties = d
        return get_issue_creators_response_200_data_item

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
