"""A bareClient implementation of TweeterSession"""

import json
from typing import Any, AsyncIterator, List, Mapping, Optional, Union

from bareclient import (
    HttpClient,
    HttpClientMiddlewareCallback as Middleware
)
from bareclient.middlewares import SessionMiddleware
from bareutils import (
    text_reader,
    bytes_writer
)


from ...errors import ApiError, StreamError
from ...types import AbstractTweeterSession

from .utils import to_lines, make_headers


class BareTweeterSession(AbstractTweeterSession):
    """A tweeter session using bareClient."""

    def __init__(self) -> None:
        self._middleware: List[Middleware] = []  # [SessionMiddleware()]

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

        async with HttpClient(
                url,
                method=method.upper(),
                headers=bare_headers,
                body=content,
                middleware=self._middleware,
                protocols=('http/1.1')
        ) as response:
            if not response.ok:
                raise StreamError(url, response.status, headers)

            if response.body is not None:
                buf = b''
                async for item in response.body:
                    lines, buf = to_lines(buf + item)
                    for line in lines:
                        yield json.loads(line.decode())

    async def get(
            self,
            url: str,
            headers: Mapping[str, str]
    ) -> Union[List[Any], Mapping[str, Any]]:
        bare_headers = make_headers(headers) + [
            (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')
        ]
        async with HttpClient(
                url,
                headers=bare_headers,
                middleware=self._middleware,
                protocols=('http/1.1')
        ) as response:
            if not response.ok:
                if response.body is not None:
                    text = await text_reader(response.body)
                    print(text)
                raise ApiError(url, response.status, headers)

            if response.body is None:
                raise ValueError('no data')

            content = await text_reader(response.body)
            return json.loads(content)

    async def post(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        bare_headers = make_headers(headers) + [
            (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')
        ]
        buf = body.encode() if body else None
        content = bytes_writer(buf) if buf else None
        if buf:
            bare_headers.append(
                (b'content-length', str(len(buf)).encode())
            )

        response_content: Optional[Union[List[Any], Mapping[str, Any]]] = None
        async with HttpClient(
                url,
                method='POST',
                headers=bare_headers,
                body=content,
                middleware=self._middleware,
                protocols=('http/1.1')
        ) as response:
            if not response.ok:
                raise ApiError(url, response.status, headers)

            if response.body is None:
                return None

            body = await text_reader(response.body)
            response_content = json.loads(body)

        return response_content

    async def put(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        bare_headers = make_headers(headers) + [
            (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')
        ]
        buf = body.encode() if body else None
        content = bytes_writer(buf) if buf else None
        if buf:
            bare_headers.append(
                (b'content-length', str(len(buf)).encode())
            )

        response_content: Optional[Union[List[Any], Mapping[str, Any]]] = None
        async with HttpClient(
                url,
                method='PUT',
                headers=bare_headers,
                body=content,
                middleware=self._middleware,
                protocols=('http/1.1')
        ) as response:
            if not response.ok:
                raise ApiError(url, response.status, headers)

            if response.body is None:
                return None

            body = await text_reader(response.body)
            response_content = json.loads(body)

        return response_content

    async def delete(
            self,
            url: str,
            headers: Mapping[str, str],
            body: Optional[str]
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        bare_headers = make_headers(headers) + [
            (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')
        ]
        buf = body.encode() if body else None
        content = bytes_writer(buf) if buf else None
        if buf:
            bare_headers.append(
                (b'content-length', str(len(buf)).encode())
            )

        response_content: Optional[Union[List[Any], Mapping[str, Any]]] = None
        async with HttpClient(
                url,
                method='DELETE',
                headers=bare_headers,
                body=content,
                middleware=self._middleware,
                protocols=('http/1.1')
        ) as response:
            if not response.ok:
                raise ApiError(url, response.status, headers)

            if response.body is None:
                return None

            body = await text_reader(response.body)
            response_content = json.loads(body)

        return response_content

    async def close(self) -> None:
        pass
