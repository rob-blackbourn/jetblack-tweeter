"""Errors"""

import io
from typing import Mapping
from urllib.error import HTTPError


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
