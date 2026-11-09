from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_issue_to_collection_response_201_data import AddIssueToCollectionResponse201Data
    from ..models.add_issue_to_collection_response_201_follow_up import AddIssueToCollectionResponse201FollowUp


T = TypeVar("T", bound="AddIssueToCollectionResponse201")


@_attrs_define
class AddIssueToCollectionResponse201:
    """
    Attributes:
        data (AddIssueToCollectionResponse201Data):
        was_on_wishlist (bool):
        follow_up (AddIssueToCollectionResponse201FollowUp):
    """

    data: AddIssueToCollectionResponse201Data
    was_on_wishlist: bool
    follow_up: AddIssueToCollectionResponse201FollowUp
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        was_on_wishlist = self.was_on_wishlist

        follow_up = self.follow_up.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "was_on_wishlist": was_on_wishlist,
                "follow_up": follow_up,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_issue_to_collection_response_201_data import AddIssueToCollectionResponse201Data  # noqa: PLC0415
        from ..models.add_issue_to_collection_response_201_follow_up import AddIssueToCollectionResponse201FollowUp  # noqa: PLC0415

        d = dict(src_dict)
        data = AddIssueToCollectionResponse201Data.from_dict(d.pop("data"))

        was_on_wishlist = d.pop("was_on_wishlist")

        follow_up = AddIssueToCollectionResponse201FollowUp.from_dict(d.pop("follow_up"))

        add_issue_to_collection_response_201 = cls(
            data=data,
            was_on_wishlist=was_on_wishlist,
            follow_up=follow_up,
        )

        add_issue_to_collection_response_201.additional_properties = d
        return add_issue_to_collection_response_201

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
