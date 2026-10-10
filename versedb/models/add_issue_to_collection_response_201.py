from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_issue_to_collection_response_201_data import AddIssueToCollectionResponse201Data
    from ..models.add_issue_to_collection_response_201_follow_up import AddIssueToCollectionResponse201FollowUp


T = TypeVar("T", bound="AddIssueToCollectionResponse201")


@_attrs_define
class AddIssueToCollectionResponse201:
    """
    Attributes:
        data (AddIssueToCollectionResponse201Data | Unset):
        was_on_wishlist (bool | Unset):
        follow_up (AddIssueToCollectionResponse201FollowUp | Unset):
    """

    data: AddIssueToCollectionResponse201Data | Unset = UNSET
    was_on_wishlist: bool | Unset = UNSET
    follow_up: AddIssueToCollectionResponse201FollowUp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        was_on_wishlist = self.was_on_wishlist

        follow_up: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_up, Unset):
            follow_up = self.follow_up.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if was_on_wishlist is not UNSET:
            field_dict["was_on_wishlist"] = was_on_wishlist
        if follow_up is not UNSET:
            field_dict["follow_up"] = follow_up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_issue_to_collection_response_201_data import AddIssueToCollectionResponse201Data  # noqa: PLC0415
        from ..models.add_issue_to_collection_response_201_follow_up import AddIssueToCollectionResponse201FollowUp  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: AddIssueToCollectionResponse201Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AddIssueToCollectionResponse201Data.from_dict(_data)

        was_on_wishlist = d.pop("was_on_wishlist", UNSET)

        _follow_up = d.pop("follow_up", UNSET)
        follow_up: AddIssueToCollectionResponse201FollowUp | Unset
        if isinstance(_follow_up, Unset):
            follow_up = UNSET
        else:
            follow_up = AddIssueToCollectionResponse201FollowUp.from_dict(_follow_up)

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
