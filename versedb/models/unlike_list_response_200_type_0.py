from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unlike_list_response_200_type_0_reactions_item import UnlikeListResponse200Type0ReactionsItem


T = TypeVar("T", bound="UnlikeListResponse200Type0")


@_attrs_define
class UnlikeListResponse200Type0:
    """Unliked

    Attributes:
        message (str | Unset):
        liked (bool | Unset):
        likes_count (int | Unset):
        my_reaction (None | str | Unset):
        reactions (list[UnlikeListResponse200Type0ReactionsItem] | Unset):
    """

    message: str | Unset = UNSET
    liked: bool | Unset = UNSET
    likes_count: int | Unset = UNSET
    my_reaction: None | str | Unset = UNSET
    reactions: list[UnlikeListResponse200Type0ReactionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        liked = self.liked

        likes_count = self.likes_count

        my_reaction: None | str | Unset
        if isinstance(self.my_reaction, Unset):
            my_reaction = UNSET
        else:
            my_reaction = self.my_reaction

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if liked is not UNSET:
            field_dict["liked"] = liked
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if my_reaction is not UNSET:
            field_dict["my_reaction"] = my_reaction
        if reactions is not UNSET:
            field_dict["reactions"] = reactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unlike_list_response_200_type_0_reactions_item import (
            UnlikeListResponse200Type0ReactionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        liked = d.pop("liked", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        def _parse_my_reaction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_reaction = _parse_my_reaction(d.pop("my_reaction", UNSET))

        _reactions = d.pop("reactions", UNSET)
        reactions: list[UnlikeListResponse200Type0ReactionsItem] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = UnlikeListResponse200Type0ReactionsItem.from_dict(reactions_item_data)

                reactions.append(reactions_item)

        unlike_list_response_200_type_0 = cls(
            message=message,
            liked=liked,
            likes_count=likes_count,
            my_reaction=my_reaction,
            reactions=reactions,
        )

        unlike_list_response_200_type_0.additional_properties = d
        return unlike_list_response_200_type_0

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
