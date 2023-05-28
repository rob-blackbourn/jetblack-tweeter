"""Support for the v2 users endpoint"""

from typing import Any, Literal, Optional, Sequence
from ..types import AbstractHttpClient

from ..constants import URL_API_2
from ..utils import optional_str_list_to_str, str_list_to_str

MediaFields = Literal[
    "duration_ms",
    "height",
    'media_key',
    "preview_image_url",
    "type",
    "url",
    "width",
    "public_metrics",
    "non_public_metrics",
    "organic_metrics",
    "promoted_metrics",
    "alt_text",
    "variants"
]
PollFields = Literal[
    "duration_minutes",
    "end_datetime",
    "id",
    "options",
    "voting_status"
]
TweetFields = Literal[
    "attachments",
    "author_id",
    "context_annotations",
    "conversation_id",
    "created_at",
    "edit_controls",
    "entities",
    "geo",
    "id",
    "in_reply_to_user_id",
    "lang",
    "non_public_metrics",
    "public_metrics",
    "organic_metrics",
    "promoted_metrics",
    "possibly_sensitive",
    "referenced_tweets",
    "reply_settings",
    "source",
    "text",
    "withheld"
]
UserFields = Literal[
    "created_at",
    "description",
    "entities",
    "id",
    "location",
    "name",
    "pinned_tweet_id",
    "profile_image_url",
    "protected",
    "public_metrics",
    "url",
    "username",
    "verified",
    "verified_type",
    "withheld"

]


class Users:
    """Support for the v2 users endpoint"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the statuses end point.

        Args:
            client (AbstractHttpClient): THe authenticated HTTP client
        """
        self._client = client
        self._url = f'{URL_API_2}/users'

    async def liked_tweets(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            max_requests: Optional[int] = None,
            expansions: Optional[Sequence[Literal[
                "attachments.poll_ids",
                "attachments.media_keys",
                "author_id",
                "edit_history_tweet_ids",
                "entities.mentions.username",
                "geo.place_id",
                "in_reply_to_user_id",
                "referenced_tweets.id",
                "referenced_tweets.id.author_id"
            ]]] = None,
            media_fields: Optional[Sequence[MediaFields]] = None,
            pagination_token: Optional[str] = None,
            place_fields: Optional[Sequence[Literal[
                "contained_within",
                "country",
                "country_code",
                "full_name",
                "geo",
                "id",
                "name",
                "place_type"
            ]]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'max_requests': max_requests,
            'expansions': optional_str_list_to_str(expansions),
            'media.fields': optional_str_list_to_str(media_fields),
            "pagination_token": pagination_token,
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/liked_tweets'
        return await self._client.get(url, body)

    async def lookup_by_ids(
            self,
            ids: Sequence[str],
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'ids': str_list_to_str(ids),
            'expansions': optional_str_list_to_str(expansions),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        return await self._client.get(self._url, body)

    async def lookup_by_id(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}'
        return await self._client.get(url, body)

    async def lookup_by_usernames(
            self,
            usernames: Sequence[str],
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'usernames': str_list_to_str(usernames),
            'expansions': optional_str_list_to_str(expansions),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/by'
        return await self._client.get(url, body)

    async def lookup_by_username(
            self,
            username: str,
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/by/username/{username}'
        return await self._client.get(url, body)

    async def me(
            self,
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/me'
        return await self._client.get(url, body)

    async def following(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            max_results: Optional[int] = None,
            pagination_token: Optional[str] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'pagination_token': pagination_token,
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/following'
        return await self._client.get(url, body)

    async def followers(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            max_results: Optional[int] = None,
            pagination_token: Optional[str] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'pagination_token': pagination_token,
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/followers'
        return await self._client.get(url, body)

    async def follow(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            target_user_id: str
    ) -> Any:
        body = {
            'target_user_id': target_user_id,
        }
        url = f'{self._url}/{id}/following'
        return await self._client.put(url, body)

    async def unfollow(
            self,
            source_user_id: str,
            target_user_id: str
    ) -> Any:
        url = f'{self._url}/{source_user_id}/following/{target_user_id}'
        return await self._client.delete(url, None)

    async def blocking(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            max_results: Optional[int] = None,
            pagination_token: Optional[str] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'pagination_token': pagination_token,
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/blocking'
        return await self._client.get(url, body)

    async def block(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            target_user_id: str
    ) -> Any:
        body = {
            'target_user_id': target_user_id,
        }
        url = f'{self._url}/{id}/blocking'
        return await self._client.put(url, body)

    async def unblock(
            self,
            source_user_id: str,
            target_user_id: str
    ) -> Any:
        url = f'{self._url}/{source_user_id}/blocking/{target_user_id}'
        return await self._client.delete(url, None)

    async def muting(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            expansions: Optional[Sequence[Literal[
                "pinned_tweet_id"
            ]]] = None,
            max_results: Optional[int] = None,
            pagination_token: Optional[str] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'pagination_token': pagination_token,
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/muting'
        return await self._client.get(url, body)

    async def mute(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            target_user_id: str
    ) -> Any:
        body = {
            'target_user_id': target_user_id,
        }
        url = f'{self._url}/{id}/mute'
        return await self._client.put(url, body)

    async def unmute(
            self,
            source_user_id: str,
            target_user_id: str
    ) -> Any:
        url = f'{self._url}/{source_user_id}/blocking/{target_user_id}'
        return await self._client.delete(url, None)
