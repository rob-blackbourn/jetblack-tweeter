"""An aiohttp session"""

import json
from ssl import SSLContext
from typing import Any, AsyncIterator, List, Mapping, Optional, Union

from aiohttp import ClientSession, Fingerprint, ClientTimeout

from ...errors import ApiError
from ...types import AbstractTweeterSession

def _make_timeout(timeout: Optional[float]) -> Optional[ClientTimeout]:
    if timeout is None:
        return None
    else:
        return ClientTimeout(total=timeout)

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
            headers: Mapping[str, str],
            timeout: Optional[float]
    ) -> Union[List[Any], Mapping[str, Any]]:
        client_timeout = _make_timeout(timeout)
        async with self._client.get(
                url,
                headers=headers,
                ssl=self._ssl,
                timeout=client_timeout
        ) as response:
            if 400 <= response.status:
                raise ApiError(url, response.status, headers)
            return await response.json()

    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str],
            timeout: Optional[float]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        client_timeout = _make_timeout(timeout)
        data = body.encode() if body else None
        async with self._client.post(
                url,
                headers=headers,
                data=data,
                ssl=self._ssl,
                timeout=client_timeout
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def close(self) -> None:
        await self._client.close()
