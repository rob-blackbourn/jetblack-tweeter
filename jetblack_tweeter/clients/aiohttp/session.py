"""An aiohttp session"""

import json
from ssl import SSLContext
from typing import Any, AsyncIterator, List, Mapping, Optional, Union

from aiohttp import ClientSession, Fingerprint

from ...types import AbstractTweeterSession


class AiohttpTweeterSession(AbstractTweeterSession):
    """A tweeter session using aiohttp."""

    def __init__(
            self,
            *,
            ssl: Optional[Union[SSLContext, bool, Fingerprint]] = None
    ) -> None:
        self._ssl = ssl
        self._client = ClientSession()

    async def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        async with self._client.request(
                method.upper(),
                url,
                headers=headers,
                data=body,
                timeout=None,
                ssl=self._ssl
        ) as response:
            response.raise_for_status()
            async for line in response.content:
                if not line.strip():
                    continue
                yield json.loads(line)

    async def get(
            self,
            url: str,
            headers: Mapping[str, str]
    ) -> Union[List[Any], Mapping[str, Any]]:
        async with self._client.get(
                url,
                headers=headers,
                ssl=self._ssl
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        data = body.encode() if body else None
        async with self._client.post(
                url,
                headers=headers,
                data=data,
                ssl=self._ssl
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def close(self) -> None:
        await self._client.close()
