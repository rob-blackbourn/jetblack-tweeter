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
    async def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        ...

    @abstractmethod
    async def get(
            self,
            url: str,
            headers: Mapping[str, str]
    ) -> Union[List[Any], Mapping[str, Any]]:
        ...

    @abstractmethod
    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        ...


class AbstractHttpClient(metaclass=ABCMeta):

    @ abstractmethod
    async def stream(
            self,
            url: str,
            data: Optional[Mapping[str, Any]] = None,
            method: str = 'post'
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        ...

    @ abstractmethod
    async def get(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None
    ) -> Union[List[Any], Mapping[str, Any]]:
        ...

    @ abstractmethod
    async def post(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        ...


class FilterLevel(Enum):
    NONE = 'none'
    LOW = 'low'
    MEDIUM = 'medium'


class UserObject(TypedDict, total=False):
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
    coordinates: Location
    type: str


class TweetObject(TypedDict, total=False):
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
