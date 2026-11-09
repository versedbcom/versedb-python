from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unlike_list_response_200_type_1_reactions_item import UnlikeListResponse200Type1ReactionsItem


T = TypeVar("T", bound="UnlikeListResponse200Type1")


@_attrs_define
class UnlikeListResponse200Type1:
    """Not Liked

    Attributes:
        message (str):
        liked (bool):
        likes_count (int):
        my_reaction (None | str): The reaction the user now holds, null for none.
        reactions (list[UnlikeListResponse200Type1ReactionsItem]): Each reaction left on the list with its count, most
            used first.
    """

    message: str
    liked: bool
    likes_count: int
    my_reaction: None | str
    reactions: list[UnlikeListResponse200Type1ReactionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        liked = self.liked

        likes_count = self.likes_count

        my_reaction: None | str
        my_reaction = self.my_reaction

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "liked": liked,
                "likes_count": likes_count,
                "my_reaction": my_reaction,
                "reactions": reactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unlike_list_response_200_type_1_reactions_item import UnlikeListResponse200Type1ReactionsItem  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message")

        liked = d.pop("liked")

        likes_count = d.pop("likes_count")

        def _parse_my_reaction(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        my_reaction = _parse_my_reaction(d.pop("my_reaction"))

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = UnlikeListResponse200Type1ReactionsItem.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        unlike_list_response_200_type_1 = cls(
            message=message,
            liked=liked,
            likes_count=likes_count,
            my_reaction=my_reaction,
            reactions=reactions,
        )

        unlike_list_response_200_type_1.additional_properties = d
        return unlike_list_response_200_type_1

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
