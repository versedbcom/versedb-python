from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_list_body_status import UpdateListBodyStatus, check_update_list_body_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_list_body_rules import UpdateListBodyRules


T = TypeVar("T", bound="UpdateListBody")


@_attrs_define
class UpdateListBody:
    """
    Attributes:
        title (str | Unset): List title (max 100 chars).
        description (None | str | Unset): List description (max 2000 chars).
        is_ranked (bool | Unset): Whether items are ranked.
        is_private (bool | Unset): Whether the list is private. Non-wishlist private lists require a Pro subscription.
        status (UpdateListBodyStatus | Unset): The list status. One of: `published`, `draft`.
        rules (UpdateListBodyRules | Unset): A replacement smart-list rule. Accepted only on a list that was created
            rule-built — a rule is tuned here, never introduced or removed. Fetch the field catalog from `/lists/rule-
            vocabulary` and validate a draft against `/lists/rule-preview`.
    """

    title: str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_ranked: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    status: UpdateListBodyStatus | Unset = UNSET
    rules: UpdateListBodyRules | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_ranked = self.is_ranked

        is_private = self.is_private

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if is_ranked is not UNSET:
            field_dict["is_ranked"] = is_ranked
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if status is not UNSET:
            field_dict["status"] = status
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_list_body_rules import UpdateListBodyRules  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_ranked = d.pop("is_ranked", UNSET)

        is_private = d.pop("is_private", UNSET)

        _status = d.pop("status", UNSET)
        status: UpdateListBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_list_body_status(_status)

        _rules = d.pop("rules", UNSET)
        rules: UpdateListBodyRules | Unset
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = UpdateListBodyRules.from_dict(_rules)

        update_list_body = cls(
            title=title,
            description=description,
            is_ranked=is_ranked,
            is_private=is_private,
            status=status,
            rules=rules,
        )

        update_list_body.additional_properties = d
        return update_list_body

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
