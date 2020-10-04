"""A bareClient implementation of TweeterSession"""

import json
from typing import Any, AsyncIterator, List, Mapping, Optional, Tuple, Union

from bareclient import HttpUnboundSession
from bareutils import text_reader
import bareutils.response_code as response_code

from ..types import AbstractTweeterSession

from .utils import to_lines


class BareTweeterSession(AbstractTweeterSession):

    def __init__(self) -> None:
        self._client = HttpUnboundSession()

    async def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        async with self._client.request(
            url,
            method=method.upper(),
            headers=[
                (name.encode(), value.encode())
                for name, value in headers.items()
            ],
            content=body.encode() if body else None
        ) as response:
            if not response_code.is_successful(response['status_code']):
                raise Exception('Failed')

            if response['more_body']:
                buf = b''
                async for item in response['body']:
                    lines, buf = to_lines(buf + item)
                    for line in lines:
                        yield json.loads(line.decode())

    async def get(
            self,
            url: str,
            headers: Mapping[str, str]
    ) -> Union[List[Any], Mapping[str, Any]]:
        async with self._client.request(
            url,
            headers=[
                (name.encode(), value.encode())
                for name, value in headers.items()
            ]
        ) as response:
            if not response_code.is_successful(response['status_code']):
                raise Exception('Failed')
            if not response['more_body']:
                raise Exception('No data')

            content = await text_reader(response['body'])
            return json.loads(content)
