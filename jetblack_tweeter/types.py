"""The HTTP client session"""

from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import (
    Any,
    AsyncIterator,
    List,
    Mapping,
    Optional,
    TypedDict,
    Tuple,
    Union
)


Number = Union[float, int]
Location = Tuple[Number, Number]
BoundingBox = Tuple[Location, Location]


class AbstractTweeterSession(metaclass=ABCMeta):
    """The abstract class for Tweeter sessions.

    Implement this class to provide clients for the http library of your choice.
    """

    @abstractmethod
    def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        """Stream data

        Args:
            url (str): The url
            method (str): The HTTP method
            headers (Mapping[str, str]): The HTTP headers
            body (Optional[str]): The body (if any)

        Returns:
            AsyncIterator[Union[List[Any], Mapping[str, Any]]]: An async
                iterator of the unpacked JSON message.
        """

    @abstractmethod
    async def get(
            self,
            url: str,
            headers: Mapping[str, str],
            timeout: Optional[float]
    ) -> Union[List[Any], Mapping[str, Any]]:
        """Get data from Twitter

        Args:
            url (str): The url
            headers (Mapping[str, str]): The HTTP headers.
            timeout (Optional[float]): An optional timeout.

        Returns:
            Union[List[Any], Mapping[str, Any]]: The unpacked JSON response.
        """

    @abstractmethod
    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str],
            timeout: Optional[float]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        """Post data to Twitter

        Args:
            url (str): The url
            headers (Mapping[str, str]): The HTTP headers.
            body (Optional[str]): The body (if any).
            timeout (Optional[float]): An optional timeout.

        Returns:
            Optional[Union[List[Any], Mapping[str, Any]]]: The unpacked JSON
                response (if any).
        """

    @abstractmethod
    async def close(self) -> None:
        """Close the connection.
        """


class AbstractHttpClient(metaclass=ABCMeta):
    """The abstract class for HTTP clients.
    """

    @abstractmethod
    def stream(
            self,
            url: str,
            data: Optional[Mapping[str, Any]] = None,
            method: str = 'post'
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        """Stream data from Twitter

        Args:
            url (str): The url
            data (Optional[Mapping[str, Any]], optional): The data. Defaults to
                None.
            method (str, optional): The HTTP method. Defaults to 'post'.

        Returns:
            Coroutine[Any, Any, AsyncIterator[Union[List[Any], Mapping[str, Any]]]]: An async
                iterator of unpacked JSON responses.
        """

    @ abstractmethod
    async def get(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None
    ) -> Union[List[Any], Mapping[str, Any]]:
        """Gets data from Twitter.

        Args:
            url (str): The url.
            params (Optional[Mapping[str, Any]], optional): The parameters if
                any. Defaults to None.
            timeout (Optional[float], optional): The timeout if any. Defaults
                to None.

        Returns:
            Union[List[Any], Mapping[str, Any]]: The unpacked JSON response.
        """

    @ abstractmethod
    async def post(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        """Post data to Twitter.

        Args:
            url (str): The url
            params (Optional[Mapping[str, Any]], optional): The parameters if
                any. Defaults to None.
            timeout (Optional[float], optional): The timeout if any. Defaults
                to None.

        Returns:
            Optional[Union[List[Any], Mapping[str, Any]]]: The unpacked JSON
                response if any
        """

    @abstractmethod
    async def close(self) -> None:
        """Close the connection.
        """


class FilterLevel(Enum):
    """The filter level for streaming queries
    """
    NONE = 'none'
    LOW = 'low'
    MEDIUM = 'medium'


class SearchResultType(Enum):
    """Specifies what type of search results you would prefer to receive."""
    MIXED = 'mixed'
    RECENT = 'recent'
    POPULAR = 'popular'


class Alignment(Enum):
    """Tweet alignment"""
    NONE = 'none'
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'


class Theme(Enum):
    """Tweet display theme"""
    LIGHT = 'light'
    DARK = 'dark'


class WidgetType(Enum):
    """The widget type"""
    VIDEO = 'video'


class UserObject(TypedDict, total=False):
    """The UserObject response"""
    id: int
    id_str: str
    name: str
    screen_name: str
    location: Optional[str]
    derived: Mapping[str, Any]
    url: Optional[str]
    description: Optional[str]
    protected: bool
    verified: bool
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: str
    profile_banner_url: str
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool
    withheld_in_countries: Optional[List[str]]
    withheld_scope: Optional[str]


class CoordinatesObject(TypedDict, total=False):
    """The coordinates object response"""
    coordinates: Location
    type: str


class TweetObject(TypedDict, total=False):
    """The tweet object response"""
    created_at: str
    id: str
    id_str: str
    text: str
    source: str
    truncated: bool
    in_reply_to_status_id: Optional[int]
    in_reply_to_status_id_str: Optional[str]
    in_reply_to_user_id: Optional[int]
    in_reply_to_user_id_str: Optional[str]
    in_reply_to_screen_name: Optional[str]
    user: UserObject
    coordinates: CoordinatesObject
