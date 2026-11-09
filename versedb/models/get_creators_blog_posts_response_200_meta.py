from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_creators_blog_posts_response_200_meta_links_item import (
        GetCreatorsBlogPostsResponse200MetaLinksItem,
    )


T = TypeVar("T", bound="GetCreatorsBlogPostsResponse200Meta")


@_attrs_define
class GetCreatorsBlogPostsResponse200Meta:
    """
    Attributes:
        current_page (int):
        from_ (int | None):
        last_page (int):
        links (list[GetCreatorsBlogPostsResponse200MetaLinksItem]):
        path (str):
        per_page (int):
        to (int | None):
        total (int):
    """

    current_page: int
    from_: int | None
    last_page: int
    links: list[GetCreatorsBlogPostsResponse200MetaLinksItem]
    path: str
    per_page: int
    to: int | None
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        from_: int | None
        from_ = self.from_

        last_page = self.last_page

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        path = self.path

        per_page = self.per_page

        to: int | None
        to = self.to

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "from": from_,
                "last_page": last_page,
                "links": links,
                "path": path,
                "per_page": per_page,
                "to": to,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creators_blog_posts_response_200_meta_links_item import (
            GetCreatorsBlogPostsResponse200MetaLinksItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        current_page = d.pop("current_page")

        def _parse_from_(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        from_ = _parse_from_(d.pop("from"))

        last_page = d.pop("last_page")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = GetCreatorsBlogPostsResponse200MetaLinksItem.from_dict(links_item_data)

            links.append(links_item)

        path = d.pop("path")

        per_page = d.pop("per_page")

        def _parse_to(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        to = _parse_to(d.pop("to"))

        total = d.pop("total")

        get_creators_blog_posts_response_200_meta = cls(
            current_page=current_page,
            from_=from_,
            last_page=last_page,
            links=links,
            path=path,
            per_page=per_page,
            to=to,
            total=total,
        )

        get_creators_blog_posts_response_200_meta.additional_properties = d
        return get_creators_blog_posts_response_200_meta

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
