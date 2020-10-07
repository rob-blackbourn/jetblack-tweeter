"""Support for status type messages"""

from typing import Any, List, Mapping, Optional, Union

from ..constants import URL_API_1_1
from ..types import AbstractHttpClient
from ..utils import (
    optional_bool_to_str,
    int_list_to_str,
    optional_int_list_to_str,
    bool_to_str
)


class Statuses:
    """Support for the statuses end point"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the statuses end point.

        Args:
            client (AbstractHttpClient): THe authenticated HTTP client
        """
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
        """Returns a collection of the most recent Tweets and Retweets posted by
        the authenticating user and the users they follow. The home timeline is
        central to how most users interact with the Twitter service.

        Args:
            count (int, optional): Specifies the number of records to retrieve.
                Must be less than or equal to 200. Defaults to 20. The value of
                count is best thought of as a limit to the number of tweets to
                return because suspended or deleted content is removed after the
                count has been applied. Defaults to 20.
            since_id (Optional[int], optional): Returns results with an ID
                greater than (that is, more recent than) the specified ID. There
                are limits to the number of Tweets which can be accessed through
                the API. If the limit of Tweets has occurred since the since_id,
                the since_id will be forced to the oldest ID available. Defaults
                to None.
            max_id (Optional[int], optional): Returns results with an ID less
                than (that is, older than) or equal to the specified ID.
                Defaults to None.
            trim_user (bool, optional): When true each Tweet returned in a
                timeline will include a user object including only the status
                authors numerical ID. Omit this parameter to receive the
                complete user object. Defaults to True.
            exclude_replies (bool, optional): This parameter will prevent
                replies from appearing in the returned timeline. Using
                exclude_replies with the count parameter will mean you will
                receive up-to count Tweets — this is because the count parameter
                retrieves that many Tweets before filtering out retweets and
                replies. Defaults to True.
            include_entities (bool, optional): The entities node will not be
                included when set to false. Defaults to False.

        Returns:
            Mapping[str, Any]: The user timeline.
        """
        body = {
            'count': count,
            'since_id': since_id,
            'max_id': max_id,
            'trim_user': bool_to_str(trim_user),
            'exclude_replies': bool_to_str(exclude_replies),
            'include_entities': bool_to_str(include_entities),
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
        """Returns a collection of the most recent Tweets posted by the user
        indicated by the screen_name or user_id parameters.

        Args:
            user_id (Optional[str], optional): The ID of the user for whom to
                return results. Defaults to None.
            screen_name (Optional[str], optional): The screen name of the user
                for whom to return results. Defaults to None.
            since_id (Optional[int], optional): Returns results with an ID
                greater than (that is, more recent than) the specified ID. There
                are limits to the number of Tweets that can be accessed through
                the API. If the limit of Tweets has occurred since the
                since_id, the since_id will be forced to the oldest ID
                available. Defaults to None.
            count (Optional[int], optional): Specifies the number of Tweets to
                try and retrieve, up to a maximum of 200 per distinct request.
                The value of count is best thought of as a limit to the number
                of Tweets to return because suspended or deleted content is
                removed after the count has been applied. We include retweets in
                the count, even if include_rts is not supplied. It is
                recommended you always send include_rts=1 when using this API
                method. Defaults to None.
            max_id (Optional[int], optional): Returns results with an ID less
                than (that is, older than) or equal to the specified ID.
                Defaults to None.
            trim_user (bool, optional): When set to true each Tweet returned in
                a timeline will include a user object including only the status
                authors numerical ID. Omit this parameter to receive the
                complete user object. Defaults to True.
            exclude_replies (bool, optional): This parameter will prevent
                replies from appearing in the returned timeline. Using
                exclude_replies with the count parameter will mean you will
                receive up-to count tweets — this is because the count parameter
                retrieves that many Tweets before filtering out retweets and
                replies. Defaults to True.
            include_rts (bool, optional): When set to false , the timeline will
                strip any native retweets (though they will still count toward
                both the maximal length of the timeline and the slice selected
                by the count parameter). Note: If you're using the trim_user
                parameter in conjunction with include_rts, the retweets will
                still contain a full user object. Defaults to False.

        Returns:
            List[Mapping[str, Any]]: The user timeline.
        """
        body = {
            'user_id': user_id,
            'screen_name': screen_name,
            'since_id': since_id,
            'count': count,
            'max_id': max_id,
            'trim_user': bool_to_str(trim_user),
            'exclude_replies': bool_to_str(exclude_replies),
            'include_rts': bool_to_str(include_rts),
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
    ) -> List[Mapping[str, Any]]:
        """Returns the 20 most recent mentions (Tweets containing a users's
        @screen_name) for the authenticating user.



        Args:
            count (Optional[int], optional): Specifies the number of Tweets to
                try and retrieve, up to a maximum of 200. The value of count is
                best thought of as a limit to the number of tweets to return
                because suspended or deleted content is removed after the count
                has been applied. We include retweets in the count, even if
                include_rts is not supplied. It is recommended you always send
                include_rts=1 when using this API method.. Defaults to None.
            since_id (Optional[int], optional): Returns results with an ID
                greater than (that is, more recent than) the specified ID. There
                are limits to the number of Tweets which can be accessed through
                the API. If the limit of Tweets has occurred since the since_id,
                the since_id will be forced to the oldest ID available. Defaults
                to None.
            max_id (Optional[int], optional): Returns results with an ID less
                than (that is, older than) or equal to the specified ID.
                Defaults to None.
            trim_user (bool, optional): When true each tweet returned in a
                timeline will include a user object including only the status
                authors numerical ID. Omit this parameter to receive the
                complete user object. Defaults to True.
            include_entities (bool, optional): The entities node will not be
                included when set to false. Defaults to True.

        Returns:
            List[Mapping[str, Any]]: The mentions timeline.
        """
        body = {
            'count': count,
            'since_id': since_id,
            'max_id': max_id,
            'trim_user': bool_to_str(trim_user),
            'include_entities': bool_to_str(include_entities),
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
    ) -> Optional[Mapping[str, Any]]:
        """Updates the authenticating user's current status, also known as
        Tweeting.

        Args:
            status (str): The text of the status update. URL encode as
                necessary. t.co link wrapping will affect character counts.
            in_reply_to_status_id (Optional[int], optional): The ID of an
                existing status that the update is in reply to. Note: This
                parameter will be ignored unless the author of the Tweet this
                parameter references is mentioned within the status text.
                Therefore, you must include @username , where username is the
                author of the referenced Tweet, within the update. Defaults to
                None.
            auto_populate_reply_metadata (Optional[bool], optional): If set to
                true and used with in_reply_to_status_id, leading @mentions will
                be looked up from the original Tweet, and added to the new Tweet
                from there. This wil append @mentions into the metadata of an
                extended Tweet as a reply chain grows, until the limit on
                @mentions is reached. In cases where the original Tweet has been
                deleted, the reply will fail. Defaults to None.
            exclude_reply_user_ids (Optional[List[int]], optional): When used
                with auto_populate_reply_metadata, a comma-separated list of
                user ids which will be removed from the server-generated
                @mentions prefix on an extended Tweet. Note that the leading
                @mention cannot be removed as it would break the
                in-reply-to-status-id semantics. Attempting to remove it will be
                silently ignored. Defaults to None.
            attachment_url (Optional[str], optional): In order for a URL to not
                be counted in the status body of an extended Tweet, provide a
                URL as a Tweet attachment. This URL must be a Tweet permalink,
                or Direct Message deep link. Arbitrary, non-Twitter URLs must
                remain in the status text. URLs passed to the attachment_url
                parameter not matching either a Tweet permalink or Direct
                Message deep link will fail at Tweet creation and cause an
                exception. Defaults to None.
            media_ids (Optional[List[int]], optional): A comma-delimited list of
                media_ids to associate with the Tweet. You may include up to 4
                photos or 1 animated GIF or 1 video in a Tweet. See Uploading
                Media for further details on uploading media. Defaults to None.
            possibly_sensitive (Optional[bool], optional): If you upload Tweet
                media that might be considered sensitive content such as nudity,
                or medical procedures, you must set this value to true. See
                Media setting and best practices for more context. Defaults to
                None.
            lat (Optional[Union[int, float]], optional): The latitude of the
                location this Tweet refers to. This parameter will be ignored
                unless it is inside the range -90.0 to +90.0 (North is positive)
                inclusive. It will also be ignored if there is no corresponding
                long parameter. Defaults to None.
            long (Optional[Union[int, float]], optional): The longitude of the
                location this Tweet refers to. The valid ranges for longitude
                are -180.0 to +180.0 (East is positive) inclusive. This
                parameter will be ignored if outside that range, if it is not a
                number, if geo_enabled is disabled, or if there no corresponding
                lat parameter. Defaults to None.
            place_id (Optional[str], optional): A place in the world. Defaults
                to None.
            display_coordinates (Optional[bool], optional): Whether or not to
                put a pin on the exact coordinates a Tweet has been sent from.
                Defaults to None.
            trim_user (Optional[bool], optional): When true the response will
                include a user object including only the author's ID. Omit this
                parameter to receive the complete user object. Defaults to None.
            enable_dmcommands (Optional[bool], optional): When set to true,
                enables shortcode commands for sending Direct Messages as part
                of the status text to send a Direct Message to a user. When set
                to false, disables this behavior and includes any leading
                characters in the status text that is posted. Defaults to None.
            fail_dmcommands (Optional[bool], optional): When set to true, causes
                any status text that starts with shortcode commands to return an
                API error. When set to false, allows shortcode commands to be
                sent in the status text and acted on by the API. Defaults to
                None.
            card_uri (Optional[str], optional): Associate an ads card with the
                Tweet using the card_uri value from any ads card response.
                Defaults to None.

        Returns:
            Optional[Mapping[str, Any]]: The tweet.
        """
        body = {
            'status': status,
            'in_reply_to_status_id': in_reply_to_status_id,
            'auto_populate_reply_metadata': optional_bool_to_str(auto_populate_reply_metadata),
            'exclude_reply_user_ids': optional_int_list_to_str(exclude_reply_user_ids),
            'attachment_url': attachment_url,
            'media_ids': optional_int_list_to_str(media_ids),
            'possibly_sensitive': optional_bool_to_str(possibly_sensitive),
            'lat': lat,
            'long': long,
            'place_id': place_id,
            'display_coordinates': display_coordinates,
            'trim_user': optional_bool_to_str(trim_user),
            'enable_dmcommands': optional_bool_to_str(enable_dmcommands),
            'fail_dmcommands': optional_bool_to_str(fail_dmcommands),
            'card_uri': card_uri
        }
        url = f'{self._url}/update.json'
        return await self._client.post(url, body)

    async def lookup(
            self,
            ids: List[int],
            *,
            include_entities: Optional[bool] = None,
            trim_user: Optional[bool] = None,
            map: Optional[bool] = None,
            include_ext_alt_text: Optional[bool] = None,
            include_card_uri: Optional[bool] = None
    ) -> List[Mapping[str, Any]]:
        """Returns fully-hydrated Tweet objects for up to 100 Tweets per
        request, as specified by comma-separated values passed to the ids
        parameter.

        Args:
            ids (List[int]): A list of Tweet IDs, up to 100 are allowed in a
                single request.
            include_entities (Optional[bool], optional): The entities node that
                may appear within embedded statuses will not be included when
                set to false. Defaults to None.
            trim_user (Optional[bool], optional): When set to true each Tweet
                returned in a timeline will include a user object including only
                the status authors numerical ID. Omit this parameter to receive
                the complete user object. Defaults to None.
            map (Optional[bool], optional): When using the map parameter, Tweets
                that do not exist or cannot be viewed by the current user will
                still have their key represented but with an explicitly null
                value paired with it. Defaults to None.
            include_ext_alt_text (Optional[bool], optional): If alt text has
                been added to any attached media entities, this parameter will
                return an ext_alt_text value in the top-level key for the media
                entity. If no value has been set, this will be returned as null.
                Defaults to None.
            include_card_uri (Optional[bool], optional): When set to true each
                Tweet returned will include a card_uri attribute when there is
                an ads card attached to the Tweet and when that card was
                attached using the card_uri value. Defaults to None.

        Returns:
            List[Mapping[str, Any]]: A list of tweets.
        """
        body = {
            'id': int_list_to_str(ids),
            'include_entities': include_entities,
            'trim_user': optional_bool_to_str(trim_user),
            'map': optional_bool_to_str(map),
            'include_ext_alt_text': optional_bool_to_str(include_ext_alt_text),
            'include_card_uri': optional_bool_to_str(include_card_uri)
        }
        url = f'{self._url}/lookup.json'
        return await self._client.get(url, body)
