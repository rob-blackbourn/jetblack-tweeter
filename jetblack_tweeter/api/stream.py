"""Support for streams"""

from typing import Any, AsyncIterable, List, Optional


from ..constants import URL_STREAM_1_1
from ..types import AbstractHttpClient, FilterLevel
from ..utils import optional_str_list_to_str


class Stream:

    def __init__(self, client: AbstractHttpClient) -> None:
        self._client = client

    async def filter(
            self,
            *,
            track: Optional[List[str]] = None,
            follow: Optional[List[str]] = None,
            locations: Optional[List[str]] = None,
            filter_level: FilterLevel = FilterLevel.NONE,
            stall_warnings: bool = True
    ) -> AsyncIterable[Any]:
        """Follow the statuses filtering api

        https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter.html

        Args:
            track (Optional[List[str]], optional): List of keywords (or phrases)
                to track. Defaults to None.
            follow (Optional[List[str]], optional): List of user ids to follow.
                Defaults to None.
            locations (Optional[List[str]], optional): List of bounding boxes to
                track. Defaults to None.
            filter_level (FilterLevel, optional): Filter status update
                frequency. Defaults to FilterLevel.NONE.
            stall_warnings (bool, optional): Whether or not to warn the caller
                about stalls when falling behind the twitter real time queue.
                Defaults to True.

        Yields:
            Any: A response
        """
        body = {
            'filter_level': filter_level.value,
            'stall_warnings': 'true' if stall_warnings else 'false',
            'track': optional_str_list_to_str(track, ''),
            'follow': optional_str_list_to_str(follow, ''),
            'locations': optional_str_list_to_str(locations, ''),
        }
        url = f'{URL_STREAM_1_1}/statuses/filter.json'
        async for message in self._client.stream(url, body):
            yield message

    async def sample(self) -> AsyncIterable:
        """Retrieve a sampling of public statuses"""
        url = f'{URL_STREAM_1_1}/statuses/sample.json'
        async for message in self._client.stream(url):
            yield message
