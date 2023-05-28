"""Tweets"""

from typing import Any, Literal, Optional, Sequence
from ..types import AbstractHttpClient

from ..constants import URL_API_2
from ..types import (
    MediaFields,
    PlaceFields,
    PollFields,
    TweetFields,
    UserFields
)
from ..utils import optional_str_list_to_str, str_list_to_str


class Tweets:
    """Support for the v2 tweets endpoint"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the users end point.

        Args:
            client (AbstractHttpClient): THe authenticated HTTP client
        """
        self._client = client
        self._url = f'{URL_API_2}/tweets'

    async def lookup(
            self,
            ids: Sequence[str],
            *,
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
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """Returns a variety of information about the Tweet specified by the
        requested ID or list of IDs.

        Args:
            ids (Sequence[str]): Tweet ids.
            expansions (Optional[Sequence[Literal[
                &quot;attachments.poll_ids&quot;,
                &quot;attachments.media_keys&quot;,
                &quot;author_id&quot;,
                &quot;edit_history_tweet_ids&quot;,
                &quot;entities.mentions.username&quot;,
                &quot;geo.place_id&quot;,
                &quot;in_reply_to_user_id&quot;,
                &quot;referenced_tweets.id&quot;,
                &quot;referenced_tweets.id.author_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned Tweets. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            place_fields (Optional[Sequence[PlaceFields]], optional): This
                fields parameter enables you to select which specific place
                fields will deliver in each returned Tweet. Defaults to None.
            poll_fields (Optional[Sequence[PollFields]], optional): This fields
                parameter enables you to select which specific poll fields will
                deliver in each returned Tweet. Defaults to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: The tweets.
        """
        body = {
            'ids': str_list_to_str(ids),
            'expansions': optional_str_list_to_str(expansions),
            'media.fields': optional_str_list_to_str(media_fields),
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        return await self._client.get(self._url, body)

    async def lookup_by_id(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
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
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """Returns a variety of information about the Tweet specified by the
        requested ID or list of IDs.

        Args:
            id (str): Unique identifier of the Tweet to request.
            expansions (Optional[Sequence[Literal[
                &quot;attachments.poll_ids&quot;,
                &quot;attachments.media_keys&quot;,
                &quot;author_id&quot;,
                &quot;edit_history_tweet_ids&quot;,
                &quot;entities.mentions.username&quot;,
                &quot;geo.place_id&quot;,
                &quot;in_reply_to_user_id&quot;,
                &quot;referenced_tweets.id&quot;,
                &quot;referenced_tweets.id.author_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned Tweets. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            place_fields (Optional[Sequence[PlaceFields]], optional): This
                fields parameter enables you to select which specific place
                fields will deliver in each returned Tweet. Defaults to None.
            poll_fields (Optional[Sequence[PollFields]], optional): This fields
                parameter enables you to select which specific poll fields will
                deliver in each returned Tweet. Defaults to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: The tweets.
        """
        body = {
            'expansions': optional_str_list_to_str(expansions),
            'media.fields': optional_str_list_to_str(media_fields),
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}'
        return await self._client.get(url, body)
