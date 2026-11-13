from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_by_isbn_response_200_data_availabilities_item import (
        LookupByIsbnResponse200DataAvailabilitiesItem,
    )
    from ..models.lookup_by_isbn_response_200_data_awards_item import LookupByIsbnResponse200DataAwardsItem
    from ..models.lookup_by_isbn_response_200_data_characters_item import LookupByIsbnResponse200DataCharactersItem
    from ..models.lookup_by_isbn_response_200_data_comic_events_item import LookupByIsbnResponse200DataComicEventsItem
    from ..models.lookup_by_isbn_response_200_data_creators_item import LookupByIsbnResponse200DataCreatorsItem
    from ..models.lookup_by_isbn_response_200_data_images_type_0 import LookupByIsbnResponse200DataImagesType0
    from ..models.lookup_by_isbn_response_200_data_imprint import LookupByIsbnResponse200DataImprint
    from ..models.lookup_by_isbn_response_200_data_key_issue_reasons_item import (
        LookupByIsbnResponse200DataKeyIssueReasonsItem,
    )
    from ..models.lookup_by_isbn_response_200_data_name_i18n import LookupByIsbnResponse200DataNameI18N
    from ..models.lookup_by_isbn_response_200_data_publisher_type_0 import LookupByIsbnResponse200DataPublisherType0
    from ..models.lookup_by_isbn_response_200_data_series_type_0 import LookupByIsbnResponse200DataSeriesType0
    from ..models.lookup_by_isbn_response_200_data_story_arcs_item import LookupByIsbnResponse200DataStoryArcsItem
    from ..models.lookup_by_isbn_response_200_data_teams_item import LookupByIsbnResponse200DataTeamsItem
    from ..models.lookup_by_isbn_response_200_data_title import LookupByIsbnResponse200DataTitle
    from ..models.lookup_by_isbn_response_200_data_universes_item import LookupByIsbnResponse200DataUniversesItem


T = TypeVar("T", bound="LookupByIsbnResponse200Data")


@_attrs_define
class LookupByIsbnResponse200Data:
    """
    Attributes:
        id (int):
        slug (None | str):
        series_id (int | None):
        issue_number (None | str):
        name (None | str):
        solicitation (None | str):
        release_date (None | str):
        foc_date (None | str):
        cover_date (None | str):
        is_unreleased (bool):
        cover_url (None | str):
        images (LookupByIsbnResponse200DataImagesType0 | None):
        is_reprint (bool | None):
        content_rating_label (None | str):
        min_age (int | None):
        is_nsfw (bool | None):
        page_count (int | None):
        price (None | str):
        currency_code (None | str):
        formatted_price (None | str):
        isbn (None | str):
        upc (None | str):
        lunar_code (None | str):
        universal_code (None | str):
        diamond_code (None | str):
        ean (None | str):
        issn (None | str):
        is_anthology (bool | None):
        is_tie_in (bool):
        adapted_from (None | str):
        print_run (int | None):
        locations (None | str):
        sku (None | str):
        variant_count (int):
        reads_count (int):
        series (LookupByIsbnResponse200DataSeriesType0 | None):
        availabilities (list[LookupByIsbnResponse200DataAvailabilitiesItem]):
        name_i18n (LookupByIsbnResponse200DataNameI18N): One name per language, keyed by BCP 47 tag.
        average_rating (float | Unset):
        review_count (int | Unset):
        title (LookupByIsbnResponse200DataTitle | Unset):
        publisher (LookupByIsbnResponse200DataPublisherType0 | None | Unset):
        imprint (LookupByIsbnResponse200DataImprint | Unset):
        awards (list[LookupByIsbnResponse200DataAwardsItem] | Unset):
        creators (list[LookupByIsbnResponse200DataCreatorsItem] | Unset):
        characters (list[LookupByIsbnResponse200DataCharactersItem] | Unset):
        teams (list[LookupByIsbnResponse200DataTeamsItem] | Unset):
        story_arcs (list[LookupByIsbnResponse200DataStoryArcsItem] | Unset):
        universes (list[LookupByIsbnResponse200DataUniversesItem] | Unset):
        comic_events (list[LookupByIsbnResponse200DataComicEventsItem] | Unset):
        key_issue_reasons (list[LookupByIsbnResponse200DataKeyIssueReasonsItem] | Unset):
    """

    id: int
    slug: None | str
    series_id: int | None
    issue_number: None | str
    name: None | str
    solicitation: None | str
    release_date: None | str
    foc_date: None | str
    cover_date: None | str
    is_unreleased: bool
    cover_url: None | str
    images: LookupByIsbnResponse200DataImagesType0 | None
    is_reprint: bool | None
    content_rating_label: None | str
    min_age: int | None
    is_nsfw: bool | None
    page_count: int | None
    price: None | str
    currency_code: None | str
    formatted_price: None | str
    isbn: None | str
    upc: None | str
    lunar_code: None | str
    universal_code: None | str
    diamond_code: None | str
    ean: None | str
    issn: None | str
    is_anthology: bool | None
    is_tie_in: bool
    adapted_from: None | str
    print_run: int | None
    locations: None | str
    sku: None | str
    variant_count: int
    reads_count: int
    series: LookupByIsbnResponse200DataSeriesType0 | None
    availabilities: list[LookupByIsbnResponse200DataAvailabilitiesItem]
    name_i18n: LookupByIsbnResponse200DataNameI18N
    average_rating: float | Unset = UNSET
    review_count: int | Unset = UNSET
    title: LookupByIsbnResponse200DataTitle | Unset = UNSET
    publisher: LookupByIsbnResponse200DataPublisherType0 | None | Unset = UNSET
    imprint: LookupByIsbnResponse200DataImprint | Unset = UNSET
    awards: list[LookupByIsbnResponse200DataAwardsItem] | Unset = UNSET
    creators: list[LookupByIsbnResponse200DataCreatorsItem] | Unset = UNSET
    characters: list[LookupByIsbnResponse200DataCharactersItem] | Unset = UNSET
    teams: list[LookupByIsbnResponse200DataTeamsItem] | Unset = UNSET
    story_arcs: list[LookupByIsbnResponse200DataStoryArcsItem] | Unset = UNSET
    universes: list[LookupByIsbnResponse200DataUniversesItem] | Unset = UNSET
    comic_events: list[LookupByIsbnResponse200DataComicEventsItem] | Unset = UNSET
    key_issue_reasons: list[LookupByIsbnResponse200DataKeyIssueReasonsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookup_by_isbn_response_200_data_images_type_0 import LookupByIsbnResponse200DataImagesType0  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_publisher_type_0 import LookupByIsbnResponse200DataPublisherType0  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_series_type_0 import LookupByIsbnResponse200DataSeriesType0  # noqa: PLC0415

        id = self.id

        slug: None | str
        slug = self.slug

        series_id: int | None
        series_id = self.series_id

        issue_number: None | str
        issue_number = self.issue_number

        name: None | str
        name = self.name

        solicitation: None | str
        solicitation = self.solicitation

        release_date: None | str
        release_date = self.release_date

        foc_date: None | str
        foc_date = self.foc_date

        cover_date: None | str
        cover_date = self.cover_date

        is_unreleased = self.is_unreleased

        cover_url: None | str
        cover_url = self.cover_url

        images: dict[str, Any] | None
        if isinstance(self.images, LookupByIsbnResponse200DataImagesType0):
            images = self.images.to_dict()
        else:
            images = self.images

        is_reprint: bool | None
        is_reprint = self.is_reprint

        content_rating_label: None | str
        content_rating_label = self.content_rating_label

        min_age: int | None
        min_age = self.min_age

        is_nsfw: bool | None
        is_nsfw = self.is_nsfw

        page_count: int | None
        page_count = self.page_count

        price: None | str
        price = self.price

        currency_code: None | str
        currency_code = self.currency_code

        formatted_price: None | str
        formatted_price = self.formatted_price

        isbn: None | str
        isbn = self.isbn

        upc: None | str
        upc = self.upc

        lunar_code: None | str
        lunar_code = self.lunar_code

        universal_code: None | str
        universal_code = self.universal_code

        diamond_code: None | str
        diamond_code = self.diamond_code

        ean: None | str
        ean = self.ean

        issn: None | str
        issn = self.issn

        is_anthology: bool | None
        is_anthology = self.is_anthology

        is_tie_in = self.is_tie_in

        adapted_from: None | str
        adapted_from = self.adapted_from

        print_run: int | None
        print_run = self.print_run

        locations: None | str
        locations = self.locations

        sku: None | str
        sku = self.sku

        variant_count = self.variant_count

        reads_count = self.reads_count

        series: dict[str, Any] | None
        if isinstance(self.series, LookupByIsbnResponse200DataSeriesType0):
            series = self.series.to_dict()
        else:
            series = self.series

        availabilities = []
        for availabilities_item_data in self.availabilities:
            availabilities_item = availabilities_item_data.to_dict()
            availabilities.append(availabilities_item)

        name_i18n = self.name_i18n.to_dict()

        average_rating = self.average_rating

        review_count = self.review_count

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        publisher: dict[str, Any] | None | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        elif isinstance(self.publisher, LookupByIsbnResponse200DataPublisherType0):
            publisher = self.publisher.to_dict()
        else:
            publisher = self.publisher

        imprint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.imprint, Unset):
            imprint = self.imprint.to_dict()

        awards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        story_arcs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.story_arcs, Unset):
            story_arcs = []
            for story_arcs_item_data in self.story_arcs:
                story_arcs_item = story_arcs_item_data.to_dict()
                story_arcs.append(story_arcs_item)

        universes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.universes, Unset):
            universes = []
            for universes_item_data in self.universes:
                universes_item = universes_item_data.to_dict()
                universes.append(universes_item)

        comic_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comic_events, Unset):
            comic_events = []
            for comic_events_item_data in self.comic_events:
                comic_events_item = comic_events_item_data.to_dict()
                comic_events.append(comic_events_item)

        key_issue_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_issue_reasons, Unset):
            key_issue_reasons = []
            for key_issue_reasons_item_data in self.key_issue_reasons:
                key_issue_reasons_item = key_issue_reasons_item_data.to_dict()
                key_issue_reasons.append(key_issue_reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "series_id": series_id,
                "issue_number": issue_number,
                "name": name,
                "solicitation": solicitation,
                "release_date": release_date,
                "foc_date": foc_date,
                "cover_date": cover_date,
                "is_unreleased": is_unreleased,
                "cover_url": cover_url,
                "images": images,
                "is_reprint": is_reprint,
                "content_rating_label": content_rating_label,
                "min_age": min_age,
                "is_nsfw": is_nsfw,
                "page_count": page_count,
                "price": price,
                "currency_code": currency_code,
                "formatted_price": formatted_price,
                "isbn": isbn,
                "upc": upc,
                "lunar_code": lunar_code,
                "universal_code": universal_code,
                "diamond_code": diamond_code,
                "ean": ean,
                "issn": issn,
                "is_anthology": is_anthology,
                "is_tie_in": is_tie_in,
                "adapted_from": adapted_from,
                "print_run": print_run,
                "locations": locations,
                "sku": sku,
                "variant_count": variant_count,
                "reads_count": reads_count,
                "series": series,
                "availabilities": availabilities,
                "name_i18n": name_i18n,
            }
        )
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if review_count is not UNSET:
            field_dict["review_count"] = review_count
        if title is not UNSET:
            field_dict["title"] = title
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if imprint is not UNSET:
            field_dict["imprint"] = imprint
        if awards is not UNSET:
            field_dict["awards"] = awards
        if creators is not UNSET:
            field_dict["creators"] = creators
        if characters is not UNSET:
            field_dict["characters"] = characters
        if teams is not UNSET:
            field_dict["teams"] = teams
        if story_arcs is not UNSET:
            field_dict["story_arcs"] = story_arcs
        if universes is not UNSET:
            field_dict["universes"] = universes
        if comic_events is not UNSET:
            field_dict["comic_events"] = comic_events
        if key_issue_reasons is not UNSET:
            field_dict["key_issue_reasons"] = key_issue_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_by_isbn_response_200_data_availabilities_item import (
            LookupByIsbnResponse200DataAvailabilitiesItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_isbn_response_200_data_awards_item import LookupByIsbnResponse200DataAwardsItem  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_characters_item import LookupByIsbnResponse200DataCharactersItem  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_comic_events_item import (
            LookupByIsbnResponse200DataComicEventsItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_isbn_response_200_data_creators_item import LookupByIsbnResponse200DataCreatorsItem  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_images_type_0 import LookupByIsbnResponse200DataImagesType0  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_imprint import LookupByIsbnResponse200DataImprint  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_key_issue_reasons_item import (
            LookupByIsbnResponse200DataKeyIssueReasonsItem,  # noqa: PLC0415
        )
        from ..models.lookup_by_isbn_response_200_data_name_i18n import LookupByIsbnResponse200DataNameI18N  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_publisher_type_0 import LookupByIsbnResponse200DataPublisherType0  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_series_type_0 import LookupByIsbnResponse200DataSeriesType0  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_story_arcs_item import LookupByIsbnResponse200DataStoryArcsItem  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_teams_item import LookupByIsbnResponse200DataTeamsItem  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_title import LookupByIsbnResponse200DataTitle  # noqa: PLC0415
        from ..models.lookup_by_isbn_response_200_data_universes_item import LookupByIsbnResponse200DataUniversesItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_series_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        series_id = _parse_series_id(d.pop("series_id"))

        def _parse_issue_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_number = _parse_issue_number(d.pop("issue_number"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_solicitation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        solicitation = _parse_solicitation(d.pop("solicitation"))

        def _parse_release_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        release_date = _parse_release_date(d.pop("release_date"))

        def _parse_foc_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        foc_date = _parse_foc_date(d.pop("foc_date"))

        def _parse_cover_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_date = _parse_cover_date(d.pop("cover_date"))

        is_unreleased = d.pop("is_unreleased")

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(d.pop("cover_url"))

        def _parse_images(data: object) -> LookupByIsbnResponse200DataImagesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = LookupByIsbnResponse200DataImagesType0.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookupByIsbnResponse200DataImagesType0 | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_is_reprint(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_reprint = _parse_is_reprint(d.pop("is_reprint"))

        def _parse_content_rating_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_rating_label = _parse_content_rating_label(d.pop("content_rating_label"))

        def _parse_min_age(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_age = _parse_min_age(d.pop("min_age"))

        def _parse_is_nsfw(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw"))

        def _parse_page_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        page_count = _parse_page_count(d.pop("page_count"))

        def _parse_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        price = _parse_price(d.pop("price"))

        def _parse_currency_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency_code = _parse_currency_code(d.pop("currency_code"))

        def _parse_formatted_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formatted_price = _parse_formatted_price(d.pop("formatted_price"))

        def _parse_isbn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        isbn = _parse_isbn(d.pop("isbn"))

        def _parse_upc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upc = _parse_upc(d.pop("upc"))

        def _parse_lunar_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lunar_code = _parse_lunar_code(d.pop("lunar_code"))

        def _parse_universal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        universal_code = _parse_universal_code(d.pop("universal_code"))

        def _parse_diamond_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        diamond_code = _parse_diamond_code(d.pop("diamond_code"))

        def _parse_ean(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ean = _parse_ean(d.pop("ean"))

        def _parse_issn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issn = _parse_issn(d.pop("issn"))

        def _parse_is_anthology(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_anthology = _parse_is_anthology(d.pop("is_anthology"))

        is_tie_in = d.pop("is_tie_in")

        def _parse_adapted_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        adapted_from = _parse_adapted_from(d.pop("adapted_from"))

        def _parse_print_run(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        print_run = _parse_print_run(d.pop("print_run"))

        def _parse_locations(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locations = _parse_locations(d.pop("locations"))

        def _parse_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sku = _parse_sku(d.pop("sku"))

        variant_count = d.pop("variant_count")

        reads_count = d.pop("reads_count")

        def _parse_series(data: object) -> LookupByIsbnResponse200DataSeriesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_type_0 = LookupByIsbnResponse200DataSeriesType0.from_dict(data)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookupByIsbnResponse200DataSeriesType0 | None, data)

        series = _parse_series(d.pop("series"))

        availabilities = []
        _availabilities = d.pop("availabilities")
        for availabilities_item_data in _availabilities:
            availabilities_item = LookupByIsbnResponse200DataAvailabilitiesItem.from_dict(availabilities_item_data)

            availabilities.append(availabilities_item)

        name_i18n = LookupByIsbnResponse200DataNameI18N.from_dict(d.pop("name_i18n"))

        average_rating = d.pop("average_rating", UNSET)

        review_count = d.pop("review_count", UNSET)

        _title = d.pop("title", UNSET)
        title: LookupByIsbnResponse200DataTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = LookupByIsbnResponse200DataTitle.from_dict(_title)

        def _parse_publisher(data: object) -> LookupByIsbnResponse200DataPublisherType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                publisher_type_0 = LookupByIsbnResponse200DataPublisherType0.from_dict(data)

                return publisher_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookupByIsbnResponse200DataPublisherType0 | None | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        _imprint = d.pop("imprint", UNSET)
        imprint: LookupByIsbnResponse200DataImprint | Unset
        if isinstance(_imprint, Unset):
            imprint = UNSET
        else:
            imprint = LookupByIsbnResponse200DataImprint.from_dict(_imprint)

        _awards = d.pop("awards", UNSET)
        awards: list[LookupByIsbnResponse200DataAwardsItem] | Unset = UNSET
        if _awards is not UNSET:
            awards = []
            for awards_item_data in _awards:
                awards_item = LookupByIsbnResponse200DataAwardsItem.from_dict(awards_item_data)

                awards.append(awards_item)

        _creators = d.pop("creators", UNSET)
        creators: list[LookupByIsbnResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = LookupByIsbnResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

        _characters = d.pop("characters", UNSET)
        characters: list[LookupByIsbnResponse200DataCharactersItem] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = LookupByIsbnResponse200DataCharactersItem.from_dict(characters_item_data)

                characters.append(characters_item)

        _teams = d.pop("teams", UNSET)
        teams: list[LookupByIsbnResponse200DataTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = LookupByIsbnResponse200DataTeamsItem.from_dict(teams_item_data)

                teams.append(teams_item)

        _story_arcs = d.pop("story_arcs", UNSET)
        story_arcs: list[LookupByIsbnResponse200DataStoryArcsItem] | Unset = UNSET
        if _story_arcs is not UNSET:
            story_arcs = []
            for story_arcs_item_data in _story_arcs:
                story_arcs_item = LookupByIsbnResponse200DataStoryArcsItem.from_dict(story_arcs_item_data)

                story_arcs.append(story_arcs_item)

        _universes = d.pop("universes", UNSET)
        universes: list[LookupByIsbnResponse200DataUniversesItem] | Unset = UNSET
        if _universes is not UNSET:
            universes = []
            for universes_item_data in _universes:
                universes_item = LookupByIsbnResponse200DataUniversesItem.from_dict(universes_item_data)

                universes.append(universes_item)

        _comic_events = d.pop("comic_events", UNSET)
        comic_events: list[LookupByIsbnResponse200DataComicEventsItem] | Unset = UNSET
        if _comic_events is not UNSET:
            comic_events = []
            for comic_events_item_data in _comic_events:
                comic_events_item = LookupByIsbnResponse200DataComicEventsItem.from_dict(comic_events_item_data)

                comic_events.append(comic_events_item)

        _key_issue_reasons = d.pop("key_issue_reasons", UNSET)
        key_issue_reasons: list[LookupByIsbnResponse200DataKeyIssueReasonsItem] | Unset = UNSET
        if _key_issue_reasons is not UNSET:
            key_issue_reasons = []
            for key_issue_reasons_item_data in _key_issue_reasons:
                key_issue_reasons_item = LookupByIsbnResponse200DataKeyIssueReasonsItem.from_dict(
                    key_issue_reasons_item_data
                )

                key_issue_reasons.append(key_issue_reasons_item)

        lookup_by_isbn_response_200_data = cls(
            id=id,
            slug=slug,
            series_id=series_id,
            issue_number=issue_number,
            name=name,
            solicitation=solicitation,
            release_date=release_date,
            foc_date=foc_date,
            cover_date=cover_date,
            is_unreleased=is_unreleased,
            cover_url=cover_url,
            images=images,
            is_reprint=is_reprint,
            content_rating_label=content_rating_label,
            min_age=min_age,
            is_nsfw=is_nsfw,
            page_count=page_count,
            price=price,
            currency_code=currency_code,
            formatted_price=formatted_price,
            isbn=isbn,
            upc=upc,
            lunar_code=lunar_code,
            universal_code=universal_code,
            diamond_code=diamond_code,
            ean=ean,
            issn=issn,
            is_anthology=is_anthology,
            is_tie_in=is_tie_in,
            adapted_from=adapted_from,
            print_run=print_run,
            locations=locations,
            sku=sku,
            variant_count=variant_count,
            reads_count=reads_count,
            series=series,
            availabilities=availabilities,
            name_i18n=name_i18n,
            average_rating=average_rating,
            review_count=review_count,
            title=title,
            publisher=publisher,
            imprint=imprint,
            awards=awards,
            creators=creators,
            characters=characters,
            teams=teams,
            story_arcs=story_arcs,
            universes=universes,
            comic_events=comic_events,
            key_issue_reasons=key_issue_reasons,
        )

        lookup_by_isbn_response_200_data.additional_properties = d
        return lookup_by_isbn_response_200_data

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
