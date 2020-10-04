"""Support for status type messages"""

from typing import Any, List, Mapping, Optional, Union

from ..constants import URL_API_1_1
from ..types import AbstractHttpClient
from ..utils import optional_int_list_to_str


class Statuses:

    def __init__(self, client: AbstractHttpClient) -> None:
        self._client = client
        self._url = f'{URL_API_1_1}/statuses'

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
        url = f'{self._url}/home_timeline.json'
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
        url = f'{self._url}/user_timeline.json'
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
        url = f'{self._url}/mentions_timeline.json'
        return await self._client.get(url, body)

    async def update(
            self,
            status: str,
            *,
            in_reply_to_status_id: Optional[int] = None,
            auto_populate_reply_metadata: Optional[bool] = None,
            exclude_reply_user_ids: Optional[List[int]] = None,
            attachment_url: Optional[str] = None,
            media_ids: Optional[List[int]] = None,
            possibly_sensitive: Optional[bool] = None,
            lat: Optional[Union[int, float]] = None,
            long: Optional[Union[int, float]] = None,
            place_id: Optional[str] = None,
            display_coordinates: Optional[bool] = None,
            trim_user: Optional[bool] = None,
            enable_dmcommands: Optional[bool] = None,
            fail_dmcommands: Optional[bool] = None,
            card_uri: Optional[str] = None
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        body = {
            'status': status,
            'in_reply_to_status_id': in_reply_to_status_id,
            'auto_populate_reply_metadata': auto_populate_reply_metadata,
            'exclude_reply_user_ids': optional_int_list_to_str(exclude_reply_user_ids),
            'attachment_url': attachment_url,
            'media_ids': optional_int_list_to_str(media_ids),
            'possibly_sensitive': possibly_sensitive,
            'lat': lat,
            'long': long,
            'place_id': place_id,
            'display_coordinates': display_coordinates,
            'trim_user': trim_user,
            'enable_dmcommands': enable_dmcommands,
            'fail_dmcommands': fail_dmcommands,
            'card_uri': card_uri
        }
        url = f'{self._url}/update.json'
        return await self._client.post(url, body)
