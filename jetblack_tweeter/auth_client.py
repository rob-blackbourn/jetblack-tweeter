"""An HTTP client which uses oauth1 for authentication"""

from typing import Any, AsyncIterator, List, Mapping, Optional, Union
from urllib.parse import urlencode

from oauthlib.oauth1 import Client as OAuth1Client

from .types import AbstractHttpClient, AbstractTweeterSession
from .utils import clean_optional_dict, clean_dict


class AuthenticatedHttpClient(AbstractHttpClient):
    """An HTTP client that generates the headers for OAuth1 authentication"""

    def __init__(
            self,
            tweeter_session: AbstractTweeterSession,
            consumer_key: str,
            consumer_secret: str,
            *,
            access_token: Optional[str] = None,
            access_token_secret: Optional[str] = None
    ) -> None:
        """Initialise the authenticated HTTP client.

        Args:
            tweeter_session (AbstractTweeterSession): The tweeter session
                implementation.
            consumer_key (str): THe OAuth1 consumer key
            consumer_secret (str): The OAuth1 consumer secret.
            access_token (Optional[str], optional): The OAuth1 access
                token. Defaults to None.
            access_token_secret (Optional[str], optional): The Oauth1 access
                token secret. Defaults to None.
        """
        self._client = tweeter_session
        self._oauth_client = OAuth1Client(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )

    def stream(
        self,
        url: str,
        data: Optional[Mapping[str, Any]] = None,
        method: str = 'post'
    ) -> AsyncIterator[Union[List[Any], Mapping[str, Any]]]:
        url, headers, body = self._oauth_client.sign(
            url,
            headers={} if data is None else {
                'content-type': 'application/x-www-form-urlencoded',
            },
            body=urlencode(clean_dict(data)) if data else None,
            http_method=method.upper(),
        )
        return self._client.stream(  # type: ignore
            url,
            method,
            headers,
            body
        )

    async def get(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None
    ) -> Union[List[Any], Mapping[str, Any]]:
        data = clean_optional_dict(params)
        url, headers, _ = self._oauth_client.sign(
            url + (f'?{urlencode(data)}' if data else ''),
            http_method='GET',
        )
        return await self._client.get(url, headers, timeout)

    async def post(
            self,
            url: str,
            params: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None
    ) -> Optional[Union[List[Any], Mapping[str, Any]]]:
        data = clean_optional_dict(params)
        url, headers, _ = self._oauth_client.sign(
            url + (f'?{urlencode(data)}' if data else ''),
            http_method='POST'
        )
        return await self._client.post(url, headers, None, timeout)

    async def close(self) -> None:
        await self._client.close()
