from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_list_response_201_data_cloned_from import CreateListResponse201DataClonedFrom
    from ..models.create_list_response_201_data_reactions_item import CreateListResponse201DataReactionsItem
    from ..models.create_list_response_201_data_sort_options import CreateListResponse201DataSortOptions
    from ..models.create_list_response_201_data_user_type_0 import CreateListResponse201DataUserType0


T = TypeVar("T", bound="CreateListResponse201Data")


@_attrs_define
class CreateListResponse201Data:
    """
    Attributes:
        id (int):
        title (str):
        slug (str):
        description (None | str):
        entity_type (str): issues, series, characters, creators, story_arcs, teams, or mixed for a list of any type.
        entity_type_label (str):
        is_curated (bool): The list is VerseDB's own.
        item_types (list[str]): The types its items hold: its own type, or each type a mixed list holds.
        is_ranked (bool):
        sort_options (CreateListResponse201DataSortOptions): What `sort` takes on this list, each with its label; the
            empty key is its own order.
        is_private (bool):
        status (str): published or draft.
        list_type (str): custom, wishlist or reading_guide.
        items_count (int):
        saves_count (int):
        likes_count (int):
        clones_count (int):
        created_at (str):
        updated_at (str):
        is_smart (bool): A rule keeps the list up to date.
        is_rule_based (bool):
        last_refreshed_at (None | str):
        smart_paused (bool): A rule-built list that stopped updating while its owner's Pro is inactive.
        cloned_from_list_id (int | None):
        user (CreateListResponse201DataUserType0 | None): The owner; null once the account is gone.
        reactions (list[CreateListResponse201DataReactionsItem]): The reactions left on the list, the most used first.
        cloned_from (CreateListResponse201DataClonedFrom | Unset): The list this one was cloned from, while it exists.
    """

    id: int
    title: str
    slug: str
    description: None | str
    entity_type: str
    entity_type_label: str
    is_curated: bool
    item_types: list[str]
    is_ranked: bool
    sort_options: CreateListResponse201DataSortOptions
    is_private: bool
    status: str
    list_type: str
    items_count: int
    saves_count: int
    likes_count: int
    clones_count: int
    created_at: str
    updated_at: str
    is_smart: bool
    is_rule_based: bool
    last_refreshed_at: None | str
    smart_paused: bool
    cloned_from_list_id: int | None
    user: CreateListResponse201DataUserType0 | None
    reactions: list[CreateListResponse201DataReactionsItem]
    cloned_from: CreateListResponse201DataClonedFrom | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_list_response_201_data_user_type_0 import CreateListResponse201DataUserType0  # noqa: PLC0415

        id = self.id

        title = self.title

        slug = self.slug

        description: None | str
        description = self.description

        entity_type = self.entity_type

        entity_type_label = self.entity_type_label

        is_curated = self.is_curated

        item_types = self.item_types

        is_ranked = self.is_ranked

        sort_options = self.sort_options.to_dict()

        is_private = self.is_private

        status = self.status

        list_type = self.list_type

        items_count = self.items_count

        saves_count = self.saves_count

        likes_count = self.likes_count

        clones_count = self.clones_count

        created_at = self.created_at

        updated_at = self.updated_at

        is_smart = self.is_smart

        is_rule_based = self.is_rule_based

        last_refreshed_at: None | str
        last_refreshed_at = self.last_refreshed_at

        smart_paused = self.smart_paused

        cloned_from_list_id: int | None
        cloned_from_list_id = self.cloned_from_list_id

        user: dict[str, Any] | None
        if isinstance(self.user, CreateListResponse201DataUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        cloned_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloned_from, Unset):
            cloned_from = self.cloned_from.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "slug": slug,
                "description": description,
                "entity_type": entity_type,
                "entity_type_label": entity_type_label,
                "is_curated": is_curated,
                "item_types": item_types,
                "is_ranked": is_ranked,
                "sort_options": sort_options,
                "is_private": is_private,
                "status": status,
                "list_type": list_type,
                "items_count": items_count,
                "saves_count": saves_count,
                "likes_count": likes_count,
                "clones_count": clones_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "is_smart": is_smart,
                "is_rule_based": is_rule_based,
                "last_refreshed_at": last_refreshed_at,
                "smart_paused": smart_paused,
                "cloned_from_list_id": cloned_from_list_id,
                "user": user,
                "reactions": reactions,
            }
        )
        if cloned_from is not UNSET:
            field_dict["cloned_from"] = cloned_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_list_response_201_data_cloned_from import CreateListResponse201DataClonedFrom  # noqa: PLC0415
        from ..models.create_list_response_201_data_reactions_item import CreateListResponse201DataReactionsItem  # noqa: PLC0415
        from ..models.create_list_response_201_data_sort_options import CreateListResponse201DataSortOptions  # noqa: PLC0415
        from ..models.create_list_response_201_data_user_type_0 import CreateListResponse201DataUserType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        slug = d.pop("slug")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        entity_type = d.pop("entity_type")

        entity_type_label = d.pop("entity_type_label")

        is_curated = d.pop("is_curated")

        item_types = cast(list[str], d.pop("item_types"))

        is_ranked = d.pop("is_ranked")

        sort_options = CreateListResponse201DataSortOptions.from_dict(d.pop("sort_options"))

        is_private = d.pop("is_private")

        status = d.pop("status")

        list_type = d.pop("list_type")

        items_count = d.pop("items_count")

        saves_count = d.pop("saves_count")

        likes_count = d.pop("likes_count")

        clones_count = d.pop("clones_count")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        is_smart = d.pop("is_smart")

        is_rule_based = d.pop("is_rule_based")

        def _parse_last_refreshed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_refreshed_at = _parse_last_refreshed_at(d.pop("last_refreshed_at"))

        smart_paused = d.pop("smart_paused")

        def _parse_cloned_from_list_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cloned_from_list_id = _parse_cloned_from_list_id(d.pop("cloned_from_list_id"))

        def _parse_user(data: object) -> CreateListResponse201DataUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = CreateListResponse201DataUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateListResponse201DataUserType0 | None, data)

        user = _parse_user(d.pop("user"))

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = CreateListResponse201DataReactionsItem.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        _cloned_from = d.pop("cloned_from", UNSET)
        cloned_from: CreateListResponse201DataClonedFrom | Unset
        if isinstance(_cloned_from, Unset):
            cloned_from = UNSET
        else:
            cloned_from = CreateListResponse201DataClonedFrom.from_dict(_cloned_from)

        create_list_response_201_data = cls(
            id=id,
            title=title,
            slug=slug,
            description=description,
            entity_type=entity_type,
            entity_type_label=entity_type_label,
            is_curated=is_curated,
            item_types=item_types,
            is_ranked=is_ranked,
            sort_options=sort_options,
            is_private=is_private,
            status=status,
            list_type=list_type,
            items_count=items_count,
            saves_count=saves_count,
            likes_count=likes_count,
            clones_count=clones_count,
            created_at=created_at,
            updated_at=updated_at,
            is_smart=is_smart,
            is_rule_based=is_rule_based,
            last_refreshed_at=last_refreshed_at,
            smart_paused=smart_paused,
            cloned_from_list_id=cloned_from_list_id,
            user=user,
            reactions=reactions,
            cloned_from=cloned_from,
        )

        create_list_response_201_data.additional_properties = d
        return create_list_response_201_data

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
