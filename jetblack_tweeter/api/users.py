"""Support for the v2 users endpoint"""

from datetime import datetime
from typing import Any, Literal, Optional, Sequence

from ..types import AbstractHttpClient

from ..constants import URL_API_2
from ..types import (
    MediaFields,
    PollFields,
    TweetFields,
    UserFields,
    PlaceFields
)
from ..utils import (
    optional_str_list_to_str,
    str_list_to_str,
    optional_datetime_to_str
)


class Users:
    """Support for the v2 users endpoint"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the users end point.

        Args:
            client (AbstractHttpClient): THe authenticated HTTP client
        """
        self._client = client
        self._url = f'{URL_API_2}/users'

    async def liked_tweets(
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
            max_requests: Optional[int] = None,
            media_fields: Optional[Sequence[MediaFields]] = None,
            pagination_token: Optional[str] = None,
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """Gets information about liked tweets.

        Args:
            id (str): User ID of the user to request liked Tweets for.
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
                objects that relate to the originally returned Tweets. Defaults
                to None.
            max_requests (Optional[int], optional): The maximum number of
                results to be returned per page. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
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
            Any: The tweet likes.
        """
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
        """Lookup users by their ids.

        Args:
            ids (Sequence[str]): The ids for the users.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: Information on the users.
        """
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
        """Lookup a user by their id.

        Args:
            id (str): The id of the user.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: Information about the user.
        """
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
        """Lookup users by their usernames.

        Args:
            usernames (Sequence[str]): The usernames.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: Information about the users.
        """
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
        """Lookup a user by their username.

        Args:
            username (str): The username.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: Information about the user.
        """
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
        """Lookup information about the authenticated user.

        Args:
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: The user information.
        """
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
        """Returns a list of users the specified user ID is following.

        Args:
            id (str): The user ID whose following you would like to retrieve.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            max_requests (Optional[int], optional): The maximum number of
                results to be returned per page. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: A list of users the specified user ID is following.
        """
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
        """Returns a list of users who are followers of the specified user ID.

        Args:
            id (str): The user ID whose followers you would like to retrieve.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            max_requests (Optional[int], optional): The maximum number of
                results to be returned per page. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: _description_
        """
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
        """Allows a user ID to follow another user.

        Args:
            id (str): The authenticated user ID who you would like to initiate
                the follow on behalf of.
            target_user_id (str): The user ID of the user that you would like
                the id to follow.

        Returns:
            Any: The status of the request.
        """
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
        """Allows a user ID to unfollow another user.

        Args:
            source_user_id (str): The user ID who you would like to initiate the
                unfollow on behalf of.
            target_user_id (str): The user ID of the user that you would like
                the source_user_id to unfollow.

        Returns:
            Any: The status of the request.
        """
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
        """Returns a list of users who are blocked by the specified user ID.

        Args:
            id (str): The user ID whose blocked users you would like to retrieve.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            max_requests (Optional[int], optional): The maximum number of
                results to be returned per page. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: A list of users.
        """
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
        """Block a user.

        Args:
            id (str): 	The user ID who you would like to initiate the block on
                behalf of.
            target_user_id (str): The user ID of the user that you would like
                the id to block.

        Returns:
            Any: The status of the request.
        """
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
        """Unblock a user.

        Args:
            source_user_id (str): The user ID who you would like to initiate an
                unblock on behalf of.
            target_user_id (str): The user ID of the user that you would like
                the source_user_id to unblock.

        Returns:
            Any: The status of the request.
        """
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
        """Returns a list of users who are muted by the specified user ID.

        Args:
            id (str): The user ID whose muted users you would like to retrieve.
            expansions (Optional[Sequence[Literal[
                &quot;pinned_tweet_id&quot;
                ]]], optional): Expansions enable you to request additional data
                objects that relate to the originally returned users. Defaults
                to None.
            max_requests (Optional[int], optional): The maximum number of
                results to be returned per page. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: A list of users.
        """
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
        """Mute a user.

        Args:
            id (str): 	The user ID who you would like to initiate the mute on
                behalf of.
            target_user_id (str): The user ID of the user that you would like
                the id to mute.

        Returns:
            Any: The status of the request.
        """
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
        """Unmute a user.

        Args:
            source_user_id (str): The user ID who you would like to initiate an
                unmute on behalf of.
            target_user_id (str): The user ID of the user that you would like
                the source_user_id to unmute.

        Returns:
            Any: The status of the request.
        """
        url = f'{self._url}/{source_user_id}/blocking/{target_user_id}'
        return await self._client.delete(url, None)

    async def timeline(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            end_time: Optional[datetime] = None,
            exclude: Optional[Sequence[Literal[
                "retweets",
                "replies"
            ]]] = None,
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
            max_results: Optional[int] = None,
            media_fields: Optional[MediaFields] = None,
            pagination_token: Optional[str] = None,
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            since_id: Optional[str] = None,
            start_time: Optional[datetime] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            until_id: Optional[str] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """Returns Tweets composed by a single user, specified by the requested
        user ID.

        By default, the most recent ten Tweets are returned per request. Using
        pagination, the most recent 3,200 Tweets can be retrieved.

        Args:
            id (str): _description_
            redefined (_type_): Unique identifier of the Twitter account (user
                ID) for whom to return results.
            end_time (Optional[datetime], optional): The newest or most recent 
                timestamp from which the Tweets will be provided. Defaults to
                None.
            exclude (Optional[Sequence[Literal[
                &quot;retweets&quot;,
                &quot;replies&quot;
                ]]], optional): _description_. Defaults to None.
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
                objects that relate to the originally returned Tweets.. Defaults
                to None.
            max_results (Optional[int], optional): Tweets to exclude from the
                response. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            place_fields (Optional[Sequence[PlaceFields]], optional): This
                fields parameter enables you to select which specific place
                fields will deliver in each returned Tweet. Defaults to None.
            poll_fields (Optional[Sequence[PollFields]], optional): This fields
                parameter enables you to select which specific poll fields will
                deliver in each returned Tweet. Defaults to None.
            since_id (Optional[str], optional): Returns results with a Tweet ID
                greater than (that is, more recent than) the specified 'since'
                Tweet ID. Defaults to None.
            start_time (Optional[datetime], optional): The oldest or earliest
                timestamp from which the Tweets will be provided.. Defaults to
                None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            until_id (Optional[str], optional): Returns results with a Tweet ID
                less than (that is, older than) the specified 'until' Tweet ID.
                Defaults to None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: The tweets.
        """
        body = {
            'end_time': optional_datetime_to_str(end_time),
            'exclude': optional_str_list_to_str(exclude),
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'media.fields': optional_str_list_to_str(media_fields),
            'pagination_token': pagination_token,
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'since_id': since_id,
            'start_time': optional_datetime_to_str(start_time),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'until_id': until_id,
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/tweets'
        return await self._client.get(url, body)

    async def mentions(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            end_time: Optional[datetime] = None,
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
            max_results: Optional[int] = None,
            media_fields: Optional[MediaFields] = None,
            pagination_token: Optional[str] = None,
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            since_id: Optional[str] = None,
            start_time: Optional[datetime] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            until_id: Optional[str] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """ the requested user ID.

        Args:
            id (str): Unique identifier of the user for whom to return Tweets mentioning the user.
            end_time (Optional[datetime], optional): The newest or most recent 
                timestamp from which the Tweets will be provided. Defaults to
                None.
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
                objects that relate to the originally returned Tweets.. Defaults
                to None.
            max_results (Optional[int], optional): Tweets to exclude from the
                response. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            place_fields (Optional[Sequence[PlaceFields]], optional): This
                fields parameter enables you to select which specific place
                fields will deliver in each returned Tweet. Defaults to None.
            poll_fields (Optional[Sequence[PollFields]], optional): This fields
                parameter enables you to select which specific poll fields will
                deliver in each returned Tweet. Defaults to None.
            since_id (Optional[str], optional): Returns results with a Tweet ID
                greater than (that is, more recent than) the specified 'since'
                Tweet ID. Defaults to None.
            start_time (Optional[datetime], optional): The oldest or earliest
                timestamp from which the Tweets will be provided.. Defaults to
                None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            until_id (Optional[str], optional): Returns results with a Tweet ID
                less than (that is, older than) the specified 'until' Tweet ID.
                Defaults to None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: _description_
        """
        body = {
            'end_time': optional_datetime_to_str(end_time),
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'media.fields': optional_str_list_to_str(media_fields),
            'pagination_token': pagination_token,
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'since_id': since_id,
            'start_time': optional_datetime_to_str(start_time),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'until_id': until_id,
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/mentions'
        return await self._client.get(url, body)

    async def timeline_reverse_chronological(
            self,
            id: str,  # pylint: disable=invalid-name,redefined-builtin
            *,
            end_time: Optional[datetime] = None,
            exclude: Optional[Sequence[Literal[
                "retweets",
                "replies"
            ]]] = None,
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
            max_results: Optional[int] = None,
            media_fields: Optional[MediaFields] = None,
            pagination_token: Optional[str] = None,
            place_fields: Optional[Sequence[PlaceFields]] = None,
            poll_fields: Optional[Sequence[PollFields]] = None,
            since_id: Optional[str] = None,
            start_time: Optional[datetime] = None,
            tweet_fields: Optional[Sequence[TweetFields]] = None,
            until_id: Optional[str] = None,
            user_fields: Optional[Sequence[UserFields]] = None
    ) -> Any:
        """Allows you to retrieve a collection of the most recent Tweets and
        Retweets posted by you and users you follow. 

        Args:
            id (str): _description_
            redefined (_type_): Unique identifier of the Twitter account (user
                ID) for whom to return results.
            end_time (Optional[datetime], optional): The newest or most recent 
                timestamp from which the Tweets will be provided. Defaults to
                None.
            exclude (Optional[Sequence[Literal[
                &quot;retweets&quot;,
                &quot;replies&quot;
                ]]], optional): _description_. Defaults to None.
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
                objects that relate to the originally returned Tweets.. Defaults
                to None.
            max_results (Optional[int], optional): Tweets to exclude from the
                response. Defaults to None.
            media_fields (Optional[Sequence[MediaFields]], optional): This
                fields parameter enables you to select which specific media
                fields will deliver in each returned Tweet. Defaults to None.
            pagination_token (Optional[str], optional): Used to request the next
                page of results if all results weren't returned with the latest
                request, or to go back to the previous page of results. Defaults
                to None.
            place_fields (Optional[Sequence[PlaceFields]], optional): This
                fields parameter enables you to select which specific place
                fields will deliver in each returned Tweet. Defaults to None.
            poll_fields (Optional[Sequence[PollFields]], optional): This fields
                parameter enables you to select which specific poll fields will
                deliver in each returned Tweet. Defaults to None.
            since_id (Optional[str], optional): Returns results with a Tweet ID
                greater than (that is, more recent than) the specified 'since'
                Tweet ID. Defaults to None.
            start_time (Optional[datetime], optional): The oldest or earliest
                timestamp from which the Tweets will be provided.. Defaults to
                None.
            tweet_fields (Optional[Sequence[TweetFields]], optional): This
                fields parameter enables you to select which specific Tweet
                fields will deliver in each returned Tweet object. Defaults to
                None.
            until_id (Optional[str], optional): Returns results with a Tweet ID
                less than (that is, older than) the specified 'until' Tweet ID.
                Defaults to None.
            user_fields (Optional[Sequence[UserFields]], optional): This fields
                parameter enables you to select which specific user fields will
                deliver in each returned Tweet. Defaults to None.

        Returns:
            Any: The tweets.
        """
        body = {
            'end_time': optional_datetime_to_str(end_time),
            'exclude': optional_str_list_to_str(exclude),
            'expansions': optional_str_list_to_str(expansions),
            'max_result': max_results,
            'media.fields': optional_str_list_to_str(media_fields),
            'pagination_token': pagination_token,
            'place.fields': optional_str_list_to_str(place_fields),
            'poll.fields': optional_str_list_to_str(poll_fields),
            'since_id': since_id,
            'start_time': optional_datetime_to_str(start_time),
            'tweet.fields': optional_str_list_to_str(tweet_fields),
            'until_id': until_id,
            'user.fields': optional_str_list_to_str(user_fields),
        }
        url = f'{self._url}/{id}/timelines/reverse_chronological'
        return await self._client.get(url, body)
