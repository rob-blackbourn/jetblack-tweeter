"""A bareClient implementation of TweeterSession"""

import json
from typing import Any, AsyncIterator, List, Mapping, Optional, Union

from bareclient import HttpUnboundSession
from bareutils import text_reader, bytes_writer
import bareutils.response_code as response_code

from ...errors import ApiError, StreamError
from ...types import AbstractTweeterSession

from .utils import to_lines, make_headers


class BareTweeterSession(AbstractTweeterSession):
    """A tweeter session using BareASGI."""

    def __init__(self) -> None:
        self._client = HttpUnboundSession(
            protocols=('http/1.1')  # http/2 doesn't seem to work.
        )

    async def stream(
            self,
            url: str,
            method: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        bare_headers = make_headers(headers)
        buf = body.encode() if body else None
        content = bytes_writer(buf) if buf else None
        if buf:
            bare_headers.append(
                (b'content-length', str(len(buf)).encode())
            )

        async with self._client.request(
            url,
            method=method.upper(),
            headers=bare_headers,
            content=content
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
            headers: Mapping[str, str],
            timeout: Optional[float]
    ) -> Union[List[Any], Mapping[str, Any]]:
        async with self._client.request(
            url,
            headers=make_headers(headers)
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
            body: Optional[str],
            timeout: Optional[float]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        bare_headers = make_headers(headers)
        buf = body.encode() if body else None
        content = bytes_writer(buf) if buf else None
        if buf:
            bare_headers.append(
                (b'content-length', str(len(buf)).encode())
            )

        response_content: Optional[Union[List[Any], Mapping[str, Any]]] = None
        async with self._client.request(
            url,
            method='POST',
            headers=bare_headers,
            content=content
        ) as response:
            if not response_code.is_successful(response['status_code']):
                raise ApiError(url, response['status_code'], headers)

            if not response['more_body']:
                return None

            body = await text_reader(response['body'])
            response_content = json.loads(body)

        return response_content

    async def close(self) -> None:
        pass
