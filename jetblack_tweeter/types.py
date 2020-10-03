"""The HTTP client session"""

from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Any, AsyncIterator, List, Mapping, Optional, Union


class AbstractTweeterSession(metaclass=ABCMeta):

    @abstractmethod
    async def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        ...

    @ abstractmethod
    async def get(
            self,
            url: str,
            headers: Mapping[str, str]
    ) -> Union[List[Any], Mapping[str, Any]]:
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


class FilterLevel(Enum):
    NONE = 'none'
    LOW = 'low'
    MEDIUM = 'medium'
