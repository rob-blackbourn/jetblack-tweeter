"""Account messages"""

from datetime import date
from typing import Any, List, Mapping, Optional, Tuple, cast

from ..constants import URL_API_1_1
from ..types import AbstractHttpClient, Number, SearchResultType
from ..utils import optional_bool_to_str


Geocode = Tuple[Number, Number, str]


def geocode_to_str(value: Geocode) -> str:
    latitude, longitude, radius = value
    return f'{latitude},{longitude},{radius}'


def optional_geocode_to_str(
        value: Optional[Geocode],
        default: Optional[str] = None
) -> Optional[str]:
    return geocode_to_str(value) if value is not None else default


class Search:
    """The search end point api"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the search endpoint api

        Args:
            client (AbstractHttpClient): The authenticated client.
        """
        self._client = client
        self._url = f'{URL_API_1_1}/search'

    async def tweets(
        self,
        q: str,
        *,
        geocode: Optional[Geocode] = None,
        lang: Optional[str] = None,
        locale: Optional[str] = None,
        result_type: Optional[SearchResultType] = None,
        count: Optional[int] = None,
        until: Optional[date] = None,
        since_id: Optional[int] = None,
        max_id: Optional[int] = None,
        include_entities: Optional[bool] = None,
        timeout: Optional[float] = None
    ) -> List[Mapping[str, Any]]:
        """Returns a collection of relevant Tweets matching a specified query.

        Args:
            q (str): A UTF-8, URL-encoded search query of 500 characters
                maximum, including operators. Queries may additionally be
                limited by complexity.
            geocode (Optional[Tuple[Number, Number, str]], optional): Returns
                tweets by users located within a given radius of the given
                latitude/longitude. The location is preferentially taking from
                the Geotagging API, but will fall back to their Twitter profile.
                The parameter value is specified by "latitude,longitude,radius",
                where radius units must be specified as either "mi" (miles) or
                "km" (kilometers). Note that you cannot use the near operator
                via the API to geocode arbitrary locations; however you can use
                this geocode parameter to search near geocodes directly. A
                maximum of 1,000 distinct "sub-regions" will be considered when
                using the radius modifier. Defaults to None.
            lang (Optional[str], optional): Restricts tweets to the given
                language, given by an ISO 639-1 code. Language detection is
                best-effort. Defaults to None.
            locale (Optional[str], optional): Specify the language of the query
                you are sending (only ja is currently effective). This is
                intended for language-specific consumers and the default should
                work in the majority of cases. Defaults to None.
            result_type (Optional[SearchResultType], optional): Specifies what
                type of search results you would prefer to receive. The current
                default is "mixed". Defaults to None.
            count (Optional[int], optional): The number of tweets to return per
                page, 15 if unspecified, up to a maximum of 100. Defaults to
                None.
            until (Optional[date], optional): Returns tweets created before the
                given date. Date should be formatted as YYYY-MM-DD. Keep in mind
                that the search index has a 7-day limit. In other words, no
                tweets will be found for a date older than one week. Defaults to
                None.
            since_id (Optional[int], optional): Returns results with an ID
                greater than (that is, more recent than) the specified ID. There
                are limits to the number of Tweets which can be accessed through
                the API. If the limit of Tweets has occurred since the since_id,
                the since_id will be forced to the oldest ID available. Defaults
                to None.
            max_id (Optional[int], optional): Returns results with an ID less
                than (that is, older than) or equal to the specified ID.
                Defaults to None.
            include_entities (Optional[bool], optional): The entities node will
                not be included when set to false. Defaults to None.
            timeout (Optional[float], optional): If specified the timeout for
                the request. Defaults to None.

        Returns:
            List[Mapping[str, Any]]: A list of matching tweets.
        """
        body = {
            'q': q,
            'geocode': optional_geocode_to_str(geocode),
            'lang': lang,
            'locale': locale,
            'result_type': result_type.value if result_type is not None else None,
            'count': count,
            'until': until.isoformat() if until is not None else None,
            'since_id': since_id,
            'max_id': max_id,
            'include_entities': optional_bool_to_str(include_entities)
        }
        url = f'{self._url}/tweets.json'
        return cast(
            List[Mapping[str, Any]],
            await self._client.get(url, body, timeout)
        )
