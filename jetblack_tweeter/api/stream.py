"""Support for streams"""

import asyncio
from random import random
from typing import Any, AsyncIterable, List, Optional, Tuple


from ..constants import URL_STREAM_1_1
from ..types import AbstractHttpClient, BoundingBox, FilterLevel, Number
from ..utils import (
    optional_str_list_to_str,
    optional_int_list_to_str,
    bool_to_str,
    optional_bounding_box_list_to_str
)


class Stream:
    """Support for the stream end point"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the stream end endpoint

        Args:
            client (AbstractHttpClient): An authenticated client.
        """
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
            Any: A status response
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
        async for message in self._client.stream(url, body):  # type: ignore
            yield message

    async def sample(
            self,
            *,
            delay: Optional[Tuple[Number, Number]] = None
    ) -> AsyncIterable[Any]:
        """Retrieve a sampling of public statuses

        Args:
            delay (Optional[Tuple[Number, Number]], optional): A random delay in
                seconds (min,max) to apply to responses. Defaults to None.
        Yields:
            Any: A sample status response
        """
        if delay is None:
            delay = (0, 0)
        url = f'{URL_STREAM_1_1}/statuses/sample.json'
        delay_min, delay_max = delay
        delay_range = delay_max - delay_min
        async for message in self._client.stream(url):  # type: ignore
            if delay_range > 0:
                num = random()
                delay_seconds = delay_min + num * delay_range
                await asyncio.sleep(delay_seconds)
            yield message
