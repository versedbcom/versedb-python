from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_issue_characters_response_200_data_item_tags_item_name import (
        GetIssueCharactersResponse200DataItemTagsItemName,
    )
    from ..models.get_issue_characters_response_200_data_item_tags_item_pivot import (
        GetIssueCharactersResponse200DataItemTagsItemPivot,
    )
    from ..models.get_issue_characters_response_200_data_item_tags_item_slug import (
        GetIssueCharactersResponse200DataItemTagsItemSlug,
    )


T = TypeVar("T", bound="GetIssueCharactersResponse200DataItemTagsItem")


@_attrs_define
class GetIssueCharactersResponse200DataItemTagsItem:
    """
    Attributes:
        id (int):
        name (GetIssueCharactersResponse200DataItemTagsItemName):
        slug (GetIssueCharactersResponse200DataItemTagsItemSlug):
        type_ (None | str):
        order_column (int | None):
        created_at (None | str):
        updated_at (None | str):
        pivot (GetIssueCharactersResponse200DataItemTagsItemPivot):
    """

    id: int
    name: GetIssueCharactersResponse200DataItemTagsItemName
    slug: GetIssueCharactersResponse200DataItemTagsItemSlug
    type_: None | str
    order_column: int | None
    created_at: None | str
    updated_at: None | str
    pivot: GetIssueCharactersResponse200DataItemTagsItemPivot
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.to_dict()

        slug = self.slug.to_dict()

        type_: None | str
        type_ = self.type_

        order_column: int | None
        order_column = self.order_column

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        pivot = self.pivot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "order_column": order_column,
                "created_at": created_at,
                "updated_at": updated_at,
                "pivot": pivot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_issue_characters_response_200_data_item_tags_item_name import (
            GetIssueCharactersResponse200DataItemTagsItemName,  # noqa: PLC0415
        )
        from ..models.get_issue_characters_response_200_data_item_tags_item_pivot import (
            GetIssueCharactersResponse200DataItemTagsItemPivot,  # noqa: PLC0415
        )
        from ..models.get_issue_characters_response_200_data_item_tags_item_slug import (
            GetIssueCharactersResponse200DataItemTagsItemSlug,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = GetIssueCharactersResponse200DataItemTagsItemName.from_dict(d.pop("name"))

        slug = GetIssueCharactersResponse200DataItemTagsItemSlug.from_dict(d.pop("slug"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_order_column(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        order_column = _parse_order_column(d.pop("order_column"))

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

        pivot = GetIssueCharactersResponse200DataItemTagsItemPivot.from_dict(d.pop("pivot"))

        get_issue_characters_response_200_data_item_tags_item = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            order_column=order_column,
            created_at=created_at,
            updated_at=updated_at,
            pivot=pivot,
        )

        get_issue_characters_response_200_data_item_tags_item.additional_properties = d
        return get_issue_characters_response_200_data_item_tags_item

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
