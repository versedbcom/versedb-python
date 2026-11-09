from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_list_response_201_data_cloned_from_user_type_0 import (
        CreateListResponse201DataClonedFromUserType0,
    )


T = TypeVar("T", bound="CreateListResponse201DataClonedFrom")


@_attrs_define
class CreateListResponse201DataClonedFrom:
    """The list this one was cloned from, while it exists.

    Attributes:
        id (int):
        title (None | str):
        slug (None | str):
        user (CreateListResponse201DataClonedFromUserType0 | None):
    """

    id: int
    title: None | str
    slug: None | str
    user: CreateListResponse201DataClonedFromUserType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_list_response_201_data_cloned_from_user_type_0 import (
            CreateListResponse201DataClonedFromUserType0,  # noqa: PLC0415
        )

        id = self.id

        title: None | str
        title = self.title

        slug: None | str
        slug = self.slug

        user: dict[str, Any] | None
        if isinstance(self.user, CreateListResponse201DataClonedFromUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "slug": slug,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_list_response_201_data_cloned_from_user_type_0 import (
            CreateListResponse201DataClonedFromUserType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_user(data: object) -> CreateListResponse201DataClonedFromUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = CreateListResponse201DataClonedFromUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateListResponse201DataClonedFromUserType0 | None, data)

        user = _parse_user(d.pop("user"))

        create_list_response_201_data_cloned_from = cls(
            id=id,
            title=title,
            slug=slug,
            user=user,
        )

        create_list_response_201_data_cloned_from.additional_properties = d
        return create_list_response_201_data_cloned_from

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
