"""Support for streams"""

from typing import Any, AsyncIterable, List, Optional


from ..constants import URL_STREAM_1_1
from ..types import AbstractHttpClient, BoundingBox, FilterLevel
from ..utils import (
    optional_str_list_to_str,
    optional_int_list_to_str,
    bool_to_str,
    optional_bounding_box_list_to_str
)


class Stream:

    def __init__(self, client: AbstractHttpClient) -> None:
        self._client = client

    async def filter(
            self,
            *,
            follow: Optional[List[int]] = None,
            track: Optional[List[str]] = None,
            locations: Optional[List[BoundingBox]] = None,
            filter_level: FilterLevel = FilterLevel.NONE,
            delimited: Optional[int] = None,
            stall_warnings: bool = True
    ) -> AsyncIterable[Any]:
        """Follow the statuses filtering api

        Args:
            follow (Optional[List[int]], optional): List of user ids to follow.
                Defaults to None.
            track (Optional[List[str]], optional): List of keywords (or phrases)
                to track. Defaults to None.
            locations (Optional[List[BoundingBox]], optional): List of bounding boxes to
                track. Defaults to None.
            filter_level (FilterLevel, optional): Filter status update
                frequency. Defaults to FilterLevel.NONE.
            delimited (Optional[int], optional): Specifies whether messages should
                be length-delimited. Defaults None.
            stall_warnings (bool, optional): Whether or not to warn the caller
                about stalls when falling behind the twitter real time queue.
                Defaults to True.

        Yields:
            Any: A response
        """
        body = {
            'follow': optional_int_list_to_str(follow),
            'track': optional_str_list_to_str(track),
            'locations': optional_bounding_box_list_to_str(locations),
            'filter_level': filter_level.value,
            'delimited': delimited,
            'stall_warnings': bool_to_str(stall_warnings)
        }
        url = f'{URL_STREAM_1_1}/statuses/filter.json'
        async for message in self._client.stream(url, body):
            yield message

    async def sample(self) -> AsyncIterable:
        """Retrieve a sampling of public statuses"""
        url = f'{URL_STREAM_1_1}/statuses/sample.json'
        async for message in self._client.stream(url):
            yield message
