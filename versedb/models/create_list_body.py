from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_list_body_rules_type_0 import CreateListBodyRulesType0


T = TypeVar("T", bound="CreateListBody")


@_attrs_define
class CreateListBody:
    """
    Attributes:
        title (str): List title (max 100 chars).
        description (None | str | Unset): List description (max 2000 chars).
        entity_type (None | str | Unset): The kind of item a smart-list rule matches (issues, series, characters,
            creators, story_arcs, teams). Required, and never `mixed`, when `rules` is supplied; ignored without it, because
            a list you fill by hand holds any combination of types.
        is_ranked (bool | Unset): Whether items are ranked/ordered. Defaults to true.
        is_private (bool | Unset): Whether the list is private. Requires a Pro subscription. Defaults to false.
        rules (CreateListBodyRulesType0 | None | Unset): A smart-list rule. Supply it to have the list built and kept
            current from a query instead of by hand. Requires a Pro subscription, and forces `is_ranked` to false because
            the rule carries its own sort. Fetch the field catalog from `/lists/rule-vocabulary` and validate a draft
            against `/lists/rule-preview`.
    """

    title: str
    description: None | str | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    is_ranked: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    rules: CreateListBodyRulesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_list_body_rules_type_0 import CreateListBodyRulesType0  # noqa: PLC0415

        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        is_ranked = self.is_ranked

        is_private = self.is_private

        rules: dict[str, Any] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, CreateListBodyRulesType0):
            rules = self.rules.to_dict()
        else:
            rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if is_ranked is not UNSET:
            field_dict["is_ranked"] = is_ranked
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_list_body_rules_type_0 import CreateListBodyRulesType0  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

        is_ranked = d.pop("is_ranked", UNSET)

        is_private = d.pop("is_private", UNSET)

        def _parse_rules(data: object) -> CreateListBodyRulesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rules_type_0 = CreateListBodyRulesType0.from_dict(data)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateListBodyRulesType0 | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        create_list_body = cls(
            title=title,
            description=description,
            entity_type=entity_type,
            is_ranked=is_ranked,
            is_private=is_private,
            rules=rules,
        )

        create_list_body.additional_properties = d
        return create_list_body

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
