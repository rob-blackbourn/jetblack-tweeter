"""The twitter client"""

from typing import Any, AsyncIterable, List, Optional

from .auth_client import AuthenticatedHttpClient
from .types import AbstractTweeterSession, FilterLevel

URL_STREAM_1_1 = 'https://stream.twitter.com/1.1'
URL_API_1_1 = 'https://api.twitter.com/1.1'


class Tweeter:

    def __init__(
            self,
            session: AbstractTweeterSession,
            app_key: str,
            app_key_secret: str,
            *,
            access_token: Optional[str] = None,
            access_token_secret: Optional[str] = None
    ):
        self._client = AuthenticatedHttpClient(
            session,
            consumer_key=app_key,
            consumer_secret=app_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

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
            'track': ','.join(track) if track is not None else '',
            'follow': ','.join(follow) if follow is not None else '',
            'locations': ','.join(locations) if locations is not None else '',
        }
        url = f'{URL_STREAM_1_1}/statuses/filter.json'
        async for message in self._client.stream(url, body):
            yield message

    async def sample(self) -> AsyncIterable:
        """Retrieve a sampling of public statuses"""
        url = f'{URL_STREAM_1_1}/statuses/sample.json'
        async for message in self._client.stream(url):
            yield message

    async def home_timeline(
            self,
            *,
            count: int = 20,
            since_id: Optional[int] = None,
            max_id: Optional[int] = None,
            trim_user: bool = True,
            exclude_replies: bool = True,
            include_entities: bool = False
    ):
        """Returns a collection of the most recent Tweets posted
        by the authenticating user and the users they follow."""
        body = {
            'count': count,
            'since_id': since_id,
            'max_id': max_id,
            'trim_user': 'true' if trim_user else 'false',
            'exclude_replies': 'true' if exclude_replies else 'false',
            'include_entities': 'true' if include_entities else 'false',
        }
        url = f'{URL_API_1_1}/statuses/home_timeline.json'
        return await self._client.get(url, body)

    async def user_timeline(
            self,
            *,
            user_id: Optional[str] = None,
            screen_name: Optional[str] = None,
            since_id: Optional[int] = None,
            count: Optional[int] = None,
            max_id: Optional[int] = None,
            trim_user: bool = True,
            exclude_replies: bool = True,
            include_rts: bool = False
    ):
        body = {
            'user_id': user_id,
            'screen_name': screen_name,
            'since_id': since_id,
            'count': count,
            'max_id': max_id,
            'trim_user': str(trim_user).lower(),
            'exclude_replies': str(exclude_replies).lower(),
            'include_rts': str(include_rts).lower(),
        }
        url = f'{URL_API_1_1}/statuses/user_timeline.json'
        return await self._client.get(url, body)

    async def mentions_timeline(
            self,
            *,
            count: Optional[int] = None,
            since_id: Optional[int] = None,
            max_id: Optional[int] = None,
            trim_user: bool = True,
            include_entities: bool = True
    ):
        body = {
            'count': count,
            'since_id': since_id,
            'max_id': max_id,
            'trim_user': str(trim_user).lower(),
            'include_entities': str(include_entities).lower(),
        }
        url = f'{URL_API_1_1}/statuses/mentions_timeline.json'
        return await self._client.get(url, body)

    async def account_settings(self):
        url = f'{URL_API_1_1}/account/settings.json'
        return await self._client.get(url)

    async def account_verify_credentials(
            self,
            include_entities: Optional[bool] = None,
            skip_status: Optional[bool] = None,
            include_email: Optional[bool] = None
    ):
        body = {
            'include_entities': include_entities,
            'skip_status': skip_status,
            'include_email': include_email
        }
        url = f'{URL_API_1_1}/account/verify_credentials.json'
        return await self._client.get(url, body)
