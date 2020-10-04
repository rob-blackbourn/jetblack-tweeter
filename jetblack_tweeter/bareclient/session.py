"""A bareClient implementation of TweeterSession"""

import json
import io
from typing import Any, AsyncIterator, List, Mapping, Optional, Union
from urllib.error import HTTPError

from bareclient import HttpUnboundSession
from bareutils import text_reader
import bareutils.response_code as response_code

from ..types import AbstractTweeterSession

from .utils import to_lines

DUMMY_FP = io.BytesIO(b'')


class TweeterHttpError(HTTPError):

    def __init__(
            self,
            url: str,
            status_code: int,
            headers: Mapping[str, str],
            message: str
    ) -> None:
        super().__init__(
            url,
            status_code,
            message,
            headers,
            io.BytesIO(b'')
        )


class StreamError(TweeterHttpError):

    def __init__(
            self,
            url: str,
            status_code: int,
            headers: Mapping[str, str]
    ) -> None:
        super().__init__(
            url,
            status_code,
            headers,
            'stream request failed'
        )


class ApiError(TweeterHttpError):

    def __init__(
            self,
            url: str,
            status_code: int,
            headers: Mapping[str, str]
    ) -> None:
        super().__init__(
            url,
            status_code,
            headers,
            'api request failed'
        )


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
                raise StreamError(
                    url,
                    response['status_code'],
                    headers
                )

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
                raise ApiError(url, response['status_code'], headers)

            if not response['more_body']:
                raise ValueError('no data')

            content = await text_reader(response['body'])
            return json.loads(content)

    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        async with self._client.request(
            url,
            headers=[
                (name.encode(), value.encode())
                for name, value in headers.items()
            ],
            content=body.encode() if body else None
        ) as response:
            if not response_code.is_successful(response['status_code']):
                raise ApiError(url, response['status_code'], headers)

            if not response['more_body']:
                return None

            content = await text_reader(response['body'])
            return json.loads(content)
