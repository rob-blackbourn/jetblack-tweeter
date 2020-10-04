"""An aiohttp session"""

import json
from typing import Any, AsyncIterator, List, Mapping, Optional, Union

from aiohttp import ClientSession

from ...types import AbstractTweeterSession


class AiohttpTweeterSession(AbstractTweeterSession):

    def __init__(self) -> None:
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
                timeout=None
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
        async with self._client.get(url, headers=headers) as r:
            r.raise_for_status()
            return await r.json()

    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        data = body.encode() if body else None
        async with self._client.post(url, headers=headers, data=data) as r:
            r.raise_for_status()
            return await r.json()
